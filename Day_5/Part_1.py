def readInput():
    lines = open("input.txt", "r").readlines()
    outputArr = []
    for line in lines:
        outputArr.append(list(line.strip()))
    return outputArr

result = 0
for seat in readInput():
    rowRangeStart = 0
    rowRangeStop = 127
    columnRangeStart = 0
    columnRangeStop = 7
    for letter in seat:
        if(letter == "F"):
            rowRangeStop = ((rowRangeStart + rowRangeStop) - 1)/2
        elif(letter == "B"):
            rowRangeStart = ((rowRangeStart + rowRangeStop) + 1)/2
        elif(letter == "L"):
            columnRangeStop = ((columnRangeStart + columnRangeStop) - 1)/2
        elif(letter == "R"):
            columnRangeStart = ((columnRangeStart + columnRangeStop) + 1)/2
    if(rowRangeStart*8 + columnRangeStart > result):
        result = rowRangeStart*8 + columnRangeStart

print(result)