import csv
from league.NaiveBayes import nb
from league.DecisionTrees import dt
from league.BoostedTrees import boost
from league.RandomForest import rf

print()

from DataPrep import data

def convert2(arr):
    ret = []
    for i in range(len(arr)):
        ret.append(convert(arr[i]))
    return ret

def convert(arr):
    ret = []
    for i in range(len(arr)):
        if arr[i]:
            ret.append(1)
        else:
            ret.append(0)
    return ret

def convertWL(arr):
    ret = []
    for i in range(len(arr)):
        if arr[i] == 'Win':
            ret.append(1)
        else:
            ret.append(0)
    return ret

def league():
    dat = data()
    colLabelInd = dat[0]
    dataMatInd = dat[1]
    classLabelInd = dat[2]
    colLabelTeam = dat[3]
    dataMatTeam = dat[4]
    classLabelTeam = dat[5]
    nb(colLabelTeam,dataMatTeam,classLabelTeam,"League Of Legends Naive Bayes Using Team Based Data")
    dt(colLabelTeam,dataMatTeam,classLabelTeam,"League Of Legends Decision Tree Using Team Based Data","league-team")
    boost(colLabelTeam,convert2(dataMatTeam),convertWL(classLabelTeam),"League Of Legends Boosted Trees Using Team Based Data")
    rf(colLabelTeam,convert2(dataMatTeam),convertWL(classLabelTeam),"League Of Legends Random Forest Using Team Based Data")
    nb(colLabelInd,dataMatInd,classLabelInd, "League Of Legends Naive Bayes Using Individual Based Data")
    dt(colLabelInd,dataMatInd,classLabelInd,"League Of Legends Decision Tree Using Individual Based Data","league-ind")
    boost(colLabelInd,dataMatInd,classLabelInd,"League Of Legends Boosted Trees Using individual Based Data")
    rf(colLabelInd,dataMatInd,classLabelInd,"League Of Legends Random Forest Using individual Based Data")
