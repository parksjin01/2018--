# -*- encoding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import pprint
import json
import nltk
import random

from flask import Flask
from flask import request, url_for
from flask import render_template, redirect, make_response
from nltk.tree import Tree
from werkzeug import secure_filename

from grouping.grouping_phrase import grouping_phrase
from grouping.grouping_clause import grouping_clause
from util.read_configuration import configuration
from util.read_text import read_file, spanning
from util.dictionary import wikipedia_dict

os.environ['CLASSPATH'] += configuration()["parser"] + ":"
print os.environ['CLASSPATH']
from nltk.parse import stanford
print nltk.__version__

upload_folder = configuration()["upload_folder"]
allowed_extensions = configuration()["allowed_extensions"]
app = Flask(__name__, static_url_path="/image", static_folder="image")
app.config['UPLOAD_FOLDER'] = upload_folder

CLAUSE = 1

def file_check(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in allowed_extensions

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
            # grouping_phrase(sentence, "", res)
            grouping_clause(sentence.productions(), "SBAR", res)
            print res
            for idx in range(len(res)):
                result.append(" ".join(res[idx]))
            if "" in result:
                result.remove("")
            print original_sentences, "\n===>", " / ".join(result), "\n\n"
            # sentence.draw()
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

@app.route("/ajax/word")
def word_dict():
    # print json.dumps(wikipedia_dict(request.args.get("word")))
    return json.dumps(wikipedia_dict(request.args.get("word")))

@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file_check(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            content = '</br>'.join(spanning(read_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))))
            return render_template("load_on_server.html", res={'content':content})
    return render_template("load_on_server.html", res={})

@app.route("/word", methods=["GET"])
def word():
    return render_template("word_search.html")

if __name__ == '__main__':
    app.run(debug=True)
