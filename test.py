# -*- encoding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import PyPDF2

with file("/Users/Knight/Desktop/2018 학부생RA/UbiG_MobiCom18-2.pdf", "rb") as f:
    pdf = PyPDF2.PdfFileReader(f)
    # print pdf.numPages
    # print pdf.documentInfo
    # print pdf.getNamedDestinations()
    print pdf.getPage(0).extractText()
    # print pdf.getPageLayout()
    # print pdf.getFields()
    # print dir(pdf)