import math

class part:
    def __init__(self, name):
        self.__name = name
        self.__val1 = None
        self.__val2 = None
        self.__coefficient = 0.0

    def addValue(self, val, diff=1.0):
        if self.__val1 is None:
            self.__val1 = val
        elif self.__val2 is None:
            self.__val2 = val
            self.__coefficient += math.fabs(self.__val2 - self.__val1) / math.fabs(diff)
        else:
            self.__val1 = self.__val2
            self.__val2 = val
            self.__coefficient += math.fabs(self.__val2 - self.__val1) / math.fabs(diff)

    def getName(self, ):
        return self.__name

    def getCoefficient(self):
        return str('%+10f' % self.__coefficient)

def readdata(path):
    data = open(path, 'r', encoding='utf-8')
    xc = 0
    datalist = []
    res = []
    for i in data:
        z = i.replace('\n', '').split(' ')
        if xc == 0:
            for j in range(1, len(z)):
                datalist.append(part(z[j]))
            xc += 1
        elif xc == 1:
            res.append(float(z[0]))
            for j in range(1, len(z)):
                datalist[j - 1].addValue(float(z[j]))
            xc += 1
        else:
            if len(res) == 2:
                res[0] = res[1]
                res[1] = float(z[0])
            else:
                res.append(float(z[0]))
            for j in range(1, len(z)):
                if not float(res[1] - res[0]) == 0:
                    datalist[j - 1].addValue(float(z[j]), float(res[1] - res[0]))
    return datalist

def printresult(datalist):
    for i in datalist:
        print(i.getName() + ' ' + i.getCoefficient())

def main():
    datapath = input('Enter path to data file: ')
    printresult(readdata(datapath))

main()
