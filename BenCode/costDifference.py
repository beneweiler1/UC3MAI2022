from ast import comprehension
import csv
import pandas as pd
import numpy as np
from pprint import pp

def dayCalc(intervals):
    total = intervals * 20 
    day = 86400.0
    if total < day:
       return 0
    elif total >= day*2:
        return 2
    else:
        return 1

def timeCalc(intervals):
    while intervals >= 86400:
        intervals = intervals - 86400
    minu = intervals / 60
    hour = minu /60
    return np.floor(hour)

df = pd.read_csv('data.csv', delimiter=';')
df = df.replace("Low", 0)
df = df.replace("High", 1)

df['i'] = range(1, len(df) + 1)
df['day'] = df.apply(lambda row: dayCalc(row.i), axis=1)
df['time'] = df.apply(lambda row: timeCalc(row.i), axis=1)

counter = df.groupby(['G']).size()
meanCalc = df.groupby(['G']).mean()

comboBinary = np.array([[0, 0, 0], [0, 0, 1],[0, 1, 0],[0, 1, 1],[1, 0, 0],[1, 0, 1],[1, 1, 0],[1, 1, 1]])

indexX = 0

def makeArray():
    array = np.zeros((9,9))
    array[0][0] = 0
    array[0][1] = 0
    array[0][2] = 1
    array[0][3] = 10
    array[0][4] = 11
    array[0][5] = 100
    array[0][6] = 101
    array[0][7] = 110
    array[0][8] = 111

    array[0][0] = 0
    array[1][0] = 0
    array[2][0] = 1
    array[3][0] = 10
    array[4][0] = 11
    array[5][0] = 100
    array[6][0] = 101
    array[7][0] = 110
    array[8][0] = 111
    return array

directions = ["N","W","E"]

arrN = []
arrE = []
arrW = []
index = 0
for d in directions:
    array = makeArray()
    #print(d)
    indexX = 1
    for i in comboBinary:
        initial = df.query('iN ==' + str(i[0]) + '& iE ==' + str(i[1]) + '& iW ==' + str(i[2]))  # initial north
        inital = initial.query('G==' + '"' + str(d)+'"')
        total = inital.iN.count()
        indexY = 1
        for j in comboBinary: 
            final = df.query('iN =='+ str(i[0])+ '& iE ==' + str(i[1])+ '& iW ==' + str(i[2]) + '& fN =='+ str(j[0])+ '& fE ==' + str(j[1])+ '& fW ==' + str(j[2]))
            final = final.query('G==' + '"' + str(d)+'"')
            probCond = final.iN.count() / total
            array[indexX][indexY] = probCond
            indexY += 1
        indexX += 1

    if index == 0:
        arrN = array
    if index == 1:
        arrW = array
    if index == 2:
        arrE = array
    index += 1


def dirCalc(arrD, values, value, orginalD, costChange):
    sum =0
    for i in range (1, len(arrD[value])):
        sum += arrD[value][i]*values[i-1]
    if orginalD == 1:
        return sum + 1 
    else:
        return sum + costChange


def generalAlg(arrN, arrE, arrW, Di, costChange):
    #direction 0 = North, 1 = East, 2 = West
    values = np.zeros(8)
    optimalDirections = np.zeros(8)
    maxi = 450
    for p in range(0,maxi):
        for x in range (2,9):
            if Di == 0: #north:
                n = dirCalc(arrN,values,x,1,costChange)
                e = dirCalc(arrE,values,x,0,costChange)
                w = dirCalc(arrW,values,x,0,costChange)
                values[x-1] = min(n,e,w)
                if n < e and n < w:
                    Di = 0
                elif e < n and e < w:
                    Di = 1
                else:
                    Di = 2
            if Di == 1: #East:
                n = dirCalc(arrN,values,x,0,costChange)
                e = dirCalc(arrE,values,x,1,costChange)
                w = dirCalc(arrW,values,x,0,costChange)
                values[x-1] = min(n,e,w)
                if n < e and n < w:
                    Di = 0
                elif e < n and e < w:
                    Di = 1
                else:
                    Di = 2
            if Di == 2: #West:
                n = dirCalc(arrN,values,x,0,costChange)
                e = dirCalc(arrE,values,x,0,costChange)
                w = dirCalc(arrW,values,x,1,costChange)
                values[x-1] = min(n,e,w)
                if n < e and n < w:
                    Di = 0
                elif e < n and e < w:
                    Di = 1
                else:
                    Di = 2
            optimalDirections[x-1] = Di

        if (p%100 == 1):
            print(values)
    for x in range(1,len(comboBinary)):
        if optimalDirections[x] == 0:
            print(comboBinary[x],': N')
        elif optimalDirections[x] == 1:
            print(comboBinary[x],': E')
        else:
            print(comboBinary[x], ': W')



originState = 1 #0=north, 1 = east, 2 = west
costToChange = 1


generalAlg(arrN, arrE, arrW, originState, costToChange)
