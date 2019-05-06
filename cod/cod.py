import csv
from cod.DataPrep import data
from cod.NaiveBayes import nb
from cod.DecisionTrees import dt
from cod.BoostedTrees import boost
from cod.RandomForest import rf

def convertWL(arr):
    ret = []
    for i in range(len(arr)):
        if arr[i] == 'W':
            ret.append(1)
        else:
            ret.append(0)
    return ret

def cod():
    print()
    dat = data()
    colLabel = dat[0]
    dataMat = dat[1]
    classLabel = dat[2]
    nb(colLabel, dataMat, classLabel, "Naive Bayes for COD data")
    dt(colLabel, dataMat, classLabel, "Decision Tree for COD data","cod_tree")
    rf(colLabel, dataMat, convertWL(classLabel), "Random Forest for COD data")
    boost(colLabel, dataMat, convertWL(classLabel), "Boosted Trees for COD data")
