import csv
from sklearn.feature_selection import SelectKBest, SelectPercentile, f_classif, mutual_info_classif
from sklearn.naive_bayes import GaussianNB

def nb(colLabels, dataMat, classes,label):
    print()
    print()
    print("--------- "+label+" ---------")
    print()
    print()
    gnb = GaussianNB()
    #print(len(pred))
    fit = gnb.fit(dataMat,classes)
    pred = fit.predict(dataMat)
    acc = sum(1 for i in range(len(pred)) if pred[i] == classes[i])
    print("accuracy: "+str(acc/len(pred)))
    theta = fit.theta_;
    print("averages for W/L: ")
    for i in range(len(theta[0])):
        print("\t"+colLabels[i]+" "+str(theta[1][i])+"/"+str(theta[0][i]))
    print()
