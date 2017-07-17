import threading
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from PyQt4.QtWebKit import * 



index = 0
def onDone(val):
    global index
    
    print('load finished,index is', index, val)

    printer.setOutputFileName(names[index])
    ui.print_(printer)

    if index+1 < len(urls):
        index = index + 1
        ui.load(QUrl(urls[index]))
    else:
        return
def onStart():
    print("Started...")


urls = ['http://www.qaulau.com/books/PyQt4_Tutorial/events_and_signals.html', 'http://map.baidu.com/',
        'https://book.douban.com/subject/4244803/', 'https://www.quora.com/Whats-an-efficient-way-to-overcome-procrastination/answer/Oliver-Emberton']
names=['1.pdf','2.pdf','3.pdf','4.pdf']

app = QApplication(sys.argv)
ui = QWebView()
ui.loadStarted.connect(onStart)
ui.loadFinished.connect(onDone)

# for url in urls:
ui.load(QUrl(urls[index]))
ui.showMaximized()
printer = QPrinter()
printer.setPageSize(QPrinter.A4)
printer.setOutputFormat(QPrinter.PdfFormat)



sys.exit(app.exec_())


# def sayhello():
#         print ("hello world")
#         global t        #Notice: use global variable!
#         t = threading.Timer(5.0, sayhello)
#         t.start()

# t = threading.Timer(5.0, sayhello)
# t.start()
