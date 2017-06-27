import S
import pandas as pd
import datetime
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def get_attr_list(list, attr):
    attrs = []
    for l in list:
        v = getattr(l, attr)
        if isinstance(v, float):
            attrs.append("%.2f" % v)
            pass
        else:
            attrs.append(v)
            pass
        pass

    return attrs
    pass


list = S.read_from_xls()
S.compute_with_lastest_price(list)

column_names = ['name', 'code', "current", 'pbCurrent', 'price2', 'pb2', 'price5', 'pb5', 'roe2', 'roe5', 'roe2017',
                'roe2016', 'roe2015', 'roe2014', 'roe2013', 'roe2012', 'roe2011', 'roe2010']
data = {}
for c in column_names:
    data[c] = get_attr_list(list, c)
    pass

df = pd.DataFrame(data, columns=column_names)

if not os.path.exists("s"):
    os.mkdir("s")
    pass
now_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
df.to_excel("s/" + now_str + ".xls")


import chart
chart.S_UI(list).show()