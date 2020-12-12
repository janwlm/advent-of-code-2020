import math

def parse_input():
    inputFile = open("input.txt").readlines()
    tempArr = []
    for line in inputFile:
        tempArr.append(line.strip())
    return tempArr

currentDegrees = 0
currentDirection = [1, 0]
shipCoord = [0, 0]
for element in parse_input():
    instruction = element[0]
    value = int(element[1:])
    
    if(instruction == "N"):
        shipCoord[1] += value
    elif(instruction == "S"):
        shipCoord[1] -= value
    elif(instruction == "E"):
        shipCoord[0] += value
    elif(instruction == "W"):
        shipCoord[0] -= value
    elif(instruction == "L"):
        currentDegrees += value
        currentDirection[0] = int(math.cos((currentDegrees/180)*math.pi))
        currentDirection[1] = int(math.sin((currentDegrees/180)*math.pi))
    elif(instruction == "R"):
        currentDegrees -= value
        currentDirection[0] = int(math.cos((currentDegrees/180)*math.pi))
        currentDirection[1] = int(math.sin((currentDegrees/180)*math.pi))
    elif(instruction == "F"):
        shipCoord[0] += value*currentDirection[0]
        shipCoord[1] += value*currentDirection[1]

print(abs(shipCoord[0]) + abs(shipCoord[1]))