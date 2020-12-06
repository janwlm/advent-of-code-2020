def readInput():
    lines = open("input.txt", "r").readlines()
    outputArr = []
    for line in lines:
        outputArr.append(line.strip())
    return outputArr

tempArr = []
filteredInput = []
for element in readInput():
    if(element != ""):
        tempArr.append(element)
    else:
        filteredInput.append(tempArr)
        tempArr = []
filteredInput.append(tempArr)

result = 0
for group in filteredInput:
    groupLen = len(group)
    lettersInPerson0 = len(group[0])

    for i in range(lettersInPerson0):
        notInstrings = False
        for j in range(1, groupLen):
            if(group[j].find(group[0][i]) == -1):
                notInstrings = True
        if(notInstrings == False):
            result += 1
print(result)