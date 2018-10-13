# -*-encoding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import textract

def read_file(file_path):
    return textract.process(file_path)

def spanning(text):
    sentences = text.split("\n")
    span_sentences = []
    for line in sentences:
        sentence = ""
        for word in line.split(" "):
            if word not in '.,?/!@#$%^&*()_-+=':
                sentence += '<span class="word">' + word + ' </span>'
        span_sentences.append(sentence)
    return span_sentences

# print spanning("It should be clear that, given the structure of the measurements, we can create a beam that points in one direction, s, by setting a to the s-th row in the Fourier matrix.")