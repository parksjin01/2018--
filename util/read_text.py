# -*-encoding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import textract
import PyPDF2
import shutil
import subprocess
import BeautifulSoup
import io
import re

def is_ascii(word):
    for char in word:
        if ord(char) < 0x20 or ord(char) > 0x7e:
            return False
    return True

def mapping(text):
    regex = "(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"
    regex = re.compile(regex)
    text = regex.split(text)
    return text


def read_file(file_path):
    print file_path
    res = ""
    # try:
    reader = PyPDF2.PdfFileReader(open(file_path, "rb"))
    for num in range(reader.getNumPages())[:1]:
        print reader.getPage(num).extractText()
            # writer = PyPDF2.PdfFileWriter()
            # writer.addPage(reader.getPage(num))
            # with open("./upload/tmp.pdf", "wb") as f:
            #     writer.write(f)
            # if num > 0:
            #     res += '<div id="page_' + str(num) + '" hidden>' + spaning(textract.process("./upload/tmp.pdf")) + '</div>'
            # else:
            #     res += '<div id="page_' + str(num) + '">' + spaning(textract.process("./upload/tmp.pdf")) + '</div>'
        # print type(res)
        # return res, reader.getNumPages()
    # except:
    #     res = '<div id="page_' + str(0) + '">' + spaning(textract.process('./' + file_path)) + '</div>'
    #     return res, 0

def words2sentence(sentence):
    res = {}
    regex = "(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"
    regex = re.compile(regex)
    pivot = 0

    tmp_sentence = regex.split(' '.join(sentence))
    for s in tmp_sentence:
        res[pivot + len(s.split(" "))] = s
        pivot += len(s.split(" "))

    return res

def get_sentence(idx, sentence_dict):
    key = sorted(sentence_dict.keys())
    for i in key:
        if i > idx:
            return sentence_dict[i]

def spaning(html, word_idx, sentence):
    # sentence_idx = -1
    html = str(html)
    # print html
    child = []
    soup = BeautifulSoup.BeautifulSoup(html, fromEncoding='utf-8').find("div")

    plain_text = str(soup)
    plain_text = plain_text.split(">", 1)[1][:-6]
    words = []
    span_node = soup.findChildren("span", recursive=False)
    # print span_node
    for pivot in span_node:
        try:
            a, plain_text = plain_text.split(str(pivot), 1)
            words.append(a.strip().split())
        except:
            print "[ERROR]:", plain_text, pivot
    words.append(plain_text.strip().split())
    # words_to_sentence, text_idx = words2sentence(words, pdf_text, text_idx)
    # print words
    # print words_to_sentence, text_idx
    # print words

    for idx in range(len(span_node)):
        if words[idx] != []:
            for words_idx, tmp in enumerate(words[idx][:-1]):
                # if tmp.encode("utf-8") in pdf_text[text_idx].encode("utf-8"):
                #     sentence_idx = text_idx
                # elif tmp.encode("utf-8") in pdf_text[text_idx + 1].encode("utf-8"):
                #     text_idx += 1
                #     sentence_idx = text_idx
                new_tag = BeautifulSoup.BeautifulSoup("<span class=\"word %d\"></span>" %(word_idx)).find("span")
                sentence.append(tmp.encode("utf-8"))
                word_idx += 1
                new_tag.insert(0, tmp.encode("utf-8"))
                child.append(new_tag)
                new_tag = BeautifulSoup.BeautifulSoup("<span class=\"word %d\"></span>" %(word_idx)).find("span")
                new_tag.insert(0, " ")
                child.append(new_tag)
            new_tag = BeautifulSoup.BeautifulSoup("<span class=\"word %d\"></span>" %(word_idx)).find("span")
            sentence.append(words[idx][-1].encode("utf-8"))
            word_idx += 1
            new_tag.insert(0, words[idx][-1].encode("utf-8"))
            child.append(new_tag)
            child.append(span_node[idx])
            if span_node[idx].name == "div":
                break

    if words[-1] != []:
        for words_idx, tmp in enumerate(words[-1][:-1]):
            new_tag = BeautifulSoup.BeautifulSoup("<span class=\"word %d\"></span>" %(word_idx)).find("span")
            sentence.append(tmp.encode("utf-8"))
            word_idx += 1
            new_tag.insert(0, tmp.encode("utf-8"))
            child.append(new_tag)
            new_tag = BeautifulSoup.BeautifulSoup("<span class=\"word %d\"></span>" %(word_idx)).find("span")
            new_tag.insert(0, " ")
            child.append(new_tag)
        new_tag = BeautifulSoup.BeautifulSoup("<span class=\"word %d\"></span>" %(word_idx)).find("span")
        sentence.append(words[-1][-1].encode("utf-8"))
        word_idx += 1
        new_tag.insert(0, words[-1][-1].encode("utf-8"))
        child.append(new_tag)

    soup.replaceWithChildren()
    # print soup

    for item in child:
        soup.append(item)
    # print soup
    return soup, word_idx, sentence

def pdf2html(filename):
    sentence = []
    sentence_idx = 0
    word_idx = 0
    # pdf_text = mapping(filename)
    # print "1\n", pdf_text[0]
    # print "2\n", pdf_text[1]
    # print "3\n", pdf_text[2]
    shutil.move(filename, "/Users/Knight/pdf/" + filename.split("/")[-1])
    subprocess.call("docker run --rm -v ~/pdf:/pdf bwits/pdf2htmlex pdf2htmlEX --zoom 1.3 " + filename.split("/")[-1], shell=True, stdout=sys.stdout, stderr=sys.stderr)
    shutil.move("/Users/Knight/pdf/" + filename.split("/")[-1], filename)
    shutil.move("/Users/Knight/pdf/" + filename.split("/")[-1][:-4] + ".html", filename[:-4] + ".html")
    with io.open(filename[:-4] + ".html", "rt", encoding="utf-8") as f:
        data = f.read()
    f = open("debugging", 'wr')
    body = data.split("<body>")[1].split("</body>")[0].split("\n")
    header = data.split("<head>")[1].split("</head>")[0]
    processed_body = []
    for line in body:
        if "data-page-no=" in line:
            f.write(line)
            soup = BeautifulSoup.BeautifulSoup(line, fromEncoding='utf-8')
            div = soup.findChildren(recursive=False)
            # soup.replaceWithChildren()
            for i in range(len(div)):
                if div[i].name == "div":
                    sub_div = div[i].findChildren(recursive=False)
                    div[i].replaceWithChildren()
                    for j in range(len(sub_div)):
                        if sub_div[j].name == "div":
                            tags = sub_div[j].findChildren(recursive=False)
                            sub_div[j].replaceWithChildren()
                            # print sub_div
                            for idx in range(len(tags)):
                                if tags[idx].name == "div":
                                    if "today" in tags[idx].text:
                                        print repr(tags[idx].text)
                                    tags[idx], word_idx, sentence = spaning(tags[idx], word_idx, sentence)
                                sub_div[j].append(tags[idx])
                        div[i].append(sub_div[j])
            processed_body.append(str(div[i]))
            f.write(str(div[i]))
        else:
            processed_body.append(line)
    f.close()
    sentence_dict = words2sentence(sentence)
    print sentence_dict
    return {"body":'\n'.join(processed_body), "header":header}, 1, sentence_dict
# pdf2html("../upload/p432-hassanieh.pdf")
# read_file("/Users/Knight/PycharmProjects/2018-Graduation-Project/upload/p432-hassanieh.pdf")
# a = mapping("/Users/Knight/PycharmProjects/2018-Graduation-Project/upload/multipath_mobicom16.html")
# print repr(a[0])
# a = mapping("/Users/Knight/PycharmProjects/2018-Graduation-Project/upload/p432-hassanieh.pdf")
# while(True):
#     print a[int(raw_input())]