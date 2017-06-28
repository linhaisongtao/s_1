import urllib2
import json, os, datetime


#
# print resultString
# open("a.json", "w").write(resultString)

class PB(object):
    pb = 0
    date = ""
    pass


class PBS(object):

    def __init__(self):
        self.name = ""
        self.pb_list =[]
        self.code = ""
        pass
    pass


def request_net(code):
    now_date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    if not os.path.exists("pb"):
        os.mkdir("pb")
        pass
    file_name = "pb/%s_%s.json" % (code, now_date_str)

    if os.path.exists(file_name):
        print "read from file", file_name
        return open(file_name, "r").read()
        pass
    else:
        body = "{\"stockCode\":\"%s\"}" % code
        url = "http://www.51shiyinglv.com/stockservice.svc/GetPEByStockCode"
        cookie = "ASP.NET_SessionId=hypb24xlqiitk0gujkjzfnxr"
        request = urllib2.Request(url, body)
        request.add_header("Cookie", cookie)
        request.add_header("Content-Type", "application/json")
        result = urllib2.urlopen(request)
        resultString = result.read()
        open(file_name, "w").write(resultString)

        print "read from net"
        return resultString
        pass
    pass


def request_pbs(code):
    pbs = PBS()

    resultString = request_net(code)
    json_object = json.loads(resultString, encoding="utf-8")
    pbs.code = json_object['d']['Result']['StockCode']
    pbs.name = json_object['d']['Result']['StockName']
    pb_list = json_object['d']['Result']['PBValues']['data']
    dates = json_object['d']['Result']['PBValues']['categories']
    for i, d in enumerate(dates):
        pb = PB()
        pb.pb = pb_list[i]
        pb.date = d
        pbs.pb_list.append(pb)
        pass
    return pbs
    pass

