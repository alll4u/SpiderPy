import sys 
from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from PyQt4.QtWebKit import * 
import time

class Printer(object):
    def __init__(self, url, name):
        # self.url = url
        # self.nam = name
        self.app = QApplication(sys.argv)
        self.web = QWebView()
        self.web.load(QUrl(url))
        self.printer = QPrinter()
        self.printer.setPageSize(QPrinter.A4)
        self.printer.setOutputFormat(QPrinter.PdfFormat)
        self.printer.setOutputFileName(name)
    def convertIt(self):
        self.web.print_(printer)
        print ("Pdf generated")
        QApplication.exit()
    def printpdf(self):
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), convertIt)
        sys.exit(app.exec_())


# app = QApplication(sys.argv)
# web = QWebView()
# web.load(QUrl("https://www.quora.com/What-are-some-social-norms-one-can-intentionally-break-to-get-a-response"))
# # web.load(QUrl('https://www.baidu.com'))
# printer = QPrinter()
# printer.setPageSize(QPrinter.A4)
# printer.setOutputFormat(QPrinter.PdfFormat)
# printer.setOutputFileName("fileOK.pdf")
# index = 0
# index2 = 0
# def convertIt():
#     global index
#     index = index + 1
#     print('index1:',index)
#     web.print_(printer)
#     print ("Pdf generated")
#     QApplication.exit()
# # QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)

# # def pdfprinter(url, name):
# #     global web
# #     global printer
# #     global index2
# #     index2 = index2 + 1
# #     print('index2:',index2)
# #     web.load(QUrl(url))
# #     printer.setOutputFileName(name)
# #     QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)

# print("1111111111111")

# print(12)
# web.load(QUrl('https://www.baidu.com/'))
# print(34)
# printer.setOutputFileName('fileOK3.pdf')
# # web.print_(printer)
# b = QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)


# print(12)
# web.load(QUrl('https://www.baidu.com/'))
# print(34)
# printer.setOutputFileName('fileOK4.pdf')
# b = QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)

# # web.load(QUrl('http://blog.csdn.net/dengjianqiang2011/article/details/9260435'))
# # printer.setOutputFileName('fileOK4.pdf')
# # b = QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)

# # web.load(QUrl('http://blog.csdn.net/raylee2007/article/details/48437661'))
# # printer.setOutputFileName('fileOK5.pdf')
# # b = QObject.connect(web, SIGNAL("loadFinished(bool)"), convertIt)








# # time.sleep(10)
# # print("2222222222222")
# # pdfprinter('http://blog.csdn.net/whiterbear/article/details/50232637','fileOK4.pdf')
# # time.sleep(10)
# # print("3333333333333")
# # pdfprinter('http://blog.csdn.net/raylee2007/article/details/48437661','fileOK5.pdf')





# sys.exit(app.exec_())