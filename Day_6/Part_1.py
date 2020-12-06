def readInput():
    lines = open("input.txt", "r").readlines()
    outputArr = []
    for line in lines:
        outputArr.append(line.strip())
    return outputArr

tempStr = ""
filteredInput = []
for element in readInput():
    if(element != ""):
        tempStr += element
    else:
        filteredInput.append(tempStr)
        tempStr = ""
filteredInput.append(tempStr)

result = 0
for group in filteredInput:
    result += len("".join(set(group)))
print(result)