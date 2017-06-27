import matplotlib.pyplot as plt

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def show_history_char(history_list, current_s):
    x = []
    histories = []
    price2s = []
    price5s = []

    for i, l in enumerate(history_list):
        x.append(i)
        histories.append(l.current)
        price2s.append(current_s.price2)
        price5s.append(current_s.price5)
        pass
    plt.plot(x, histories)
    plt.plot(x, price2s)
    plt.plot(x, price5s)
    plt.legend(['histories', 'price2s', 'price5s'])

    maxX = len(history_list)
    maxY = max([max(histories), max(price2s), max(price5s)]) * 1.05
    plt.axis([0, maxX, 0, maxY])

    plt.title(u'%s[%s]' % (current_s.name, current_s.code))
    plt.show()
    pass


from Tkinter import *

import S


class S_UI(object):
    s_list = []

    def __init__(self, s_list):
        self.s_list = s_list
        pass

    def on_selected(self, event):
        lb = event.widget
        index = lb.curselection()[0]
        s = self.s_list[index]
        print s

        histories = S.get_history(s.code)
        show_history_char(histories, s)
        pass

    def show(self):
        root = Tk()
        listb = Listbox(root, width=100, height=len(self.s_list) + 1)
        for i, s in enumerate(self.s_list):
            listb.insert(i, s.__str__())
            pass
        listb.bind("<Double-Button-1>", self.on_selected)
        listb.pack()

        root.mainloop()
        pass

    pass
