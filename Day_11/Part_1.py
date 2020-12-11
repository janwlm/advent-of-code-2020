import copy

def readInput():
    inputFile = open("input.txt").readlines()
    tempArr = []
    for line in inputFile:
        tempArr.append(list(line.strip()))
    return tempArr

def checkAdjacent(i, j, seats):
    adjacent = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if(x != i or y != j):
                if(x < len(seats) and x >= 0 and y < len(seats[0]) and y >= 0):
                    if(seats[x][y] == "#"):
                        adjacent += 1
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
            elif(seats[i][j] == "#" and adjacent >= 4):
                new_seats[i][j] = "L"

    if(seats == new_seats):
        break

result = 0
for a in new_seats:
    result += a.count("#")

print(result)