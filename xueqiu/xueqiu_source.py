import urllib2
import urllib, json, os
import thread, threading
import datetime, time

timestamp = (long)(time.time() * 1000)
now_date = datetime.datetime.now().strftime("%Y-%m-%d")
url = "https://xueqiu.com/stock/screener/screen.json?category=SH&exchange=&areacode=&indcode=&orderby=symbol&order=desc&current=ALL&pct=ALL&page=1&pb=0_5&roediluted.20170331=0_100&pettm=0_50&dy=0_9.79&_=1498112302285"


def get_xueqiu_stocks(url):
    cookie = "u=691496828345862; s=ew15skiac9; webp=0; aliyungf_tc=AQAAAPAMpALfyAMA/jdr2ts8oaP6w6OQ; xq_a_token=445b4b15f59fa37c8bd8133949f910e7297a52ef; xq_a_token.sig=5qsKG3NMR_Go5O8QjcKxalfFwhM; xq_r_token=132b2ba19b0053bc7f04401788b6e0d24f35d365; xq_r_token.sig=1w18Bj12xS0s6jGzDJnEQgA8IGo; device_id=0e265d4368be601f15cc880fe55a241b; __utma=1.368657217.1497955103.1497955103.1498112219.2; __utmc=1; __utmz=1.1497955103.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_1db88642e346389874251b5a1eded6e3=1496828346,1497951524,1497955103,1498112213; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1498112283"
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    request = urllib2.Request(url)
    request.add_header("Cookie", cookie)
    request.add_header("User-Agent", user_agent)
    result = urllib2.urlopen(request)

    resultString = result.read()

    return resultString
    pass


url_roe2017 = "https://xueqiu.com/stock/screener/screen.json?category=SH&exchange=&areacode=&indcode=&orderby=symbol&order=desc&current=ALL&pct=ALL&page=%d&roediluted.20170331=0_1000&_=" + (
    "%s" % timestamp)
url_roe2016 = "https://xueqiu.com/stock/screener/screen.json?category=SH&exchange=&areacode=&indcode=&orderby=symbol&order=desc&current=ALL&pct=ALL&page=%d&roediluted.20161231=0_1000&_=" + (
    "%s" % timestamp)
url_roe2015 = "https://xueqiu.com/stock/screener/screen.json?category=SH&exchange=&areacode=&indcode=&orderby=symbol&order=desc&current=ALL&pct=ALL&page=%d&roediluted.20151231=0_1000&_=" + (
    "%s" % timestamp)
url_roe2014 = "https://xueqiu.com/stock/screener/screen.json?category=SH&exchange=&areacode=&indcode=&orderby=symbol&order=desc&current=ALL&pct=ALL&page=%d&roediluted.20141231=0_1000&_=" + (
    "%s" % timestamp)
url_roe2013 = "https://xueqiu.com/stock/screener/screen.json?category=SH&exchange=&areacode=&indcode=&orderby=symbol&order=desc&current=ALL&pct=ALL&page=%d&roediluted.20131231=0_1000&_=" + (
    "%s" % timestamp)
url_roe2012 = "https://xueqiu.com/stock/screener/screen.json?category=SH&exchange=&areacode=&indcode=&orderby=symbol&order=desc&current=ALL&pct=ALL&page=%d&roediluted.20121231=0_1000&_=" + (
    "%s" % timestamp)
url_basic = "https://xueqiu.com/stock/screener/screen.json?category=SH&exchange=&areacode=&indcode=&orderby=symbol&order=desc&current=0_472.75&pct=ALL&page=%d&dy=0_100&pb=0.1_17000&pettm=0_121907.1009&_=" + (
    "%s" % timestamp)

url_reo_map = {'roe_2017': url_roe2017, 'roe_2016': url_roe2016, 'roe_2015': url_roe2015, 'roe_2014': url_roe2014,
               'roe_2013': url_roe2013,
               'roe_2012': url_roe2012, 'basic': url_basic}
url_reo_map['basic_%s' % now_date] = url_basic


def get_data(key, page_no):
    dir_name = key
    file_name = "%s/page_%d" % (dir_name, page_no)
    if not os.path.exists(file_name):
        url = url_reo_map[key]
        print "request page %s %d" % (key, page_no)
        result_string = get_xueqiu_stocks(url % (page_no))
        # save to file
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
            pass
        open(file_name, "w").write(result_string)

        print "request page %s %d" % (key, page_no), "success"
    else:
        print "read from file[%s]" % file_name
        result_string = open(file_name).read()
        pass

    return result_string
    pass


def get_roe_from_net(year):
    result_string = get_data(year, 1)
    json_object = json.loads(result_string, encoding="utf-8")
    total_count = json_object['count']

    threads = []
    for i in range(1, total_count / 30 + 1):
        t = threading.Thread(target=get_data, args=(year, i))
        threads.append(t)
        t.start()
        pass
    for t in threads:
        t.join()
    pass


get_roe_from_net('roe_2017')
get_roe_from_net('roe_2016')
get_roe_from_net('roe_2015')
get_roe_from_net('roe_2014')
get_roe_from_net('roe_2013')
get_roe_from_net('roe_2012')
get_roe_from_net('basic_%s' % now_date)


def get_json_object_from_file(file_name):
    str = open(file_name, "r").read()
    return json.loads(str, encoding='utf-8')


def get_json_object_list_from_dir(dir_name):
    files = os.listdir(dir_name)
    l = []
    for f in files:
        l.append(get_json_object_from_file(dir_name + "/" + f))
        pass
    return l
    pass


def get_roe_map_from_dir(dir_name, keyword):
    stocks = {}
    objects = get_json_object_list_from_dir(dir_name)
    for o in objects:
        list = o['list'];
        for l in list:
            m = {}
            m['code'] = l['symbol']
            m['roe'] = l['roediluted'][keyword]
            m['key'] = dir_name
            stocks[m['code']] = m
            pass
        pass

    return stocks
    pass


roes = []
roes.append(get_roe_map_from_dir('roe_2017', '20170331'))
roes.append(get_roe_map_from_dir('roe_2016', '20161231'))
roes.append(get_roe_map_from_dir('roe_2015', '20151231'))
roes.append(get_roe_map_from_dir('roe_2014', '20141231'))
roes.append(get_roe_map_from_dir('roe_2013', '20131231'))
roes.append(get_roe_map_from_dir('roe_2012', '20121231'))

print 'origin data got success'


def get_basic_info_from_dir(dir_name):
    stocks = []
    objects = get_json_object_list_from_dir(dir_name)
    for o in objects:
        list = o['list'];
        for l in list:
            m = {}
            m['code'] = l['symbol']
            m['name'] = l['name']
            m['pettm'] = float(l['pettm'])
            m['pb'] = float(l['pb'])
            m['price'] = float(l['current'])
            m['benefit'] = float(l['dy'])
            stocks.append(m)
            pass
        pass
    return stocks
    pass


def get_stocks():
    all = []
    basics = get_basic_info_from_dir('basic_%s' % now_date)
    for b in basics:
        code = b['code']
        select_it = True
        for r in roes:
            if r.has_key(code):
                m = r[code]
                key = m['key']
                roe = float(m['roe'])
                b[key] = roe
            else:
                select_it = False
                break
            pass

        if select_it:
            all.append(b)
        pass
    return all
    pass


print "success"
