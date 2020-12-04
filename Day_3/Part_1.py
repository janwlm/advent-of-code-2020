def readInput():
    lines = open("input.txt", "r").readlines()
    outputArr = []
    for line in lines:
        outputArr.append(list(line.strip()))
    return outputArr

puzzleInput = readInput()
currentX = 0
currentY = 0
counter = 0
while True:
    if(currentY >= len(puzzleInput)):
        break
    if(-len(puzzleInput[0]) <= currentX < len(puzzleInput[0]) and -len(puzzleInput) <= currentY < len(puzzleInput)):
        if(puzzleInput[currentY][currentX] == "#"):
            counter += 1 
        currentX += 3
        currentY += 1
    else:
        currentX = currentX - len(puzzleInput[0])
print(counter)