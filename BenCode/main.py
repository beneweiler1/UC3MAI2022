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
print(pd.DataFrame(df))

counter = df.groupby(['G']).size()
meanCalc = df.groupby(['G']).mean()



x = np.array([[0, 0, 0], [0, 0, 1],[0, 1, 0],[0, 1, 1],[1, 0, 0],[1, 0, 1],[1, 1, 0],[1, 1, 1]])

#xinital yfinal
#array = np.append(array,[0,1,2,3,4,5,6,7])
#print(array)
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

for d in directions:
    array = makeArray()
    print(d)
    indexX = 1
    for i in x:
        initial = df.query('iN ==' + str(i[0]) + '& iE ==' + str(i[1]) + '& iW ==' + str(i[2]))  # initial north
        # print('intial states n:'+str(i[0])+' e:'+ str(i[1])+' w:'+str(i[2]))
        inital = initial.query('G==' + '"' + str(d)+'"')
        # counter = initial.groupby(['G']).iN.count()
        total = inital.iN.count()
        indexY = 1
        for j in x: 
            final = df.query('iN =='+ str(i[0])+ '& iE ==' + str(i[1])+ '& iW ==' + str(i[2]) + '& fN =='+ str(j[0])+ '& fE ==' + str(j[1])+ '& fW ==' + str(j[2]))
                #print('final states n:'+str(j[0])+' e:'+ str(j[1])+' w:'+str(j[2]))
            final = final.query('G==' + '"' + str(d)+'"')
            probCond = final.iN.count() / total
            array[indexX][indexY] = probCond
            indexY += 1
        indexX += 1
    #pp(array, width=1000, depth=2)
    #print(pd.DataFrame(array))
#np.insert(array,x,0)
#np.savetxt("stats.csv", array, delimiter=",")

#prob = prob.query('G == N')

# prob = prob.query('fN == 0')
# prob = prob.query('fE == 0')
# prob = prob.query('fW == 0')
#prob = prob.query('G')
#print(prob.groupby(['G']).count())
#print(prob.G.count())
#print(meanCalc)
#print(meanCalc)

#probability of (iD, D, fD) for all states
#df.groupby(['G']) where iD = D is (1,2) and fD = D (1,2)
