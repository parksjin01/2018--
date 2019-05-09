# encoding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import string
import urllib2
import BeautifulSoup
import sqlite3

def is_ascii(keyword):
    for char in keyword:
        if char not in string.ascii_letters + "1234567890 -_+=!@#$%^&*()[]{}:;?":
            return False

    return True

def simple_word_dict(keyword):
    con = sqlite3.connect("dictionary3.db")
    cur = con.cursor()

    cur.execute("SELECT korean FROM engtohan WHERE english='%s'" % keyword)
    res = cur.fetchall()

    cur.execute("SELECT * FROM engtohan;")
    cur.fetchone()
    cur.fetchmany(2)
    cur.fetchall()

    con.commit()
    cur.close()
    con.close()
    return res

def wikipedia_dict(keyword):
    info = {}
    if is_ascii(keyword):
        print "https://en.wikipedia.org/wiki/" + keyword
        html = urllib2.urlopen("https://en.wikipedia.org/wiki/" + keyword)
    else:
        html = urllib2.urlopen("https://ko.wikipedia.org/wiki/" + keyword)
    soup = BeautifulSoup.BeautifulSoup(html)
    res = soup.findAll("div", attrs={"class": "mw-parser-output"})[0]
    tmp = res.findAll("p")
    tmp = tmp[:min(3, len(tmp))]
    text = ""
    for item in tmp:
        text += "<p>" + item.text + "</p>"
    info["text"] = text


    return info