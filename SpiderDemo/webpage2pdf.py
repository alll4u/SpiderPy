#!/usr/bin/env python
# encoding=utf-8

import sys
from PyQt4 import QtGui
# print(PyQt4)
 
app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('PyQt')
widget.show()
sys.exit(app.exec_())


import pdfkit
print('hello')
pdfkit.from_url('How to convert webpage into PDF by using Python - Stack Overflow.html', 'out.pdf')
print("OK")


# from xhtml2pdf import pisa
# import urllib.request
# url=urllib.request.urlopen('http://sheldonbrown.com/web_sample1.html')
# srchtml=url.read()
# pisa.showLogging()
# convertHtmlToPdf(srchtml, outputFilename)