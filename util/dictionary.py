# encoding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import string
import urllib2
import BeautifulSoup

def is_ascii(keyword):
    for char in keyword:
        if char not in string.ascii_letters + "1234567890 -_+=!@#$%^&*()[]{}:;?":
            return False

    return True

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
        text += item.text + "\n"
    info["text"] = text


    return info