import threading
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from PyQt4.QtWebKit import * 

def read_url_from_file(file_name):
    f = open(file_name,'r')
    length = len(f.readlines())
    f.close()

    f = open(file_name,'r')
    result = list()
    for i in range(int(length/2)):
        name = f.readline()
        link = f.readline()
        name = ''.join(name).strip('\n')
        link = ''.join(link).strip('\n')
        result.append({'name':name, 'link':link})
    print('readfileOK')
    print(result)
    f.close()
    return result

def onDone(val):
    global index
    
    print('load finished,index is', index, val)

    printer.setOutputFileName(url_name[index]['name']+'.pdf')
    ui.print_(printer)

    if index+1 < len(url_name):
        index = index + 1
        ui.load(QUrl(url_name[index]['link']))

def onStart():
    print("Started...")

index = 0
url_name = read_url_from_file('movies3')

urls = ['http://www.qaulau.com/books/PyQt4_Tutorial/events_and_signals.html', 'http://map.baidu.com/',
        'https://book.douban.com/subject/4244803/', 'https://www.quora.com/Whats-an-efficient-way-to-overcome-procrastination/answer/Oliver-Emberton']
names=['1.pdf','2.pdf','3.pdf','4.pdf']

app = QApplication(sys.argv)
ui = QWebView()
ui.loadStarted.connect(onStart)
ui.loadFinished.connect(onDone)

# for url in urls:
ui.load(QUrl(url_name[index]['link']))
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
