# coding=utf-8

import argparse

#stock_codes = ["600036", "601328", "601998", "601398"]
stock_codes = ["600036"]
future_codes = ["AU88", "RB88", "CU88", "AL88"]
vcoin_codes = ['abt_usdt', 'ada_usdt', 'ae_usdt', 'bat_usdt', 'bcd_usdt', 'bcdn_usdt', 'bch_usdt', 'bcx_usdt', 'bft_usdt', 'bifi_usdt', 'blz_usdt', 'bnty_usdt', 'bot_usdt', 'btc_usdt', 'btf_usdt', 'btg_usdt', 'btm_usdt', 'bto_usdt', 'bts_usdt', 'cdt_usdt', 'cofi_usdt', 'cs_usdt', 'cvc_usdt', 'dadi_usdt', 'dai_usdt', 'dash_usdt', 'data_usdt', 'dbc_usdt', 'ddd_usdt', 'dgd_usdt', 'dock_usdt', 'doge_usdt', 'dpy_usdt', 'drgn_usdt', 'elec_usdt', 'elf_usdt', 'eos_usdt', 'etc_usdt', 'eth_usdt', 'fil_usdt', 'fuel_usdt', 'fun_usdt', 'gas_usdt', 'gem_usdt', 'gnt_usdt', 'gnx_usdt', 'god_usdt', 'gtc_usdt', 'gxs_usdt', 'hav_usdt', 'hsr_usdt', 'icx_usdt', 'iht_usdt', 'ink_usdt', 'iota_usdt', 'jnt_usdt', 'kick_usdt', 'knc_usdt', 'lend_usdt', 'link_usdt', 'lrc_usdt', 'lrn_usdt', 'lsk_usdt', 'ltc_usdt', 'lun_usdt', 'lym_usdt', 'man_usdt', 'mana_usdt', 'mco_usdt', 'mda_usdt', 'mds_usdt', 'mdt_usdt', 'med_usdt', 'mith_usdt', 'mkr_usdt', 'mobi_usdt', 'mtn_usdt', 'nano_usdt', 'nas_usdt', 'neo_usdt', 'ocn_usdt', 'omg_usdt', 'ont_usdt', 'ost_usdt', 'pay_usdt', 'powr_usdt', 'pst_usdt', 'qash_usdt', 'qbt_usdt', 'qlc_usdt', 'qsp_usdt', 'qtum_usdt', 'rcn_usdt', 'rdn_usdt', 'rem_usdt', 'req_usdt', 'rfr_usdt', 'rlc_usdt', 'ruff_usdt', 'salt_usdt', 'sbtc_usdt', 'senc_usdt', 'skm_usdt', 'smt_usdt', 'snet_usdt', 'snt_usdt', 'storj_usdt', 'stx_usdt', 'swth_usdt', 'theta_usdt', 'tio_usdt', 'tnc_usdt', 'tnt_usdt', 'tomo_usdt', 'trx_usdt', 'tsl_usdt', 'ven_usdt', 'waves_usdt', 'xlm_usdt', 'xmc_usdt', 'xmr_usdt', 'xrp_usdt', 'xtz_usdt', 'xvg_usdt', 'zec_usdt', 'zil_usdt', 'zpt_usdt', 'zrx_usdt', 'zsc_usdt']

stock_spider_parser = argparse.ArgumentParser()
stock_spider_parser.add_argument("-c", "--codes", default=vcoin_codes, nargs="+")
stock_spider_parser.add_argument("-s", "--start", default="2008-01-01")
stock_spider_parser.add_argument("-e", "--end", default="2018-01-01")

future_spider_parser = argparse.ArgumentParser()
future_spider_parser.add_argument("-c", "--codes", default=future_codes, nargs="+")
future_spider_parser.add_argument("-s", "--start", default="2008-01-01")
future_spider_parser.add_argument("-e", "--end", default="2018-01-01")

vcoin_spider_parser = argparse.ArgumentParser()
vcoin_spider_parser.add_argument("-c", "--codes", default=vcoin_codes, nargs="+")
vcoin_spider_parser.add_argument("-s", "--start", default="2008-01-01")
vcoin_spider_parser.add_argument("-e", "--end", default="2018-01-01")

model_launcher_parser = argparse.ArgumentParser()
model_launcher_parser.add_argument("-c", "--codes", default=vcoin_codes, nargs="+")
model_launcher_parser.add_argument("-s", "--start", default="2008-01-01")
model_launcher_parser.add_argument("-e", "--end", default="2018-01-01")
model_launcher_parser.add_argument("--mode", default="train")
model_launcher_parser.add_argument("--market", default="stock")
model_launcher_parser.add_argument("--episode", default=500, type=int)
model_launcher_parser.add_argument("--train_steps", default=100000, type=int)
model_launcher_parser.add_argument("--training_data_ratio", default=0.8, type=float)
