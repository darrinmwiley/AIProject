from NaiveBayes import nb
from DecisionTrees import dt
from SupportVector import sv

print()

from DataPrep import data

dat = data()
colLabelInd = dat[0]
dataMatInd = dat[1]
classLabelInd = dat[2]
colLabelTeam = dat[3]
dataMatTeam = dat[4]
classLabelTeam = dat[5]
nb(colLabelTeam,dataMatTeam,classLabelTeam,"League Of Legends Naive Bayes Using Team Based Data")
dt(colLabelTeam,dataMatTeam,classLabelTeam,"League Of Legends Decision Tree Using Team Based Data","league-team")
sv(colLabelTeam,dataMatTeam,classLabelTeam,"League Of Legends Support Vector Machine Using Team Based Data")
nb(colLabelInd,dataMatInd,classLabelInd, "League Of Legends Naive Bayes Using Individual Based Data")
dt(colLabelInd,dataMatInd,classLabelInd,"League Of Legends Decision Tree Using Individual Based Data","league-ind")
#sv(colLabelInd,dataMatInd,classLabelInd,"League Of Legends Support Vector Machine Using Individual Based Data")