# -*- encoding: utf-8 -*-

import os
import sqlite3

BASE_DIR = os.path.abspath('.')
TARGET_DIR = os.path.join(BASE_DIR, "DB")
TARGET_FILE = 'dictionary.db'
TARGET_FILE_FULL_PATH = os.path.join(TARGET_DIR, TARGET_FILE)


def makeDir():
    if not os.path.isdir(TARGET_DIR):
        os.makedirs(TARGET_DIR)


def createTable():
    f=open("data.txt")

    con = sqlite3.connect(TARGET_FILE_FULL_PATH)
    cur = con.cursor()
    ##    cur.execute( 'Drop Table If Exists PhoneBook')
    ##    con.commit()

    cur.execute('''Create Table if not exists  engtohan (          
        english VARCHAR(50),
        korean VARCHAR(100)
        )
  ''')
    con.commit()

    # .기본( 필드명 없이 데이타 순서대로 ,Primary Key는 넣으면 안됨.)
    sql = "INSERT INTO engtohan VALUES ('a-','091101105093','Z ♣not know A from B  아무것도 모르다.\r');"
    cur.execute(sql)

    L = []

    while (1):
        line = f.readline()

        try:
            escape = line.index('\n')
        except:
            escape = len(line)

        if line:
            L.append(line[0:escape])
        else:
            break
        line = line.split('///')
        line1=line[1].split('\n')
        line2=line[0].split(' ')
        sql = "INSERT INTO engtohan VALUES(?, ?);"
        english, korean = line2[0], line1[0]
        cur.execute(sql, (english, korean))

    cur.close()
    con.close()
