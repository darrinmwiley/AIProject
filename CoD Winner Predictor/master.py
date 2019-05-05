import csv
from DataPrep import data
from NaiveBayes import nb
from DecisionTrees import dt

print()
dat = data()
colLabel = dat[0]
dataMat = dat[1]
classLabel = dat[2]
nb(colLabel, dataMat, classLabel, "Naive Bayes for COD data")
dt(colLabel, dataMat, classLabel, "Decision Tree for COD data","cod_tree")
