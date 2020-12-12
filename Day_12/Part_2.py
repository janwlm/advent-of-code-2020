def parse_input():
    inputFile = open("input.txt").readlines()
    tempArr = []
    for line in inputFile:
        tempArr.append(line.strip())
    return tempArr

def turn_left(waypointCoord, value):
    if(value == 90):
        waypointCoord = [-1*(waypointCoord[1]), waypointCoord[0]]
    elif(value == 180):
        waypointCoord = [-1*(waypointCoord[0]), -1*(waypointCoord[1])]
    elif(value == 270):
        waypointCoord = [waypointCoord[1], -1*(waypointCoord[0])]
    return waypointCoord

def turn_right(waypointCoord, value):
    if(value == 90):
        waypointCoord = [waypointCoord[1], -1*(waypointCoord[0])]
    elif(value == 180):
        waypointCoord = [-1*(waypointCoord[0]), -1*(waypointCoord[1])]
    elif(value == 270):
        waypointCoord = [-1*(waypointCoord[1]), waypointCoord[0]]
    return waypointCoord

shipCoord = [0, 0]
waypointCoord = [10, 1]
for element in parse_input():
    instruction = element[0]
    value = int(element[1:])
    
    if(instruction == "N"):
        waypointCoord[1] += value
    elif(instruction == "S"):
        waypointCoord[1] -= value
    elif(instruction == "E"):
        waypointCoord[0] += value
    elif(instruction == "W"):
        waypointCoord[0] -= value
    elif(instruction == "L"):
        waypointCoord = turn_left(waypointCoord, value)
    elif(instruction == "R"):
        waypointCoord = turn_right(waypointCoord, value)
    elif(instruction == "F"):
        shipCoord[0] += value*waypointCoord[0]
        shipCoord[1] += value*waypointCoord[1]  

print(abs(shipCoord[0]) + abs(shipCoord[1]))