import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from PyQt4.QtWebKit import * 

class PdfPrinter(object):
    def __init__(self, urls_in, names_in):
        self.urls = urls_in
        self.names = urls_in
        self.index = 0

        
        self.ui = QWebView()

        self.ui.loadStarted.connect(self.onStart)
        self.ui.loadFinished.connect(self.onDone)
        self.ui.load(QUrl(self.urls[self.index]))
        # for url in urls:
        self.ui.showMaximized()
        self.printer = QPrinter()
        self.printer.setPageSize(QPrinter.A4)
        self.printer.setOutputFormat(QPrinter.PdfFormat)

    # def print_start(self):
    #     self.ui.load(QUrl(self.urls[self.index]))

    def onStart(self):
        print("Started...")

    def onDone(self, val):
        
        if self.index < len(self.urls):
            print('load finished, index is ', self.index, val)

            self.printer.setOutputFileName(self.names[self.index])
            self.ui.print_(self.printer)

            self.ui.load(QUrl(self.urls[self.index]))
            self.index = self.index + 1
            
app = QApplication(sys.argv)

urls = ['http://www.qaulau.com/books/PyQt4_Tutorial/events_and_signals.html', 'http://map.baidu.com/',
        'https://book.douban.com/subject/4244803/', 'https://www.quora.com/Whats-an-efficient-way-to-overcome-procrastination/answer/Oliver-Emberton']
names=['1.pdf','2.pdf','3.pdf','4.pdf']
a = PdfPrinter(urls, names)
# a.print_start()



sys.exit(app.exec_())


# def sayhello():
#         print ("hello world")
#         global t        #Notice: use global variable!
#         t = threading.Timer(5.0, sayhello)
#         t.start()

# t = threading.Timer(5.0, sayhello)
# t.start()

