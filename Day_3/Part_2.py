def readInput():
    lines = open("input.txt", "r").readlines()
    outputArr = []
    for line in lines:
        outputArr.append(list(line.strip()))
    return outputArr

puzzleInput = readInput()
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
result = 1
for slope in slopes:
    counter = 0
    currentX = 0
    currentY = 0
    while True:
        if(currentY >= len(puzzleInput)):
            break
        if(-len(puzzleInput[0]) <= currentX < len(puzzleInput[0]) and -len(puzzleInput) <= currentY < len(puzzleInput)):
            if(puzzleInput[currentY][currentX] == "#"):
                counter += 1 
            currentX += slope[0]
            currentY += slope[1]
        else:
            currentX = currentX - len(puzzleInput[0])
    result = result * counter
print(result)