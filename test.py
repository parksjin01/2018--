# -*- encoding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from nltk.parse import stanford
from nltk.tree import Tree
import nltk
from inference.conditional_filter import conditional_filter
from inference.gerund_filter import gerund_filter
from inference.to_infinitive_filter import infinitive_filter
from inference.present_perfect_filter import present_perfect_filter
from inference.passive_filter import passive_filter
from inference.relative_filter import relative_filter
tmp = []

with open("/Users/Knight/Desktop/졸업작품/gerund.txt", "rt") as f:
    data = f.read().split("\n")
    corret = 0
    cnt = 0
    for original_sentences in data:
        parser = stanford.StanfordParser()
        original_sentences = "At a high level, the sys - tem operates as multiple randomized hash functions, which can be provably resolved to recover all signal directions even in the presence of multipath."
        sentences = parser.raw_parse_sents((original_sentences, u''))
        for line in sentences:
            for sentence in line:
                sentence.draw()
                cnt += 1
                # print sentence
                if (gerund_filter(sentence.productions()) == False):
                    corret += 1
                else:
                    # tmp.append(original_sentences)
                    sentence.draw()
                # print sentence.productions()
                # res = []
                # result = []
                # # grouping_phrase(sentence, "", res)
                # # grouping_clause(sentence.productions(), "SBAR", res)
                # # print res
                # for idx in range(len(res)):
                #     result.append(" ".join(res[idx]))
                # if "" in result:
                #     result.remove("")
                # print original_sentences, "\n===>", " / ".join(result), "\n\n"
                # print dir(sentence)
                # traverse_tree(sentence, 2 + level, res)
        print cnt, corret, len(data)
print corret
with open("tmp.txt", "w") as f:
    f.write("\n".join(tmp))

