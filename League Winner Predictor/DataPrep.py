import csv
from sklearn.feature_selection import SelectKBest, SelectPercentile, f_classif, mutual_info_classif
import json

def read():
    colLabelInd = []
    ranks = ["UNRANKED","BRONZE","SILVER","GOLD","PLATINUM","DIAMOND","MASTER","GRANDMASTER","CHALLENGER"]
    colLabelTeam = ["firstBlood","firstTower","firstInhibitor","firstBaron","firstDragon","firstRiftHerald","towerKills","inhibitorKills","baronKills","dragonKills"]
    partBase = ["spell1Id","spell2Id","highestAchievedSeasonTier"]
    partStats = ["kills","deaths","assists","doubleKills","tripleKills","quadraKills","pentaKills","totalDamageDealtToChampions","totalHeal","damageSelfMitigated","damageDealtToObjectives","visionScore","goldEarned","firstBloodKill","firstTowerKill"]
    partTimeline = ["creepsPerMinDeltas","xpPerMinDeltas","csDiffPerMinDeltas","xpPerMinDeltas"]
    deltas = ["0-10","10-20","20-30","30-end"]
    dataMatInd = []
    dataMatTeam = []
    colLabel = []
    classLabelInd = []
    classLabelTeam = []
    for i in range(len(partBase)):
        colLabelInd.append(partBase[i])
    for i in range(len(partStats)):
        colLabelInd.append(partStats[i])
    for i in range(len(partTimeline)):
        colLabelInd.append(partTimeline[i])
    for i in range(1,11):
        fname = "matches"+str(i)+".json"
        file = open(fname,"r", encoding='latin-1')
        contents = file.read()
        obj = json.loads(contents);
        matches = obj['matches']
        for j in range(len(matches)):
            match = matches[j]
            teams = match['teams']
            for k in range(len(teams)):
                team = teams[k]
                classLabelTeam.append(team['win'])
                row = []
                for l in range(len(colLabelTeam)):
                    row.append(team[colLabelTeam[l]])
                dataMatTeam.append(row)
            participants = match['participants']
            for k in range(len(participants)):
                participant = participants[k]
                row = []
                for l in range(len(partBase)):
                    if l!=2:
                        row.append(participant[partBase[l]])
                    else:
                        row.append(ranks.index(participant[partBase[l]]))
                stats = participant['stats']
                classLabelInd.append(stats['win'])
                for l in range(len(partStats)):
                    if partStats[l] in stats:
                        row.append(stats[partStats[l]])
                    else:
                        row.append(False)
                timeline = participant['timeline']
                for l in range(len(partTimeline)):
                    num = 0;
                    sum = 0;
                    if partTimeline[l] in timeline :
                        delta = timeline[partTimeline[l]]
                        for m in range(len(deltas)):
                            if(deltas[m] in delta):
                                num+=1
                                sum+= delta[deltas[m]]
                    else:
                        num+=1;
                    row.append(sum/num)
                dataMatInd.append(row)
    return [colLabelInd,dataMatInd,classLabelInd,colLabelTeam,dataMatTeam,classLabelTeam]

def filter(used):
    for i in range(len(colLabel)-len(rowId[0])):
        if used[i]:
            colLabelRelevent.append(colLabel[i+len(rowId[0])])
    for i in range(len(dataMat)):
        dat = []
        for j in range(len(dataMat[i])):
            if(used[j]):
                dat.append(dataMat[i][j])
        dataRelevant.append(dat)

def data():
    dat = read()
    colLabelInd = dat[0]
    dataMatInd = dat[1]
    classLabelInd = dat[2]
    colLabelTeam = dat[3]
    dataMatTeam = dat[4]
    classLabelTeam = dat[5]
    return [colLabelInd,dataMatInd,classLabelInd,colLabelTeam,dataMatTeam,classLabelTeam]
