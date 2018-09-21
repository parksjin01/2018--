# -*- encoding:utf-8 -*-

from nltk.parse import stanford
import os
from util.read_configuration import configuration
from inference.conditional_filter import conditional_filter

def precision_test(corpus_name):

    config = configuration()

    parser = stanford.StanfordParser()
    with open(config["corpus"] + "/" + corpus_name, "r") as f:
        data1 = f.read().split("\n")

    data2 = []
    for name in os.listdir(config["corpus"]):
        if name == corpus_name:
            continue
        with open(config["corpus"] + "/" + name) as f:
            data2 += f.read().split("\n")

    wrong = 0
    correct = 0

    for idx in range(len(data1)):
        sentences = parser.raw_parse_sents((data1[idx].strip(), u''))
        print "[", idx + 1, "/", len(data1), "]"
        for line in sentences:
            for sentence in line:
                if conditional_filter(sentence.productions()):
                    correct += 1

    for idx in range(len(data2[:1490])):
        sentences = parser.raw_parse_sents((data2[idx].strip(), u''))
        print "[", idx + 1, "/", len(data2[:149]), "]"
        for line in sentences:
            for sentence in line:
                if conditional_filter(sentence.productions()):
                    wrong += 1

    print str(int(float(correct)/(wrong + correct)*1000)/10.0)+"%"

precision_test("IF_corpus.txt")
print configuration()