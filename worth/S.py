import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class BasicS(object):
    roe2010 = 0
    roe2011 = 0
    roe2012 = 0
    roe2013 = 0
    roe2014 = 0
    roe2015 = 0
    roe2016 = 0
    roe2017 = 0
    pure = 0
    name = ""
    code = ""

    def get_header(self):
        return "pure\troe2017\troe2016\troe2015\troe2014\troe2013\troe2012\troe2011\troe2010\t"
        pass

    def __str__(self):
        return "%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t" % (
            self.pure, self.roe2017, self.roe2016, self.roe2015, self.roe2014, self.roe2013, self.roe2012, self.roe2011,
            self.roe2010)
        pass


class S(BasicS):
    current = 0
    pbCurrent = 0
    price5 = 0
    pb5 = 0
    price2 = 0
    pb2 = 0

    roe5 = 0
    roe2 = 0

    def compute(self):
        self.roe5 = (self.roe2016 + self.roe2015 + self.roe2014 + self.roe2013 + self.roe2012) / 5
        self.roe2 = (self.roe2017 + self.roe2016) / 2
        self.pb5 = self.roe5 / 15
        self.pb2 = self.roe2 / 15
        self.price5 = self.pb5 * self.pure
        self.price2 = self.pb2 * self.pure
        pass

    def set_current(self, current):
        self.current = current
        self.pbCurrent = self.current / self.pure
        pass

    def get_header(self):
        return "name\tcode\tcurrent\tpbCurrent\tprice2\tpb2\tprice5\tpb5\troe2\troe5\t%s" % (
            super(S, self).get_header())
        pass

    def __str__(self):
        return "%s\t%s\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%s" % (
            self.name, self.code, self.current, self.pbCurrent, self.price2, self.pb2, self.price5, self.pb5, self.roe2,
            self.roe5,
            super(S, self).__str__())
        pass

import xlrd

def read_from_xls():
    wb = xlrd.open_workbook("s.xlsx")
    sheet = wb.sheet_by_index(0)
    nrow = sheet.nrows
    s_list = []
    for rowIndex in range(3, nrow):
        row_data = sheet.row(rowIndex)
        s = S()
        s.name = row_data[0].value
        s.code = row_data[1].value
        pureBase = 6
        s.pure = row_data[pureBase].value
        roeBase = 9
        s.roe2017 = 4 * row_data[roeBase].value

        roeBase += 1
        s.roe2016 = row_data[roeBase].value

        roeBase += 1
        s.roe2015 = row_data[roeBase].value

        roeBase += 1
        s.roe2014 = row_data[roeBase].value

        roeBase += 1
        s.roe2013 = row_data[roeBase].value

        roeBase += 1
        s.roe2012 = row_data[roeBase].value

        roeBase += 1
        s.roe2011 = row_data[roeBase].value

        roeBase += 1
        s.roe2010 = row_data[roeBase].value

        s.compute()
        s_list.append(s)
        pass

    return s_list
    pass


import tushare as ts


def request_price(codes):
    df = ts.get_realtime_quotes(codes)
    prices = []
    for item in df.iterrows():
        prices.append(float(item[1]['price']))
        pass
    return prices
    pass


def compute_with_lastest_price(list):
    codes = []
    for l in list:
        codes.append(l.code)
        pass
    prices = request_price(codes)
    for i, l in enumerate(list):
        l.set_current(prices[i])
        pass
    pass
