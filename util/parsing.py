# -*- encoding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import os
import re
import nltk
from nltk.tree import Tree

from inference.conditional_filter import conditional_filter
from inference.gerund_filter import gerund_filter
from inference.to_infinitive_filter import infinitive_filter
from inference.relative_filter import relative_filter

os.environ['CLASSPATH'] += "/Users/Knight/Downloads/stanford-parser-full-2018-02-27"
print os.environ['CLASSPATH']
from nltk.parse import stanford
print nltk.__version__

option1 = re.compile(r"^[Ii]f ")
option2 = re.compile(r" [Ii]f ")

white_space_escape = re.compile(r"[ ]+")

if_conrpus = []
relative_clause_corpus = []
gerund_phrase_corpus = []
to_infinitive_corpus = []
passive_sentence_corpus = []
present_perfect_corpus = []
parser = stanford.StanfordParser()

def get_sentence(filename):
    print filename
    if os.path.isdir(filename):
        for tmp in os.listdir(filename):
            get_sentence(filename + "/" + tmp)
        return
    with open(filename, 'rt') as f:
        data = f.read().split(".")
    for line in data:
        line = line.replace("\n", " ").strip()
        # print "[" + repr(line) + "]"
        if "—" not in line and "_" not in line and "[" not in line and "]" not in line and "{" not in line and "}" not in line and ";" not in line and ":" not in line and "|" not in line and "(" not in line and ")" not in line and "’" not in line and "”" not in line and "“" not in line and "-" not in line:
            line = white_space_escape.sub(" ", line)
            if len(line.split(" ")) > 3 and len(line.split(" ")) < 20:
                if option1.match(line) != None or option2.match(line) != None:
                    # sentences = parser.raw_parse_sents((line, u''))
                    # for tmp1 in sentences:
                    #     for tmp2 in tmp1:
                    #         if conditional_filter(tmp2.productions()):
                    #             if_conrpus.append(line)
                    if_conrpus.append(line)

                if "that" in line or "That" in line or "which" in line or "Which" in line or "who" in line or "Who" in line or "whom" in line or "Whom" in line or "Whose" in line or "whose" in line or "what" in line or "What" in line or "those" in line or "Those" in line or "where" in line or "Where" in line or "when" in line or "When" in line or "why" in line or "Why" in line or "how" in line or "How" in line:
                    # if relative_filter(line):
                    relative_clause_corpus.append(line)
                if "ing" in line:
                    # if gerund_filter(line):
                    if "thing" not in line:
                        gerund_phrase_corpus.append(line)
                if "to" in line:
                    # if infinitive_filter(line):
                        to_infinitive_corpus.append(line)


get_sentence("/Users/Knight/Desktop/졸업작품/Corpus/masc_500k_texts")
print len(if_conrpus)
print len(relative_clause_corpus)
print len(gerund_phrase_corpus)
print len(to_infinitive_corpus)
print len(passive_sentence_corpus)
print len(present_perfect_corpus)
# with open("/Users/Knight/Desktop/졸업작품/Corpus/IF_corpus_auto_generated.txt", 'wt') as f:
#     f.write("\n".join(if_conrpus))

with open("/Users/Knight/Desktop/졸업작품/Corpus/Relative_Clause_auto_generated.txt", 'wt') as f:
    f.write("\n".join(relative_clause_corpus))

with open("/Users/Knight/Desktop/졸업작품/Corpus/Gerund_Phrase_auto_generated.txt", 'wt') as f:
    f.write("\n".join(gerund_phrase_corpus))

with open("/Users/Knight/Desktop/졸업작품/Corpus/To_Infinitive_auto_generated.txt", 'wt') as f:
    f.write("\n".join(to_infinitive_corpus))