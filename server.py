# -*- encoding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
from flask import Flask
from flask import request, url_for
from flask import render_template, redirect, make_response
from nltk.tree import Tree
import pprint
import json
os.environ['CLASSPATH'] = os.environ['CLASSPATH']+"/Users/Knight/Downloads/stanford-parser-full-2018-02-27:"
import nltk
import random

corpus_name = "/Users/Knight/Desktop/졸업작품/Corpus/IF_corpus.txt"

print os.environ['CLASSPATH']
from nltk.parse import stanford
print nltk.__version__

app = Flask(__name__, static_url_path="/image", static_folder="image")

CLAUSE = 1

# def traverse_tree(tree, n, res):
#     if n == 0:
#         res.append([' '.join(tree.leaves()), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
#         return
#     for subtree in tree:
#         print dir(subtree)
#         print subtree
#         if type(subtree) == nltk.tree.Tree:
#             traverse_tree(subtree, n-1, res)
#         else:
#             print subtree
#             res.append(
#                 [subtree, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])

def parsing(original_sentences, level, res):
    parser = stanford.StanfordParser()
    sentences = parser.raw_parse_sents((original_sentences, u''))
    for line in sentences:
        for sentence in line:
            # print sentence.productions()
            res = []
            result = []
            grouping_phrase(sentence, "", res)
            # grouping_clause(sentence.productions(), "SBAR", res)
            print res
            for idx in range(len(res)):
                result.append(" ".join(res[idx]))
            if "" in result:
                result.remove("")
            print original_sentences, "\n===>", " / ".join(result), "\n\n"
            sentence.draw()
            # print dir(sentence)
            # traverse_tree(sentence, 2 + level, res)

# @app.route("/", methods=["GET", "POST"])
# def home():
#     if request.method == "GET":
#         return render_template("nltk_home.html")
#     elif request.method == "POST":
#         sentence = request.form['sentence']
#         level = request.form['level']
#         res = []
#         parsing(sentence, int(level), res)
#         return render_template("nltk_home.html", res=res)
#
# @app.route("/file", methods=["GET"])
# def read_file():
#     return render_template("nltk_file.html")
#
# @app.route("/ajax/sentence")
# def json_response():
#     res = []
#     parsing(request.args.get("sentence"), 0, res)
#     return json.dumps({'success': True, 'status':'OK', 'sentence':res, 'id':request.args.get("id")}), 200, {'ContentType': 'application/json'}
#
# if __name__ == '__main__':
#     app.run()
res = []
parsing("After shaping the entire course of modern art, Cezanne died thinking that he was a failure.", 0, res)
parsing("His pleasure, listening to the music of The Beatles at full volume, caused quite a stirring among his neighbors at 3:00 a.m.", 0, res)
parsing("His filming of The Magnificent Seven was, in my opinion, Kurosawa’s greatest achievement as a film director.", 0, res)
parsing("After having been reprimanded for smoking in the hall, the thoughtless student started chewing tobacco.", 0, res)
parsing("Subscribing to the Boca Raton News was the first step in moving to that distant tropical area.", 0, res)
parsing("Sneezing for 2000 days straight is not a desirable record to set.", 0, res)
parsing("Upon discovering that she had been accepted by Coliseum College, Melissa let her hair grow very long and began to wear leotards.", 0, res)
parsing("The signing of the Declaration of Independence was one of the single most decisive acts in Western Civilization.", 0, res)
parsing("Eating strawberries without washing them might make you sick.", 0, res)
parsing("After having lost their twelfth straight game, the Erstwhiles sat glumly in their locker room.", 0, res)
parsing("Being seen in the Casbah with Pepe Le Moko proved to be a most unfortunate incident the young diplomat’s career.", 0, res)
# parsing("This is the area which they are fighting for.", 0, res)
# parsing("What would have happened if I hadn't checked the room?", 0, res)
# parsing("If I were rich, I could buy the big house", 0, res)
# parsing("If he were poor, he could not have donated 10 million dollars to the Salvation Army last month.", 0, res)
# parsing("If he or she were an American, he or she would not use that expression.", 0, res)
# parsing("If exclusive bus lanes hadn't been made, there would have been a huge traffic jam every morning.", 0, res)
# parsing("What is worse is that some of us don't even know that Christmas is the celebration of the birth of Christ.", 0, res)
# parsing("A person whose job is to handle human relations can describe their job performances clearly.", 0, res)
# parsing("What really impressed me about her was work, as I think is something some of us have lost sight of.", 0, res)
# parsing("What is worse is that some of us don't even know that Christmas is the celebration of the birth of Christ.", 0, res)
# precision_test()
