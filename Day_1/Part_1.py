def readInput():
    lines = open("input.txt", "r").readlines()
    outputArr = []
    for line in lines:
        outputArr.append(int(line))
    return outputArr

puzzleInput = readInput()
for expense in puzzleInput:
    for otherExpense in puzzleInput:
        if(expense + otherExpense == 2020):
            print(expense * otherExpense)
            exit()