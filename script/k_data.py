from mongoengine import connect, Document
from mongoengine import StringField, FloatField, DateTimeField
from multiprocessing import Pool
import datetime
import pdb


connect('vcoin')

# From source
class Ticker(Document):
    pair = StringField(required=True)
    baseVolume = FloatField()
    high24hr = FloatField()
    highestBid = FloatField()
    last = FloatField()
    low24hr = FloatField()
    lowestAsk = FloatField()
    percentChange = FloatField()
    quoteVolume = FloatField()
    date = DateTimeField(required=True)

# To source
class K15m(Document):
    code = StringField(required=True)
    open = FloatField()
    high = FloatField()
    low = FloatField()
    close = FloatField()
    volume = FloatField()
    date = DateTimeField(required=True)
    buf_size = 90

def transform(pair, k_cls):
    buf = []
    volume = 0
    for price in Ticker.objects(pair=pair).order_by('date'):
        buf.append(price.last)
        volume += price.quoteVolume
        if len(buf) == k_cls.buf_size:
            dt = datetime.datetime(price.date.year, price.date.month, price.date.day, price.date.hour, price.date.minute)
            m15 = k_cls(code=pair, open=buf[0], high=max(buf), low=min(buf), close=buf[-1], volume=volume, date=dt)
            m15.save()
            buf = []
            volume = 0


if __name__ == '__main__':
    pool = Pool()
    pair_list = []
    K15m.drop_collection()
    for pair in Ticker.objects.distinct('pair'):
         if pair.find('_usdt') > 0:
             pool.apply_async(transform, (pair, K15m))
             #transform(pair, K15m)
             pair_list.append(pair)
         else:
             print('Skiped %s ...' % pair)
    print('Loading finished')
    pool.close()
    pool.join()
    # Remove new added coins
    flag_cnt = K15m.objects(code='btc_usdt').count()
    for pair in pair_list:
        cnt = K15m.objects(code=pair).count()
        if cnt != flag_cnt:
            K15m.objects(code=pair).delete()
            pair_list.remove(pair)
            print('Detele %s as it count %s < %s' % (pair, cnt, flag_cnt))
    # Report
    min_date = K15m.objects[:1].order_by('date')[0].date
    max_date = K15m.objects[:1].order_by('-date')[0].date
    print(pair_list)
    print('Min date is: %s' % min_date)
    print('Max date is: %s' % max_date)
    print('pair count = %s' % len(pair_list))
