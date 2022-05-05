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

#prob where iN = 1 D = 'E' and fN =1

#prob = df.loc(df.iN == 1, df.G == 'W', df.fN ==1)
prob = df.query('iN == 1')
prob = prob.query('fN == 1')
#prob = prob.query('G')
#print(prob.groupby(['iN']).count())
print(prob.G.count())
#print(meanCalc)
#print(meanCalc)

#probability of (iD, D, fD) for all states
#df.groupby(['G']) where iD = D is (1,2) and fD = D (1,2)
