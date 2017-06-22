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


def cmp1(o1, o2):
    if o2['count'] == o1['count']:
        return (int)(10000 * (o2['r1'] - o1['r1']))
        pass
    else:
        return o2['count'] - o1['count']
        pass
    pass


def write_to_excel(list, file_name):
    list = sorted(list, cmp=cmp1)

    wb = xlwt.Workbook(encoding='utf-8')
    sh = wb.add_sheet("a")
    c = 0
    sh.write(0, c, 'name')
    c += 1
    sh.write(0, c, 'code')
    c += 1
    sh.write(0, c, 'price')
    c += 1
    sh.write(0, c, 'count')
    c += 1
    sh.write(0, c, 'score')
    if list[0].has_key('benefit'):
        c += 1
        sh.write(0, c, 'benefit')
        pass
    c += 1
    sh.write(0, c, 'pe')
    c += 1
    sh.write(0, c, 'pb')
    c += 1
    sh.write(0, c, 'r')
    c += 1
    sh.write(0, c, 'r1')
    c += 1
    sh.write(0, c, 'r3')
    c += 1
    sh.write(0, c, 'r5')
    c += 1
    sh.write(0, c, 'roe2017')
    c += 1
    sh.write(0, c, 'roe2016')
    c += 1
    sh.write(0, c, 'roe2015')
    c += 1
    sh.write(0, c, 'roe2014')
    c += 1
    sh.write(0, c, 'roe2013')
    c += 1
    sh.write(0, c, 'roe2012')
    for i, s in enumerate(list):
        c = 0
        sh.write(i + 1, c, s['name'])
        c += 1
        sh.write(i + 1, c, s['code'])
        c += 1
        sh.write(i + 1, c, "%.2f" % s['price'])
        c += 1
        sh.write(i + 1, c, s['count'])
        c += 1
        score = 0
        if s.has_key('score'):
            score = s['score']
            pass
        sh.write(i + 1, c, score)
        if s.has_key('benefit'):
            c += 1
            sh.write(i + 1, c, "%.2f%%" % (s['benefit'] * 100))
            pass
        c += 1
        sh.write(i + 1, c, "%.2f" % s['pe'])
        c += 1
        sh.write(i + 1, c, "%.2f" % s['pb'])
        c += 1
        r = 0
        if s.has_key('r'):
            r = s['r']
            pass
        sh.write(i + 1, c, "%.2f" % r)
        c += 1
        sh.write(i + 1, c, "%.3f" % s['r1'])
        c += 1
        sh.write(i + 1, c, "%.3f" % s['r3'])
        c += 1
        sh.write(i + 1, c, "%.3f" % s['r5'])
        c += 1
        roe2017 = 0
        if s.has_key('roe_2017_1'):
            roe2017 = s['roe_2017_1']
            pass
        sh.write(i + 1, c, "%.3f" % roe2017)
        c += 1

        if s.has_key('roe_2016_4'):
            roe2016 = s['roe_2016_4']
            pass
        else:
            roe2016 = s['roe2016']
            pass
        sh.write(i + 1, c, "%.3f" % roe2016)
        c += 1

        if s.has_key('roe_2015_4'):
            roe2015 = s['roe_2015_4']
            pass
        else:
            roe2015 = s['roe2015']
            pass
        sh.write(i + 1, c, "%.3f" % roe2015)
        c += 1

        if s.has_key('roe_2014_4'):
            roe2014 = s['roe_2014_4']
            pass
        else:
            roe2014 = s['roe2014']
            pass
        sh.write(i + 1, c, "%.3f" % roe2014)
        c += 1

        if s.has_key('roe_2013_4'):
            roe2013 = s['roe_2013_4']
            pass
        else:
            roe2013 = s['roe2013']
            pass
        sh.write(i + 1, c, "%.3f" % roe2013)
        c += 1

        if s.has_key('roe_2012_4'):
            roe2012 = s['roe_2012_4']
            pass
        else:
            roe2012 = s['roe2012']
            pass
        sh.write(i + 1, c, "%.3f" % roe2012)
        pass
    wb.save(result_dir + "/" + file_name)
    pass
