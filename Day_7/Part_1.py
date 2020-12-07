def readInput():
    inputLines = open("input.txt", "r").readlines()
    outputArr = []
    for line in inputLines:
        outputArr.append(line.strip().replace(".", "").replace("no", "0").replace("contain", "").replace("bags", "").replace("other", "").replace("bag", ""))
    return outputArr

def checkAnotherRound(checkString, cleanRules):
    outputArr = []
    for rule in cleanRules:
        if checkString in rule[1]:
            outputArr.append(rule[0])
    if(len(outputArr) == 0):
        return False
    else:
        return True

rules = readInput()
cleanRules = []
tempArr = []
topName = ""
tempName = ""
for rule in rules:
    if(rule.count(",") == 0):
        tempArr = rule.split(" ")
        tempArr = list(filter(None, tempArr))
        topName = tempArr[0] + tempArr[1]
        if(len(tempArr) == 5):
            tempName = tempArr[-2] + tempArr[-1]
            cleanRules.append([topName, tempName])
        else:
            cleanRules.append([topName, "0"])
    else:
        tempArr2 = []
        tempArr = rule.split(" ")
        tempArr = list(filter(None, tempArr))
        topName = tempArr[0] + tempArr[1]
        arrLen = len(tempArr)
        for i in range(3, arrLen - 1):
            if(tempArr[i].isdigit() == False and tempArr[i+1].isdigit() == False and tempArr[i+1] != ","):
                tempArr2.append(tempArr[i] + tempArr[i + 1])
        tempArr = []
        tempArr.append(topName)
        tempArr.append(tempArr2)
        cleanRules.append(tempArr)

possibleOuterBags = []
for rule in cleanRules:
    if "shinygold" in rule[1]:
        possibleOuterBags.append(rule[0])

possibleOuterBagsTemp2 = list(possibleOuterBags)
stop = True
while stop:
    possibleOuterBagsTemp = list(possibleOuterBagsTemp2)
    possibleOuterBagsTemp2 = []
    for x in possibleOuterBagsTemp:
        if(checkAnotherRound(x, cleanRules)):
            for rule in cleanRules:
                if x in rule[1]:
                    possibleOuterBags.append(rule[0])
                    possibleOuterBagsTemp2.append(rule[0])
    if(len(possibleOuterBagsTemp2) == 0):
        stop = False
print(len(list(dict.fromkeys(possibleOuterBags))))