import csv
from sklearn.svm import SVC
import random

def sv(colLabels, dataMat, classes, label):
    print()
    print()
    print("---------- "+label+" ----------")
    print()
    print()
    indices = []
    for i in range(len(dataMat)):
        indices.append(i)
    random.shuffle(indices)
    trainsize = int(len(dataMat)*.75)

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

    svm = SVC(kernel='linear')
    fit = svm.fit(trainx,trainy)
    pred = fit.predict(testx)
    #print(len(pred))
    acc = sum(1 for i in range(len(pred)) if pred[i] == testy[i])
    print("accuracy: "+str(acc/len(pred)))
    print("# of support vectors: "+str(len(fit.support_)))

    print('b ='+str(fit.intercept_[0]))

    print("Coefficients: ")
    cof = fit.coef_
    for i in range(len(cof[0])):
        print("\t"+colLabels[i]+" "+str(cof[0][i]))
    
