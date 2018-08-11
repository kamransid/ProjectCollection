import sqlite3
import time
import datetime
import os

os.environ['TZ'] = 'Asia/Calcutta'


db = 'sentdex.db'
conn = sqlite3.connect(db)
c = conn.cursor()

iffordb = 4
keyword = 'Python Sentimate'
value = 7
sql = "select * from stuffToPlot where keyword = ?"
wordUsed = keyword
wordUsed = 'Python Sentiment'
def readData():
    for row in c.execute(sql,[(wordUsed)]):
        print(str(row))


def tableCreate():
    c.execute("create table stuffToPlot(id int, unix real, datestamp text, keyword text, value real)")


def dataEntry():
    c.execute("insert into stuffToPlot values(1,1533475675.456,'2018-08-5 13:27:55', 'Python Sentiment', 5)")
    c.execute("insert into stuffToPlot values(2,1533475850.567,'2018-08-5 13:30:50', 'Python Sentiment', 6)")
    c.execute("insert into stuffToPlot values(3,1533475914.669,'2018-08-5 13:31:54', 'Python Sentiment', 4)")
    conn.commit()

def showUnixTime():
    print(time.asctime())

def showDateTime():
    print (dateTime)    

def dataEntryByVariable():
    dateTime = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("insert into stuffToPlot(id,unix,datestamp,keyword,value) values(?,?,?,?,?)", (iffordb,time.time(),dateTime,keyword,value))
    conn.commit()


def valueCheck(number):
    number+=5

number = 10

valueCheck(number)

print(number);




def main():
    num1 = int(input());
    num2 = int(input());
    num3 = float(input());
    print(num3)
    #num3 = str(input())
    #num4 = float(input())
    print(num1+num2);

def setCheck():
    set = {'kamran','kamran','bhai'}
    for e in set:
        print(len(set))




##################################################
        ##################################################
        ##################################################
        ##################################################
        ##################################################
        ##################################################
        ##################################################
        ##################################################
        ##################################################
        ##################################################
        ##################################################
##################################################


def tryCheck():
    try:
        hello = 2+'Hello'
    except Exception as e:
        print('Hello Bhai Log this an exception of :::'+str(e))
    










