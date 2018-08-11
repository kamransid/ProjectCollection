from datetime import datetime
from time import mktime


def onceCall():
     readFile = open('TestDatabae.txt', 'r').read()

def writeFile():
    myFile = open('MyTextFile.txt', 'rw')
    stuffToWrite = 'hai na mere pas bhi'
    myFile.write(stuffToWrite)
    myFile.close()

def dateTime():
    print(mktime(datetime.now().timetuple()))
    #print(datetime.strptime(datetime.now()))





print('Hi Bhai')

str = '''value hai mera bhi'''
       
       
print(str)


