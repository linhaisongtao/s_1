import matplotlib.pyplot as plt

import sys
import datetime
import threading

reload(sys)
sys.setdefaultencoding('utf-8')


class ChartData(object):

    def __init__(self):
        self.x = []
        self.y = []
        self.name = ""
        pass
    pass


class ChartManager(object):
    def __init__(self, title, datas):
        self.datas = datas
        self.title = title
        pass

    def show(self):
        names = []
        maxXs = []
        maxYs = []
        for d in self.datas:
            plt.plot(d.x, d.y)
            names.append(d.name)
            maxXs.append(max(d.x))
            maxYs.append(max(d.y))
            pass
        plt.axis([0, max(maxXs) + 1, 0, max(maxYs) * 1.05])
        plt.legend(names)
        plt.title(self.title)
        plt.show()
        pass

    pass


def show_history_chart(history_list, current_s):
    print "show_history_char", len(history_list)
    print "show_history_char", current_s
    x = []
    histories = []
    price2s = []
    price5s = []
    pures = []

    date = history_list[len(history_list) - 1].date
    for i, l in enumerate(history_list):
        x.append(i)
        histories.append(l.current)
        price2s.append(current_s.price2)
        price5s.append(current_s.price5)
        pures.append(current_s.pure)
        pass
    plt.plot(x, histories)
    plt.plot(x, price2s)
    plt.plot(x, price5s)
    plt.plot(x, pures)
    plt.legend(['histories', 'price2s', 'price5s', 'pure'])

    maxX = len(history_list)
    maxY = max([max(histories), max(price2s), max(price5s), max(pures)]) * 1.05
    plt.axis([0, maxX, 0, maxY])

    plt.title(u'%s[%s] %s' % (current_s.name, current_s.code, date))
    print 'show history chart!'
    plt.show()
    pass


from Tkinter import *

import S

import pb


class S_UI(object):
    s_list = []

    def __init__(self, s_list):
        self.s_list = s_list
        pass

    def on_selected(self, event):
        lb = event.widget
        index = lb.curselection()[0]
        if (index < 0 or index >= len(self.s_list)):
            return
            pass
        s = self.s_list[index]
        print s

        pbs = pb.request_pbs(s.code)
        chart_data = ChartData()
        chart_data.name = 'pb'
        for i, p in enumerate(pbs.pb_list):
            chart_data.x.append(i)
            chart_data.y.append(p.pb)
            pass

        chart_data1 = ChartData()
        chart_data1.name = "pb5"
        for i, p in enumerate(chart_data.x):
            chart_data1.x.append(i)
            chart_data1.y.append(s.pb5)
            pass

        chart_data2 = ChartData()
        chart_data2.name = "pb2"
        for i, p in enumerate(chart_data.x):
            chart_data2.x.append(i)
            chart_data2.y.append(s.pb2)
            pass

        chart_data3 = ChartData()
        chart_data3.name = "1"
        for i, p in enumerate(chart_data.x):
            chart_data3.x.append(i)
            chart_data3.y.append(1)
            pass

        ChartManager("%s(%s)_%s"%(s.name, s.code, s.date),[chart_data, chart_data1, chart_data2, chart_data3]).show()
        pass

    def show(self):
        root = Tk()
        listb = Listbox(root, width=100, height=len(self.s_list) + 1)
        for i, s in enumerate(self.s_list):
            listb.insert(i, s.__str__())
            pass
        listb.bind("<Double-Button-1>", self.on_selected)
        listb.pack()
        root.title(datetime.datetime.now().strftime("%Y-%m-%d"))
        root.mainloop()
        pass

    pass
