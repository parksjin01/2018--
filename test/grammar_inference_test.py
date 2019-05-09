# -*- encoding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from nltk.parse import stanford
import os
import itertools

from util.read_configuration import configuration
from inference.conditional_filter import conditional_filter
from inference.gerund_filter import gerund_filter
from inference.to_infinitive_filter import infinitive_filter
from inference.present_perfect_filter import present_perfect_filter
from inference.passive_filter import passive_filter
from inference.relative_filter import relative_filter

def precision_test(grammar="conditional", precision=True):

    config = {"corpus": "/Users/Knight/Desktop/졸업작품/Corpus"}
    os.environ['CLASSPATH'] = "/Users/Knight/Downloads/stanford-parser-full-2018-02-27"

    parser = stanford.StanfordParser()
    true = []
    whole_sentence = []

    tp = 0
    tn = 0
    fp = 0
    fp_sentence = []
    fn = 0

    for name in os.listdir(config["corpus"]):
        if os.path.isfile(config["corpus"] + "/" + name):
            with open(config["corpus"] + "/" + name) as f:
                if grammar == "conditional" and "IF" in name:
                    true.append(f.read().split("\n"))
                    whole_sentence.append(true[-1])
                elif grammar == "gerund" and "Gerund" in name:
                    true.append(f.read().split("\n"))
                    whole_sentence.append(true[-1])
                elif grammar == "infinitive" and "Infinitive" in name:
                    true.append(f.read().split("\n"))
                    whole_sentence.append(true[-1])
                elif grammar == "relative" and "Relative" in name:
                    true.append(f.read().split("\n"))
                    whole_sentence.append(true[-1])
                whole_sentence.append(f.read().split("\n"))

    true = list(itertools.chain(*true))

    for idx1, sentence_list in enumerate(whole_sentence):
        if len(sentence_list) > 1000:
            continue
        for idx2, sentence in enumerate(sentence_list):
            print idx1, '/', idx2, len(sentence_list)
            try:
                parsed_sentence = parser.raw_parse_sents((sentence, u''))
                for line in parsed_sentence:
                    for s in line:
                        print s.productions
                        if grammar == "conditional":
                            inference = conditional_filter(s.productions())
                        elif grammar == "gerund":
                            inference = gerund_filter(s.productions())
                        elif grammar == "relative":
                            inference = relative_filter(s.productions())
                        elif grammar == "infinitive":
                            inference = infinitive_filter(s.productions())
                        if inference == True and sentence in true:
                            tp += 1
                        elif inference == True:
                            fp += 1
                            fp_sentence.append(sentence)
                        elif inference == False and sentence not in true:
                            tn += 1
                        elif inference == False:
                            fn += 1
                        print tp, fp, tn, fn
            except Exception, e:
                print e
                print sentence
                pass
    with open("/Users/Knight/Desktop/졸업작품/"+grammar+".txt", 'wt') as f:
        f.write('\n'.join(fp_sentence))


    return 'Precision:',float(tp)/(tp+fp), '%', 'Recall:',float(tp)/(tp+fn), '%'



    # correct = 0


print precision_test("gerund")
# precision_test("Passive_Sentence_Corpus.txt", "passive")
# precision_test("Relative_Clause_corpus.txt", "relative")
# precision_test("Present_Perfect_corpus.txt", "present_perfect")
# precision_test("Gerund_Phrase_corpus.txt", "gerund")
# precision_test("To_Infinitive_corpus.txt", "infinitive")
# print configuration()