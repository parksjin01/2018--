# -*- encoding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import fitz
import docxpy

def extract_image_pdf(filename):
    doc = fitz.open(filename)
    filename = filename.split("/")[-1]
    ret = []
    for i in range(len(doc)):
        print i
        for img in doc.getPageImageList(i):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            if pix.n < 5:       # this is GRAY or RGB
                pix.writePNG("image/extracted_image/" + filename + "-p%s-%s.png" % (i, xref))
                if i > 0:
                    ret.append("<img class=" + str(i) + " src=image/extracted_image/" + filename + "-p%s-%s.png" % (i, xref) + "/>")
                else:
                    ret.append("<img class=" + str(i) + " src=image/extracted_image/" + filename + "-p%s-%s.png" % (i, xref) + "/>")
            else:               # CMYK: convert to RGB first
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.writePNG("image/extracted_image/" + filename + "-p%s-%s.png" % (i, xref))
                pix1 = None
                if i > 0:
                    ret.append("<img class=" + str(i) + " src=image/extracted_image/" + filename + "-p%s-%s.png" % (i, xref) + "/>")
                else:
                    ret.append("<img class=" + str(i) + " src=image/extracted_image/" + filename + "-p%s-%s.png" % (i, xref) + "/>")
            pix = None
    return ret

def extract_image_docx(filename):
    print filename
    # extract text
    text = docxpy.process(filename)

    # extract text and write images in /tmp/img_dir
    text = docxpy.process(filename, "./")

def extract_image(filename):
    appendix = filename.split(".")[-1]
    if appendix == 'docx' or appendix == 'doc':
        return extract_image_docx(filename)
    elif appendix == 'pdf':
        return extract_image_pdf(filename)

print extract_image("/Users/Knight/Downloads/HW1/Afternoon/127186_951634_1539675_강창훈_chkang31.docx")