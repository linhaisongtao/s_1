MIN_R = 0.1
MAX_PE = 20
MIN_BENEFIT = 0.036

def process(stockList):
    for o in stockList:
        o["r1"] = o["roe2016"] / o["pb_no_corp"]
        o["r3"] = (o["roe2016"] + o["roe2015"] + o["roe2014"]) / 3 / o["pb_no_corp"]
        o['roe_average_5'] = (o["roe2016"] + o["roe2015"] + o["roe2014"] + o["roe2013"] + o["roe2012"]) / 5
        o["r5"] = o['roe_average_5'] / o["pb_no_corp"]
        count = 0
        if (o["r1"] >= MIN_R):
            count = count + 1
            o['r1Ok'] = True
        else:
            o['r1Ok'] = False

        if o["r3"] >= MIN_R:
            count = count + 1
            o['r3Ok'] = True
        else:
            o['r3Ok'] = False

        if o["r5"] >= MIN_R:
            count = count + 1
            o['r5Ok'] = True
        else:
            o['r5Ok'] = False

        if o["benefit"] >= MIN_BENEFIT:
            count = count + 1
            o['benefitOk'] = True
        else:
            o['benefitOk'] = False

        if o["pe"] > 0 and o["pe"] <= MAX_PE:
            count = count + 1
            o['peOk'] = True
        else:
            o['peOk'] = False

        o['pb_15'] = o['roe_average_5'] / 15.0 * 100.0
        o['price_15'] = o['price'] / o['pb_no_corp'] * o['pb_15']

        if o['price_15'] > o['price']:
            o['score'] = 20
        else:
            o['score'] = 0

        o['pb_12'] = o['roe_average_5'] / 12.0 * 100.0
        o['price_12'] = o['price'] / o['pb_no_corp'] * o['pb_12']
        if o['price_12'] > o['price']:
            o['score'] += 20
        else:
            o['score'] += 0

        o['pb_10'] = o['roe_average_5'] / 10.0 * 100.0
        o['price_10'] = o['price'] / o['pb_no_corp'] * o['pb_10']
        if o['price_10'] > o['price']:
            o['score'] += 60
        else:
            o['score'] += 0

        o["count"] = count

    return stockList
    pass

# select stock from list , where code in map
def selectStocks(selected_map, list):
    result = []
    for l in list:
        if selected_map.has_key(l['code']):
            result.append(l)
            pass
        pass

    return result
    pass