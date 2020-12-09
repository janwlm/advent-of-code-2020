def readInput():
    inputLines = open("input.txt", "r").readlines()
    tempArr = []
    for line in inputLines:
        tempArr.append(int(line.strip()))
    return tempArr

preamble = 25
data = readInput()
invalidNumber = 0
for i in range(preamble, len(data)):
    isSum = False
    for x in range(i - preamble, i):
        for y in range(i - preamble, i):
            if(data[x] != data[y] and data[i] == data[x] + data[y]):
                isSum = True
                break

    if(not isSum):
        invalidNumber = data[i]
        break

startPosition = 0
i = 0
totalSum = 0
numberArr = []
while True:
    totalSum += data[i]
    numberArr.append(data[i])
    if(totalSum > invalidNumber):
        totalSum = 0
        numberArr = []
        startPosition += 1
        i = startPosition
    elif(totalSum == invalidNumber):
        print(sorted(numberArr)[0] + sorted(numberArr)[-1])
        break
    elif(totalSum < invalidNumber):
        i += 1