def readInput():
    inputLines = open("input.txt", "r").readlines()
    outputArr = []
    for line in inputLines:
        outputArr.append(line.strip().replace(".", "").replace("no", "0").replace("contain", "").replace("bags", "").replace("other", "").replace("bag", ""))
    return outputArr

def checkAnotherRound(checkString, cleanRules):
    for rule in cleanRules:
        if checkString in rule[0]:
            if(rule[1] == "0"):
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
            cleanRules.append([topName,tempArr[-3] + tempName])
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
                tempArr2.append(tempArr[i - 1] + tempArr[i] + tempArr[i + 1])
        tempArr = []
        tempArr.append(topName)
        tempArr.append(tempArr2)
        cleanRules.append(tempArr)

result = 0
possibleInnerBags = []
for rule in cleanRules:
    if "shinygold" in rule[0]:
        if(isinstance(rule[1], list)):
            for i in rule[1]:
                possibleInnerBags.append(i)
        else:
            possibleInnerBags.append(rule[1])

for x in possibleInnerBags:
    result += int(x[0])

possibleInnerBagsTemp2 = list(possibleInnerBags)
stop = True
while stop:
    possibleInnerBagsTemp = list(possibleInnerBagsTemp2)
    possibleInnerBagsTemp2 = []
    for x in possibleInnerBagsTemp:
        digit = int(''.join(c for c in x if c.isdigit()))
        letters = ''.join(c for c in x if not c.isdigit())
        if(checkAnotherRound(letters, cleanRules)):
            for rule in cleanRules:
                if letters in rule[0]:
                    if(isinstance(rule[1], list)):
                        for i in rule[1]:
                            oldDigit = int(''.join(c for c in i if c.isdigit()))
                            result += oldDigit * digit
                            possibleInnerBagsTemp2.append(str(oldDigit*digit) + ''.join(c for c in i if not c.isdigit()))
                    else:
                        oldDigit = int(''.join(c for c in rule[1] if c.isdigit()))
                        result += oldDigit * digit
                        possibleInnerBagsTemp2.append(str(oldDigit*digit) + ''.join(c for c in rule[1] if not c.isdigit()))
    if(len(possibleInnerBagsTemp2) == 0):
        stop = False
print(result)