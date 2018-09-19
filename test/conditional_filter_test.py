import inference.conditional_filter

def precision_test():
    parser = stanford.StanfordParser()
    with open(corpus_name, "r") as f:
        data1 = f.read().split("\n")

    with open("/Users/Knight/Desktop/졸업작품/Corpus/Relative_Clause_corpus.txt", "r") as f:
        data2 = f.read().split("\n")
    with open("/Users/Knight/Desktop/졸업작품/Corpus/Relative_Clause_corpus.txt", "r") as f:
        data2 += f.read().split("\n")
    with open("/Users/Knight/Desktop/졸업작품/Corpus/Relative_Clause_corpus.txt", "r") as f:
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