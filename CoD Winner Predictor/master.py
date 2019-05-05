import csv
from DataPrep import data
from NaiveBayes import nb
from DecisionTrees import dt

print()
dat = data()
colLabel = dat[0]
dataMat = dat[1]
classLabel = dat[2]
nb(colLabel, dataMat, classLabel)
dt(colLabel, dataMat, classLabel)
