import pandas as pd
import numpy as np
from pprint import pp

def dayCalc(intervals): #not important unless we are organizing by time
    total = intervals * 20 
    day = 86400.0
    if total < day:
       return 0
    elif total >= day*2:
        return 2
    else:
        return 1

def timeCalc(intervals): #not important unless we are organizing by time
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

comboBinary = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])

indexX = 0

def makeArray(): #makes array x and y coordinates
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
def array_maker():
    directions = ["N","W","E"]

    arrN = []
    arrE = []
    arrW = []
    index = 0
    for d in directions:
        array = makeArray()
        #print(d)
        indexX = 1
        for i in comboBinary: #iterate through traffic patterns
            initial = df.query('iN ==' + str(i[0]) + '& iE ==' + str(i[1]) + '& iW ==' + str(i[2]))  #query to get initial traffic
            inital = initial.query('G==' + '"' + str(d)+'"') #query to get designated traffic light on
            total = inital.iN.count() #sum of all values within query
            indexY = 1
            for j in comboBinary: #iterate through traffic for each final state
                final = df.query('iN ==' + str(i[0]) + '& iE ==' + str(i[1])+ '& iW ==' + str(i[2]) + '& fN ==' + str(j[0])
                                 + '& fE ==' + str(j[1]) + '& fW ==' + str(j[2]))
                final = final.query('G==' + '"' + str(d)+'"')
                probCond = final.iN.count() / total
                array[indexX][indexY] = probCond
                indexY += 1
            indexX += 1

        if index == 0:
            arrN = array  # north iteration
        if index == 1:
            arrW = array  # west iteration
        if index == 2:
            arrE = array  # east iteration
        index += 1
    return arrN, arrW, arrE


def dirCalc(arrD, values, col, orginalD, costChange):
    sum =0
    for i in range(1, len(arrD[col])):
        sum += arrD[col][i]*values[i-1]  # selects col, iterates through all row values in row and multiplies by
                                         # its designated weight in values array
    if orginalD == 1:  # not changing traffic light N-N or E-E or W-W
        return sum + 1 
    else:  # changing traffic light ex. N-E, or E-W or N-W....
        return sum + costChange


def generalAlg(arrN, arrE, arrW, Di, costChange):
    #direction 0 = North, 1 = East, 2 = West
    values = np.zeros(8)
    optimalDirections = np.zeros(8)
    maxi = 450
    for p in range(0,maxi):
        for x in range (2,9):
            if Di == 0: #previous location is north:
                n = dirCalc(arrN,values,x,1,costChange)
                e = dirCalc(arrE,values,x,0,costChange)
                w = dirCalc(arrW,values,x,0,costChange)
                values[x-1] = min(n,e,w)
                if n < e and n < w: #set previous direction to north
                    Di = 0
                elif e < n and e < w: #set previos direction to east 
                    Di = 1
                else: #set previous location to west
                    Di = 2
            if Di == 1: #previous location is East:
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
            if Di == 2: #previous location is West:
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
            #print(pd.DataFrame(values))
            for x in range(1, len(values)):
                a = 1
                # print(comboBinary[x],': ',values[x])
            # print(values)
    my_optimal_policy = []
    my_optimal_policy_dic = {}
    for x in range(1, len(comboBinary)):
        if optimalDirections[x] == 0:
            # print(comboBinary[x],': N')
            my_optimal_policy.append(str(comboBinary[x]) + ': N')
            my_optimal_policy_dic[str(comboBinary[x])] = "N"
        elif optimalDirections[x] == 1:
            # print(comboBinary[x],': E')
            my_optimal_policy.append(str(comboBinary[x]) + ': E')
            my_optimal_policy_dic[str(comboBinary[x])] = "E"
        else:
            # print(comboBinary[x], ': W')
            my_optimal_policy.append(str(comboBinary[x]) + ': W')
            my_optimal_policy_dic[str(comboBinary[x])] = "W"
        # print(my_optimal_policy)

    return my_optimal_policy_dic

def main_function(originState, costToChange):

    # originState = 0 #0=north, 1 = east, 2 = west
    # costToChange = 1.5 #change this value to manipulate cost to change traffic light color
    arrN, arrW, arrE = array_maker()
    optimal_policy  = generalAlg(arrN, arrE, arrW, originState, costToChange)
    return optimal_policy
