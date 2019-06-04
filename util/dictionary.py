"""
    Dictionary
    ~~~~~~~~~~
"""

# encoding: utf-8 -*-

try:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

    import string
    import urllib2
    import BeautifulSoup
    import sqlite3
except:
    pass

def is_ascii(keyword):
    """
    Check special character such as !@#$ and number is included in word or not

    :param keyword: Word to search
    :return: True (Word contain only ascii character) / False (Special character or number is included in word)
    """
    for char in keyword:
        if char not in string.ascii_letters + "1234567890 -_+=!@#$%^&*()[]{}:;?":
            return False

    return True

def simple_word_dict(keyword):
    """
    Search the meaning of word in database

    :param keyword: Word to search
    :return: Meaning of word. If word is not in database, return null
    """

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
    """
    Search the meaning of word which can't find the meaning in database

    :param keyword: Word to search
    :return: Information related to word
    """

    info = {}
    if is_ascii(keyword):
        # print "https://en.wikipedia.org/wiki/" + keyword
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