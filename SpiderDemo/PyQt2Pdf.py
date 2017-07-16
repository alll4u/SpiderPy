import sys 
from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from PyQt4.QtWebKit import * 


# class Printer(object):
#     def __init__(self, url, name):
#         self.url = url
#         self.nam = name
#         self.app = QApplication(sys.argv)
#         self.web = QWebView()
#         self.web.load(QUrl(url))
#         self.printer = QPrinter()
#         self.printer.setPageSize(QPrinter.A4)
#         self.printer.setOutputFormat(QPrinter.PdfFormat)
#         self.printer.setOutputFileName(name)
#     def convertIt(self):
#         self.web.print_(printer)
#         print ("Pdf generated")
#         QApplication.exit()
#     def printpdf(self):
#         QObject.connect(self.web, SIGNAL("loadFinished(bool)"), convertIt)
#         sys.exit(app.exec_())


import sys 
from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from PyQt4.QtWebKit import * 

app = QApplication(sys.argv)
web = QWebView()
web.load(QUrl("https://www.quora.com/What-are-some-social-norms-one-can-intentionally-break-to-get-a-response"))
# web.load(QUrl('https://www.baidu.com'))
printer = QPrinter()
printer.setPageSize(QPrinter.A4)
printer.setOutputFormat(QPrinter.PdfFormat)
printer.setOutputFileName("fileOK.pdf")
index = 0
index2 = 0
def convertIt():
    global index
    index = index + 1
    print('index1:',index)
    web.print_(printer)
    print ("Pdf generated")
    QApplication.exit()
# QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)

def pdfprinter(url, name):
    global web
    global printer
    global index2
    index2 = index2 + 1
    print('index2:',index)
    web.load(QUrl(url))
    printer.setOutputFileName(name)
    QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)

pdfprinter('http://www.jb51.net/article/108952.htm','fileOK3.pdf')
pdfprinter('http://blog.csdn.net/raylee2007/article/details/48437661','fileOK4.pdf')
pdfprinter('http://blog.csdn.net/raylee2007/article/details/48437661','fileOK5.pdf')
pdfprinter('http://blog.csdn.net/raylee2007/article/details/48437661','fileOK6.pdf')
sys.exit(app.exec_())