# -*- encoding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from nltk.parse.stanford import StanfordDependencyParser
from nltk.parse.stanford import StanfordParser
from nltk.parse.stanford import StanfordNeuralDependencyParser
from nltk.parse.corenlp import CoreNLPDependencyParser
from nltk.parse.corenlp import CoreNLPParser
import time
import os

path_to_jar = '‎/Users/Knight/Downloads/stanford-parser-full-2018-02-27/stanford-parser.jar'
path_to_models_jar = '/Users/Knight/Downloads/stanford-parser-full-2018-02-27/stanford-parser-3.9.1-models.jar'

os.environ["STANFORD_PARSER"] = path_to_jar
os.environ["STANFORD_MODELS"] = path_to_models_jar
os.environ["CLASSPATH"] += "/Users/Knight/Downloads/stanford-corenlp-full-2018-10-05/"

dependency_parser = StanfordDependencyParser(path_to_models_jar=path_to_models_jar)
dependency_parser = StanfordNeuralDependencyParser()
dependency_parser = CoreNLPDependencyParser("http://localhost:9000")
stanford_parser = CoreNLPParser("http://localhost:9000")

# result = dependency_parser.raw_parse_sents(('The person who made the mess needs to clean it.', u""))
# parses = dependency_parser.parse('The person who made the mess needs to clean it.'.split())
s = time.time()
parses = stanford_parser.parse(('The person who made the mess needs to clean it.', u""))
print parses.next().productions()
print time.time() - s,s
# print list(dep.next().triples())
