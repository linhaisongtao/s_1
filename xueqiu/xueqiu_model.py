import datetime
import json
import urllib
import urllib2
import csv
import codecs
import os
import xlwt

result_dir = "stock"

now_date = datetime.datetime.now().strftime("%Y-%m-%d")
now = datetime.datetime.now()

if (not os.path.exists(result_dir)) or (not os.path.isdir(result_dir)):
    os.mkdir(result_dir)
    pass


def write_to_excel_top(list, file_name, top):
    l = []
    for i in range(1, top + 1):
        l.append(list[i])
        pass
    write_to_excel(l, "top_%d_" % top + file_name)
    pass


def write_to_excel(list, file_name):
    wb = xlwt.Workbook(encoding='utf-8')
    sh = wb.add_sheet("a")
    c = 0
    sh.write(0, c, 'name')
    c += 1
    sh.write(0, c, 'code')
    c += 1
    sh.write(0, c, 'price')
    c += 1
    sh.write(0, c, 'score')
    c += 1
    sh.write(0, c, 'pettm')
    c += 1
    sh.write(0, c, 'pb')
    c += 1
    sh.write(0, c, 'benefit')
    c += 1
    sh.write(0, c, "r1")
    c += 1
    sh.write(0, c, "r3")
    c += 1
    sh.write(0, c, "r5")
    c += 1
    sh.write(0, c, "r6")
    c += 1
    sh.write(0, c, 'roe_2017')
    c += 1
    sh.write(0, c, 'roe_2016')
    c += 1
    sh.write(0, c, 'roe_2015')
    c += 1
    sh.write(0, c, 'roe_2014')
    c += 1
    sh.write(0, c, 'roe_2013')
    c += 1
    sh.write(0, c, 'roe_2012')
    for i, s in enumerate(list):
        c = 0
        index = i + 1
        sh.write(index, c, s['name'])
        c += 1
        sh.write(index, c, s['code'])
        c += 1
        sh.write(index, c, "%.2f" % s['price'])
        c += 1
        sh.write(index, c, s['score'])
        c += 1
        sh.write(index, c, "%.2f" % s['pettm'])
        c += 1
        sh.write(index, c, "%.2f" % s['pb'])
        c += 1
        sh.write(index, c, "%.2f" % (s['benefit']))
        c += 1
        sh.write(index, c, "%.2f" % (s["r1"]))
        c += 1
        sh.write(index, c, "%.2f" % (s["r3"]))
        c += 1
        sh.write(index, c, "%.2f" % (s["r5"]))
        c += 1
        sh.write(index, c, "%.2f" % (s["r6"]))
        c += 1
        sh.write(index, c, "%.2f" % (s['roe_2017']))
        c += 1
        sh.write(index, c, "%.2f" % (s['roe_2016']))
        c += 1
        sh.write(index, c, "%.2f" % (s['roe_2015']))
        c += 1
        sh.write(index, c, "%.2f" % (s['roe_2014']))
        c += 1
        sh.write(index, c, "%.2f" % (s['roe_2013']))
        c += 1
        sh.write(index, c, "%.2f" % (s['roe_2012']))

    wb.save(result_dir + "/" + file_name)
    pass
