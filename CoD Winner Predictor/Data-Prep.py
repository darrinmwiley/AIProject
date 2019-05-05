import csv
from sklearn.feature_selection import SelectKBest, SelectPercentile, f_classif, mutual_info_classif

loadoutId = [[],[],[],[]]
colLabel = []
colLabelReal = []
rowId = []
dataMat = []
classLabel = []

def inputParser(filename):
    #Read the provided csv file and lists from the provided data
    currentLine = 0
    finalSet = []

    with open(filename, newline='') as csv_file:
        dataset = list(csv.reader(csv_file, delimiter=','))
        for data in dataset:
            if currentLine == 0:
                finalSet.append(data)
            if currentLine > 0 and data[4] == 'Hardpoint':
                #finalSet.append([str(i) for i in data])
                finalSet.append(typeConvert(data))
            currentLine += 1
    return finalSet

def typeConvert(rList):
    # Converts entries in the provided list to the correct type
    updSet = []

    for i in range(len(rList)):
        if i == 3 or (i >= 9 and i < 13) or (i >= 16 and i < 24) or i == 25 or (i >= 32 and i < 52) or (i >= 53):
            updSet.append(int(rList[i]))
        elif (i >= 13 and i < 16 or (i >= 26 and i < 28) or i == 52):
            updSet.append(float(rList[i]))
        elif i == 24:
            updSet.append(float(rList[i].strip('%')) / 100)
        else:
            updSet.append(str(rList[i]))
    return updSet

def splitData(dataset):
    global colLabel

    currentLine = 0

    for data in dataset:
        idTemp = []
        dataTemp = []

        if currentLine == 0 and not colLabel:
            for i in range(len(data)):
                if not ((i >= 35 and i < 53) or i == 8 or i == 9 or i == 33):
                    colLabel.append(data[i])
        else:
            for i in range(len(data)):
                if i < 8:
                    idTemp.append(data[i])
                elif i == 8:
                    classLabel.append(data[i])
                elif i >= 28 and i < 32:
                    if data[i] in loadoutId[i-28]:
                        dataTemp.append(loadoutId[i-28].index(data[i]))
                    else:
                        dataTemp.append(len(loadoutId[i-28]))
                        loadoutId[i-28].append(data[i])
                elif (i >= 35 and i < 53) or i == 9 or i == 33:
                    pass
                else:
                    dataTemp.append(data[i])
            rowId.append(idTemp)
            dataMat.append(dataTemp)

def writeToFile(used):
    file = open("data-formatted.txt","w")
    line = "";
    for i in range(len(colLabel)-len(rowId[0])):
        if used[i]:
            line += str(colLabel[i+len(rowId[0])]+",")
    file.write(line[0:-1])
    file.write("\n")
    for i in range(len(dataMat)):
        line = ""
        for j in range(len(dataMat[i])):
            if(used[j]):
                line+=(str(dataMat[i][j])+",");
        file.write(line[0:-1])
        file.write("\n")
    file.close()
    file = open("classes-formatted.txt","w")
    for x in range(len(classLabel)):
        file.write(str(classLabel[x]))
        if x != len(classLabel)-1:
            file.write(" ")
    file.close()

d1 = inputParser("data-2018-01-14-neworleans.csv")
splitData(d1)

eliminator = SelectPercentile(mutual_info_classif, percentile=30)
newDataMat = eliminator.fit_transform(dataMat, classLabel)
used = (eliminator.get_support())
output = "[";
for x in range(len(used)):
    if used[x]:
        output += colLabel[x+len(rowId[0])]+", "
print("factors used:")
print(output[0:-2]+"]")
writeToFile(used)
