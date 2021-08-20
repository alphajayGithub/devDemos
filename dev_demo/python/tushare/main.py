#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import tushare as ts

# https://tushare.pro/document/1?doc_id=40
# ts.set_token('23318edf2e09200749f4cbafb9a376508c2c47594be5ecd225d29766')
pro = ts.pro_api('23318edf2e09200749f4cbafb9a376508c2c47594be5ecd225d29766')


df = pro.query('trade_cal', exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')


'''
#需要200积分才能调用期货数据接口
#获取CU1811合约20180101～20181113期间的行情
df = pro.fut_daily(ts_code='CU1811.SHF', start_date='20180101', end_date='20181113')
'''

#获取2018年11月13日大商所全部合约行情数据
df = pro.fut_daily(trade_date='20181113', exchange='DCE', fields='ts_code,trade_date,pre_close,pre_settle,open,high,low,close,settle,vol')


print(df)