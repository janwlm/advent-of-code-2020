import copy

def readInput():
    inputFile = open("input.txt").readlines()
    tempArr = []
    for line in inputFile:
        tempArr.append(list(line.strip()))
    return tempArr

def checkAdjacent(i, j, seats):
    adjacent = 0

    for y in range(j + 1, len(seats[0])):
        if(seats[i][y] == "#"):
            adjacent += 1
            break
        elif(seats[i][y] == "L"):
            break

    for x in range(i + 1, len(seats)):
        if(seats[x][j] == "#"):
            adjacent += 1
            break
        elif(seats[x][j] == "L"):
            break

    for y in range(j - 1, -1, -1):
        if(seats[i][y] == "#"):
            adjacent += 1
            break
        elif(seats[i][y] == "L"):
            break
    
    for x in range(i - 1, -1, -1):
        if(seats[x][j] == "#"):
            adjacent += 1
            break
        elif(seats[x][j] == "L"):
            break

    y = j
    for x in range(i - 1, -1, -1):
        y += 1
        if(y == len(seats[0])):
            break
        if(seats[x][y] == "#"):
            adjacent += 1
            break
        elif(seats[x][y] == "L"):
            break
    
    x = i
    for y in range(j + 1, len(seats[0])):
        x += 1
        if(x == len(seats)):
            break
        if(seats[x][y] == "#"):
            adjacent += 1
            break
        elif(seats[x][y] == "L"):
            break
    
    y = j
    for x in range(i + 1, len(seats)):
        y -= 1
        if(y < 0):
            break
        if(seats[x][y] == "#"):
            adjacent += 1
            break
        elif(seats[x][y] == "L"):
            break
    
    x = i
    for y in range(j - 1, -1, -1):
        x -= 1
        if(x < 0):
            break
        if(seats[x][y] == "#"):
            adjacent += 1
            break
        elif(seats[x][y] == "L"):
            break

    return adjacent

seats = readInput()
new_seats = copy.deepcopy(seats)

while True:
    seats = copy.deepcopy(new_seats)
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            adjacent = checkAdjacent(i, j, seats)

            if(seats[i][j] == "L" and adjacent == 0):
                new_seats[i][j] = "#"
            elif(seats[i][j] == "#" and adjacent >= 5):
                new_seats[i][j] = "L"

    if(seats == new_seats):
        break

result = 0
for a in new_seats:
    result += a.count("#")

print(result)