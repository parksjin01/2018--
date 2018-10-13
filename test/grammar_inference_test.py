# -*- encoding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from nltk.parse import stanford
import os
from util.read_configuration import configuration
from inference.conditional_filter import conditional_filter
from inference.gerund_filter import gerund_filter
from inference.to_infinitive_filter import infinitive_filter
from inference.present_perfect_filter import present_perfect_filter
from inference.passive_filter import passive_filter
from inference.relative_filter import relative_filter

def precision_test(corpus_name, grammar="conditional", precision=False):

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
                if grammar == "conditional":
                    if conditional_filter(sentence.productions()):
                        correct += 1
                elif grammar == "gerund":
                    if gerund_filter(sentence.productions()):
                        correct += 1
                elif grammar == "infinitive":
                    if infinitive_filter(sentence.productions()):
                        correct += 1
                elif grammar == "present_perfect":
                    if present_perfect_filter(sentence.productions()):
                        correct += 1
                elif grammar == "passive":
                    if passive_filter(sentence.productions()):
                        correct += 1
                elif grammar == "relative":
                    if relative_filter(sentence.productions()):
                        correct += 1

    if precision:
        for idx in range(len(data2[:1490])):
            sentences = parser.raw_parse_sents((data2[idx].strip(), u''))
            print "[", idx + 1, "/", len(data2[:149]), "]"
            for line in sentences:
                for sentence in line:
                    if grammar == "conditional":
                        if conditional_filter(sentence.productions()):
                            wrong += 1
                    elif grammar == "gerund":
                        if gerund_filter(sentence.productions()):
                            wrong += 1
                    elif grammar == "infinitive":
                        if infinitive_filter(sentence.productions()):
                            wrong += 1
                    elif grammar == "present_perfect":
                        if present_perfect_filter(sentence.productions()):
                            correct += 1
                    elif grammar == "passive":
                        if passive_filter(sentence.productions()):
                            correct += 1
                    elif grammar == "relative":
                        if relative_filter(sentence.productions()):
                            correct += 1

    print str(int(float(correct)/len(data1)*1000)/10.0) + "%"
    if precision:
        print str(int(float(correct)/(wrong + correct)*1000)/10.0) + "%"

# precision_test("Passive_Sentence_Corpus.txt", "passive")
# precision_test("Relative_Clause_corpus.txt", "relative")
# precision_test("Present_Perfect_corpus.txt", "present_perfect")
# precision_test("Gerund_Phrase_corpus.txt", "gerund")
precision_test("To_Infinitive_corpus.txt", "infinitive")
# print configuration()