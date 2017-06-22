import os
import tushare as ts
import pandas as pd
import csv
import model

import datetime
import json
import urllib
import urllib2
import csv
import codecs
import os

if (not os.path.exists('_source')) or (not os.path.isdir('_source')):
    os.mkdir("_source")
    pass

def convert_selected_codes_to_map(code_list):
    code_map = {}
    for c in code_list:
        code_map[c] = c
        pass
    return code_map
    pass

def get_selected_stocks():
    f = open('_source/source.txt')
    lines = f.readlines()
    stocks = []
    for l in lines:
        stocks.append(l.replace("\n", ""))
        pass
    return stocks
    pass


def get_hs300_codes():
    s = []
    # stock
    if not os.path.exists("_stock/hs300.csv"):
        df = ts.get_hs300s()
        df.to_csv("_stock/hs300.csv")
        pass
    reader = csv.reader(open("_stock/hs300.csv"))

    for i, row in enumerate(reader):
        if i != 0:
            s.append(row[1])
            pass
        pass

    return s
    pass


def get_zz500_codes():
    s = []
    # stock
    if not os.path.exists("_stock/zz500.csv"):
        df = ts.get_zz500s()
        df.to_csv("_stock/zz500.csv")
        pass
    reader = csv.reader(open("_stock/zz500.csv"))

    for i, row in enumerate(reader):
        if i != 0:
            s.append(row[1])
            pass
        pass

    return s
    pass


def get_sz50_codes():
    s = []
    # stock
    if not os.path.exists("_stock/sz50.csv"):
        df = ts.get_sz50s()
        df.to_csv("_stock/sz50.csv")
        pass
    reader = csv.reader(open("_stock/sz50.csv"))

    for i, row in enumerate(reader):
        if i != 0:
            s.append(row[1])
            pass
        pass

    return s
    pass

def get_lixinger_stocks():
    json_file = "net_result.json"
    if not (os.path.exists(json_file)):
        print "source------>request lixinger"
        body = "{\"area\":\"cn\",\"ranges\":{\"stockCollectionIdsList\":[[],[10000000300]]},\"filterItems\":[{\"id\":\"stockPriceMetrics.pb\",\"date\":\"\",\"min\":0,\"max\":5},{\"id\":\"stockPriceMetrics.pb_wo_gw\",\"date\":\"\",\"min\":0,\"max\":5},{\"id\":\"metrics.roe.t\",\"date\":\"2016-12-31\",\"min\":0.09,\"max\":\"\"},{\"id\":\"metrics.roe.t\",\"date\":\"2015-12-31\",\"min\":0.09,\"max\":\"\"},{\"id\":\"metrics.roe.t\",\"date\":\"2014-12-31\",\"min\":0.09,\"max\":\"\"},{\"id\":\"metrics.roe.t\",\"date\":\"2013-12-31\",\"min\":0.09,\"max\":\"\"},{\"id\":\"metrics.roe.t\",\"date\":\"2012-12-31\",\"min\":0.09,\"max\":\"\"},{\"id\":\"stockPriceMetrics.dividend_r\",\"date\":\"\",\"min\":\"\",\"max\":\"\"},{\"id\":\"stockPriceMetrics.pe_ttm\",\"date\":\"\",\"min\":\"\",\"max\":\"\"},{\"id\":\"stockPriceMetrics.stock_price\",\"date\":\"\",\"min\":\"\",\"max\":\"\"}],\"sort\":{\"name\":\"stockPriceMetrics.pb\",\"order\":\"desc\"}}"
        url = "https://www.lixinger.com/api/analyt/screener/stock"
        cookie = "jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1OTNhMTBjYjg3NDQ5NzY3NWYwYTU2N2QiLCJpYXQiOjE0OTc4MzY3NDksImV4cCI6MTQ5ODQ0MTU0OX0.Jl4r6wCSIRH41ZPXfWS4_jetZeV2EBxVKoW20MY6p9I; Hm_lvt_ec0ee7e5c8bed46d4fdf3f338afc08f5=1497836726,1497836762; Hm_lpvt_ec0ee7e5c8bed46d4fdf3f338afc08f5=1497836771"
        request = urllib2.Request(url, body)
        request.add_header("Cookie", cookie)
        request.add_header("Content-Type", "application/json;charset=UTF-8")
        result = urllib2.urlopen(request)
        resultString = result.read()
        print "source------>receive lixinger"
        open(json_file, "w").write(resultString)
        pass

    print "source------>read file[%s]" % json_file
    jsonObject = json.load(open(json_file, "r"))

    stockList = []

    jsonArray = jsonObject["data"]
    for o in jsonArray:
        d = {}
        d["code"] = o["stockCode"]
        d["name"] = o["cnName"]

        d["price"] = o["stockPriceMetrics"]["stock_price"]
        d["benefit"] = o["stockPriceMetrics"]["dividend_r"]
        d["pe"] = o["stockPriceMetrics"]["pe_ttm"]
        d["pb"] = o["stockPriceMetrics"]["pb"]
        d["pb_no_corp"] = o["stockPriceMetrics"]["pb_wo_gw"]

        d["roe2012"] = o["2012-12-31"]["metrics"]["roe"]["t"]
        d["roe2013"] = o["2013-12-31"]["metrics"]["roe"]["t"]
        d["roe2014"] = o["2014-12-31"]["metrics"]["roe"]["t"]
        d["roe2015"] = o["2015-12-31"]["metrics"]["roe"]["t"]
        d["roe2016"] = o["2016-12-31"]["metrics"]["roe"]["t"]
        stockList.append(d)

    # after clock15
    if model.now.hour <= 1.5:
        os.remove(json_file)
        print "source------>delete file[%s]" % json_file
        pass

    return stockList
    pass
