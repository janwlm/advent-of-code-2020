def readInput():
    inputLines = open("input.txt", "r").readlines()
    tempArr = []
    tempArr.append(0)
    for line in inputLines:
        tempArr.append(int(line))
    tempArr = sorted(tempArr)
    tempArr.append(tempArr[-1] + 3)
    return tempArr

cache = [0]*(len(readInput()))
def possibleSolutions(sortedInput, i):
    if(i == (len(sortedInput) - 1)):
        return 1

    result = 0
    for j in range(i + 1, min(i + 4, len(sortedInput))):
        if(sortedInput[j] - sortedInput[i] <= 3):
            if(cache[j] == 0):
                cache[j] = possibleSolutions(sortedInput, j)
            result += cache[j]
            
    return result

sortedInput = readInput()
print(possibleSolutions(sortedInput, 0))