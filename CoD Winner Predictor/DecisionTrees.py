import csv
from sklearn.feature_selection import SelectKBest, SelectPercentile, f_classif, mutual_info_classif
from sklearn import tree
import random

colLabels = []
dataMat = []
classes = []

def read():
    #Read the provided csv file and lists from the provided data
    currentLine = 0

    with open("data-formatted.txt", newline='') as csv_file:
        dataset = list(csv.reader(csv_file, delimiter=','))
        for data in dataset:
            if currentLine == 0:
                colLabels = data
            else:
                dataMat.append(typeConvert(data))
            currentLine += 1

    csv_file.close()

    with open("classes-formatted.txt", newline='') as csv_file:
        lis = list(csv.reader(csv_file, delimiter=' '))
        for i in range(len(lis[0])):
            classes.append(lis[0][i])
    csv_file.close()

def typeConvert(rList):
    # Converts entries in the provided list to the correct type
    updSet = []

    whole = [0,1,2,6,7,9,10]

    for i in range(len(rList)):
        if i in whole:
            updSet.append(int(rList[i]))
        else:
            updSet.append(float(rList[i]))
    return updSet

def dt():
    read()
    indices = []
    for i in range(len(dataMat)):
        indices.append(i)
    random.shuffle(indices)
    trainsize = int(len(dataMat)*.8)
    print(trainsize)

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
    print(fit.feature_importances_)

dt()
