import xueqiu_source as xs

MIN_BENEFIT = 3
TOP_1_R = 15
TOP_2_R = 10

stocks = xs.get_stocks()

for s in stocks:
    roe2017 = s['roe_2017'] * 4
    roe2016 = s['roe_2016']
    roe2015 = s['roe_2015']
    roe2014 = s['roe_2014']
    roe2013 = s['roe_2013']
    roe2012 = s['roe_2012']
    pb = s['pb']
    s['r6'] = (roe2017 + roe2016 + roe2015 + roe2014 + roe2013 + roe2012) / 6 / pb
    s['r5'] = (roe2016 + roe2015 + roe2014 + roe2013 + roe2012) / 5 / pb
    s['r3'] = (roe2016 + roe2015 + roe2014) / 3 / pb
    s['r1'] = (roe2016) / 1 / pb

    s['score'] = 0
    if (s['r6'] >= TOP_1_R):
        s['score'] = s['score'] + 2
        pass
    elif (s['r6'] >= TOP_2_R):
        s['score'] = s['score'] + 1
        pass

    if (s['r5'] >= TOP_1_R):
        s['score'] = s['score'] + 2
        pass
    elif (s['r5'] >= TOP_2_R):
        s['score'] = s['score'] + 1
        pass

    if (s['r3'] >= TOP_1_R):
        s['score'] = s['score'] + 2
        pass
    elif (s['r3'] >= TOP_2_R):
        s['score'] = s['score'] + 1
        pass

    if (s['r1'] >= TOP_1_R):
        s['score'] = s['score'] + 2
        pass
    elif (s['r1'] >= TOP_2_R):
        s['score'] = s['score'] + 1
        pass

    if (s['benefit'] >= MIN_BENEFIT):
        s['score'] = s['score'] + 2
        pass
    pass


def cmp1(o1, o2):
    if (o2['score'] == o1['score']):
        return (int)(1000 * (o2['r1'] - o1['r1']))
        pass
    else:
        return o2['score'] - o1['score']
        pass
    pass


stocks = sorted(stocks, cmp=cmp1)

import xueqiu_model as xm
xm.write_to_excel(stocks, "all_" + xs.now_date + ".xls")
xm.write_to_excel_top(stocks, xs.now_date + ".xls", 50)
xm.write_to_excel_top(stocks, xs.now_date + ".xls", 30)
xm.write_to_excel_top(stocks, xs.now_date + ".xls", 15)
import source
print source.get_selected_stocks()

