# -*- encoding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import pprint
import json
import nltk
import random
import sqlite3
import time

from flask import Flask
from flask import request, url_for, session
from flask import render_template, redirect, make_response
from nltk.tree import Tree
from werkzeug import secure_filename

from grouping.grouping_phrase import grouping_phrase
from grouping.grouping_clause import grouping_clause
from util.read_configuration import configuration
from util.read_text import read_file
from util.read_text import pdf2html
from util.read_text import get_sentence
from util.extract_image import extract_image
from util.dictionary import wikipedia_dict, simple_word_dict
from util.gaze_analyze import analyze
from inference.conditional_filter import conditional_filter
from inference.gerund_filter import gerund_filter
from inference.to_infinitive_filter import infinitive_filter
from inference.relative_filter import relative_filter
from nltk.parse.corenlp import CoreNLPParser

os.environ['CLASSPATH'] += configuration()["parser"] + ":"

path_to_jar = '‎/Users/Knight/Downloads/stanford-parser-full-2018-02-27/stanford-parser.jar'
path_to_models_jar = '/Users/Knight/Downloads/stanford-parser-full-2018-02-27/stanford-parser-3.9.1-models.jar'

os.environ["STANFORD_PARSER"] = path_to_jar
os.environ["STANFORD_MODELS"] = path_to_models_jar
os.environ["CLASSPATH"] += "/Users/Knight/Downloads/stanford-corenlp-full-2018-10-05/"

stanford_parser = CoreNLPParser("http://localhost:9000")

print os.environ['CLASSPATH']
from nltk.parse import stanford
print nltk.__version__

upload_folder = configuration()["upload_folder"]
allowed_extensions = configuration()["allowed_extensions"]
app = Flask(__name__, static_url_path="/image", static_folder="image")
app.config['UPLOAD_FOLDER'] = upload_folder
app.secret_key = "graduationProject"
DOCS = {}

CLAUSE = 1

def file_check(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in allowed_extensions


def parsing(original_sentences, level, res):
    parser = stanford.StanfordParser()
    sentences = parser.raw_parse_sents((original_sentences, u''))
    for line in sentences:
        for sentence in line:
            print sentence
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

@app.route("/ajax/word")
def word_dict():
    # print json.dumps(wikipedia_dict(request.args.get("word")))
    try:
        w = request.args.get("word")
        w = w.lower().replace(";", "").replace("'", "").replace('"', "").replace(".", "").replace(",", "")
        res = simple_word_dict(w)
        # if res == []:
        #     res = wikipedia_dict(request.args.get("word"))
        return json.dumps(res).encode('utf-8')
    except:
        return json.dumps({"text":"No data"})

@app.route("/ajax/gaze_pattern", methods=["GET", "POST"])
def gaze_pattern():
    word_search_threshold = 2500
    session["word"].append(request.form.get("word"))
    session["duration"].append(request.form.get("duration"))
    session["start"].append(request.form.get("start"))
    session["end"].append(request.form.get("end"))
    session["class"].append(request.form.get("class").split(" ")[-1])
    with open(session["filename"]+".json", 'wt') as f:
        f.write(json.dumps({"word":session["word"], "duration":session["duration"], "start":session["start"], "end":session["end"], "class": session["class"]}))
    # print session["sentences"]

    session["word"], session["duration"], session["start"], session["end"], session["class"] = analyze(session["word"], session["duration"], session["start"], session["end"], session["class"], DOCS[request.remote_addr])
    if len(session["duration"]) > 0:
        if int(session["duration"][-1]) > word_search_threshold:
            conn = sqlite3.connect("ReadHelper.db")
            c = conn.cursor()
            print type(session["userid"]), session["word"][-1], time.time()
            sql = "insert into hardWord (userId, word, time) values (?, ?, ?)"
            c.execute(sql, ( session["userid"], session["word"][-1], time.time(), ))
            conn.commit()
            conn.close()
            return '{"result":"true", "type":"word", "grammar":"", "word":"%s"}' %(session["word"][-1])
        else:
            return '{"result": "false"}'
    else:
        grammar = ""
        current_time = time.time()
        conn = sqlite3.connect("ReadHelper.db")
        c = conn.cursor()
        sql = "insert into hardGrammar (userId, grammar, time) values (?, ?, ?)"

        idx = int(request.form.get("class").split(" ")[-1])
        sentence = get_sentence(idx, DOCS[request.remote_addr])

        # print idx, DOCS[request.remote_addr], sentence
        # parser = stanford.StanfordParser()
        # parsed_sentence = parser.raw_parse_sents((sentence, u''))
        s = stanford_parser.parse((sentence, u"")).next()
        s_p = s.productions()

        print s.productions()

        inference = conditional_filter(s_p)
        if inference == True:
            c.execute(sql, (session["userid"], "conditional", time.time()))
            grammar += "conditional "

        inference = gerund_filter(s_p)
        if inference == True:
            c.execute(sql, (session["userid"], "gerund", time.time()))
            grammar += "greund "

        inference = infinitive_filter(s_p)
        if inference == True:
            c.execute(sql, (session["userid"], "infinitive", time.time()))
            grammar += "infinitive "

        inference = relative_filter(s_p)
        if inference == True:
            c.execute(sql, (session["userid"], "relative", time.time()))
            grammar += "relative "

        grammar.strip(" ")
        conn.commit()
        conn.close()

        g_clause = []
        g_phrase = []
        # parser = stanford.StanfordParser()
        # sentences = parser.raw_parse_sents((sentence, u''))
        # for line in sentences:
        #     for sentence in line:
        #         # print sentence.productions()
        #         result = []
        grouping_phrase(s, "", g_phrase)
        grouping_clause(s_p, "SBAR", g_clause)
        clause = []
        phrase = []
        for group in g_clause:
            clause.append(" ".join(group))
        for group in g_phrase:
            phrase.append(" ".join(group))
        return '{"result": "true", "type":"sentence", "grammar":"%s", "grouping":"CLAUSE: %sPHRASE: %s"}' %(grammar, "/".join(clause), "/".join(phrase))

@app.route("/", methods=["GET", "POST"])
def upload_file():
    login = "userid" in session
    hardWord = {}
    hardGrammar = {}
    if request.method == 'POST':
        session["word"] = []
        session["duration"] = []
        session["start"] = []
        session["end"] = []
        session["class"] = []

        file = request.files['file']
        if file and file_check(file.filename):
            filename = secure_filename(file.filename)
            session["filename"] = filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            content, pages, DOCS[request.remote_addr] = pdf2html(os.path.join(app.config['UPLOAD_FOLDER'], filename)[2:])
            return render_template("load_on_server.html", res={'login': login, 'header': content['header'], 'body':content['body'], 'pages':pages, "login": login})
    if login:
        conn = sqlite3.connect("ReadHelper.db")
        c = conn.cursor()
        search_word_query = "select * from hardWord where userid=?"
        search_grammar_query = "select * from hardGrammar where userid=?"
        c.execute(search_word_query, (session["userid"],))
        result = c.fetchall()
        for column in result:
            try:
                hardWord[column[1]] += 1
            except:
                hardWord[column[1]] = 1

        c.execute(search_grammar_query, (session["userid"],))
        result = c.fetchall()
        for column in result:
            try:
                hardGrammar[column[1]] += 1
            except:
                hardGrammar[column[1]] = 1

        hardWord = sorted(hardWord.iteritems(), key=lambda (k, v): (v, k))
        hardGrammar = sorted(hardGrammar.iteritems(), key=lambda  (k, v): (v, k))

        hardWord.reverse()
        hardGrammar.reverse()

        hardWord = [k[0] for k in hardWord[:5]]
        hardGrammar = [k[0] for k in hardGrammar[:5]]

        print hardWord
        print hardGrammar

    return render_template("load_on_server.html", res={"login": login, "word": hardWord, "grammar": hardGrammar})

@app.route("/word", methods=["GET"])
def word():
    return render_template("word_search.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        conn = sqlite3.connect("ReadHelper.db")
        c = conn.cursor()
        sql = "select * from userInfo where userId=? and userPw=?"
        userid = request.form.get("username")
        userpw = request.form.get("password")
        c.execute(sql, (userid, userpw))
        result = c.fetchall()
        conn.close()
        if len(result) > 0:
            print "Login successed"
            session["userid"] = userid
            pass
        return redirect("/")
    return render_template("Login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        conn = sqlite3.connect("ReadHelper.db")
        c = conn.cursor()
        sql = "insert into userInfo (userId, email, userPw) values (?, ?, ?)"
        userid = request.form.get("username")
        email = request.form.get("email")
        userpw = request.form.get("password")
        userrepw = request.form.get("cpassword")
        print userpw, userrepw
        if userpw == userrepw:
            c.execute(sql, (userid, email, userpw))
            conn.commit()
        conn.close()
        return redirect("/")
    return render_template("Register.html")

@app.route("/logout")
def logout():
    session.pop("userid", None)
    return redirect("/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    # parsing("I have a dream", "", "")
