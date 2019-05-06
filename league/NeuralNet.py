import csv
from sklearn.neural_network import MLPClassifier
import random

def nn(colLabels, dataMat, classes, label):
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

    svm = MLPClassifier(hidden_layer_sizes=(((len(colLabels)+1)//2),),max_iter=500)
    fit = svm.fit(trainx,trainy)
    pred = fit.predict(testx)
    #print(len(pred))
    acc = sum(1 for i in range(len(pred)) if pred[i] == testy[i])
    print("accuracy: "+str(acc/len(pred)))
    
    cof = fit.coefs_
    inte = fit.intercepts_
    
    for i in range(fit.n_layers_):
        print('Layer '+str(i))
        print('Bias: '+str(inte[i-1]))
        print('Coefficients:')
        print(cof[i-1])