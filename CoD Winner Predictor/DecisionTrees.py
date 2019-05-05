import csv
from sklearn.feature_selection import SelectKBest, SelectPercentile, f_classif, mutual_info_classif
from sklearn import tree
import random

def dt(colLabels, dataMat, classes):
    indices = []
    for i in range(len(dataMat)):
        indices.append(i)
    random.shuffle(indices)
    trainsize = int(len(dataMat)*.8)

    trainx = []
    trainy = []
    testx = []
    testy = []

    for i in indices[0:trainsize]:
        trainx.append(dataMat[i])

    for i in indices[0:trainsize]:
        trainy.append(classes[i])

    for i in indices[trainsize:]:
        testx.append(dataMat[i])

    for i in indices[trainsize:]:
        testy.append(classes[i])

    clf = tree.DecisionTreeClassifier()
    fit = clf.fit(trainx,trainy)
    pred = fit.predict(testx)
    #print(len(pred))
    acc = sum(1 for i in range(len(pred)) if pred[i] == testy[i])
    print("accuracy: "+str(acc/len(pred)))
    print("importances: ")
    imp = fit.feature_importances_
    for i in range(len(imp)):
        print("\t"+colLabels[i]+" "+str(imp[i]))
