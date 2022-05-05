import csv
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv', delimiter=';')
df = df.replace("Low", 0)
df = df.replace("High",1)

#print(df.sum(axis=0))
#print(df.mean(axis=0))

counter = df.groupby(['G']).size()
meanCalc = df.groupby(['G']).mean()

#print(meanCalc)
#prob where iN = 1 D = 'E' and fN =1

#prob = df.loc(df.iN == 1, df.G == 'W', df.fN ==1)

iN = 0
iE = 0
iW = 0

x = np.array([[0, 0, 0], [0, 0, 1],[0, 1, 0],[0, 1, 1],[1, 0, 0],[1, 0, 1],[1, 1, 0],[1, 1, 1]])

for i in x:
    initial = df.query('iN =='+ str(i[0])+ '& iE ==' + str(i[1])+ '& iW ==' + str(i[2])) #initial north
    #print('intial states n:'+str(i[0])+' e:'+ str(i[1])+' w:'+str(i[2]))
    #inital = initial.query('G=="N"')
    print(initial.count())
    #print(initial.groupby(['G']).count())
    #counter = initial.groupby(['G']).iN.count().to_dict()
    #print(counter)
    
    for j in x:
        final = df.query('iN =='+ str(i[0])+ '& iE ==' + str(i[1])+ '& iW ==' + str(i[2]) + '& fN =='+ str(j[0])+ '& fE ==' + str(j[1])+ '& fW ==' + str(j[2]))
        #print('final states n:'+str(j[0])+' e:'+ str(j[1])+' w:'+str(j[2]))
        #print(final.groupby(['G']).count())

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
