#!/usr/bin/env python
# encoding=utf-8
from PyQt4.QtCore import *
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