import csv
from sklearn.feature_selection import SelectKBest, SelectPercentile, f_classif, mutual_info_classif
from sklearn.ensemble import GradientBoostingRegressor
import random

def roundarr(arr):
    ret = []
    for i in range(len(arr)):
        ret.append(int(round(arr[i])))
    return ret;

def boost(colLabels, dataMat, classes, label):
    print()
    print()
    print("--------- "+label+" ---------")
    print()
    print()
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

    boost = GradientBoostingRegressor(max_depth = 5)
    boost.fit(trainx,trainy)
    pred = roundarr(boost.predict(testx))
    acc = sum(1 for i in range(len(pred)) if pred[i] == testy[i])
    print("accuracy: "+str(acc/len(pred)))
    print("importances: ")
    imp = boost.feature_importances_
    for i in range(len(imp)):
        print("\t"+colLabels[i]+" "+str(imp[i]))
