import math
import os

class part:
    def __init__(self, name, firstValue):
        self.__name = name
        self.__firstValue = firstValue
        self.__coefficient = 0

    def addNewValue(self, val):



def readdata(path):
    data = open('path', 'r', encoding='utf-8')
    datastring = data.read()
    data.close()



def main():
    datapath = input('Enter path to data file: ')
    readdata(datapath)

dx1k1 = 0
dx2k1 = 0
dx3k1 = 0
dx4k1 = 0
dx5k1 = 0
dx6k1 = 0
f = open('data.txt', 'r')
i = 0
line = f.readline()
x11 = float(line.strip('\n'))
line = f.readline()
x12 = float(line.strip('\n'))
line = f.readline()
x13 = float(line.strip('\n'))
line = f.readline()
x14 = float(line.strip('\n'))
line = f.readline()
x15 = float(line.strip('\n'))
line = f.readline()
x16 = float(line.strip('\n'))

line = f.readline()
res1 = float(line.strip('\n'))
try:
    while line:
        line = f.readline()
        if float(line.strip('\n')) < 1000000000:
            x21 = float(line.strip('\n'))
            line = f.readline()
            x22 = float(line.strip('\n'))
            line = f.readline()
            x23 = float(line.strip('\n'))
            line = f.readline()
            x24 = float(line.strip('\n'))
            line = f.readline()
            x25 = float(line.strip('\n'))
            line = f.readline()
            x26 = float(line.strip('\n'))
            line = f.readline()
            res2 = float(line.strip('\n'))
            i = i + 1
            razx1 = math.fabs(x21 - x11)
            razx2 = math.fabs(x22 - x12)
            razx3 = math.fabs(x23 - x13)
            razx4 = math.fabs(x24 - x14)
            razx5 = math.fabs(x25 - x15)
            razx6 = math.fabs(x26 - x16)
            razres = math.fabs(res2 - res1)
            dx1k1 = dx1k1 + (razx1 / razres)
            dx2k1 = dx2k1 + (razx2 / razres)
            dx3k1 = dx3k1 + (razx3 / razres)
            dx4k1 = dx4k1 + (razx4 / razres)
            dx5k1 = dx5k1 + (razx5 / razres)
            dx6k1 = dx6k1 + (razx6 / razres)
            x11 = x21
            x12 = x22
            x13 = x23
            x14 = x24
            x15 = x25
            x16 = x26
            res1 = res2
except:
    print(line)
f.close()
print('%+20f' % dx1k1)
print('%+20f' % dx2k1)
print('%+20f' % dx3k1)
print('%+20f' % dx4k1)
print('%+20f' % dx5k1)
print('%+20f' % dx6k1)