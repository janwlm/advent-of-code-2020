def readInput():
    inputLines = open("input.txt", "r").readlines()
    tempArr = []
    tempArr.append(0)
    for line in inputLines:
        tempArr.append(int(line))
    tempArr = sorted(tempArr)
    tempArr.append(tempArr[-1] + 3)
    return tempArr

sortedInput = readInput()

difference1 = 0
difference3 = 0
for i in range(len(sortedInput) - 1):
    joltDiff = sortedInput[i + 1] - sortedInput[i]
    if(joltDiff == 1):
        difference1 += 1
    elif(joltDiff == 3):
        difference3 += 1

print(difference1 * difference3)