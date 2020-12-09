def readInput():
    inputLines = open("input.txt", "r").readlines()
    tempArr = []
    for line in inputLines:
        tempArr.append(int(line.strip()))
    return tempArr

preamble = 25
data = readInput()
for i in range(preamble, len(data)):
    isSum = False
    for x in range(i - preamble, i):
        for y in range(i - preamble, i):
            if(data[x] != data[y] and data[i] == data[x] + data[y]):
                isSum = True
                break

    if(not isSum):
        print(data[i])
        break