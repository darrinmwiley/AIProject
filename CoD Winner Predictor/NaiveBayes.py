import csv
from sklearn.feature_selection import SelectKBest, SelectPercentile, f_classif, mutual_info_classif
from sklearn.naive_bayes import GaussianNB

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

def nb():
    read()
    gnb = GaussianNB()
    #print(len(pred))
    fit = gnb.fit(dataMat,classes)
    pred = fit.predict(dataMat)
    acc = sum(1 for i in range(len(pred)) if pred[i] == classes[i])
    print("accuracy: "+str(acc/len(pred)))
    print(fit.theta_);

nb()
