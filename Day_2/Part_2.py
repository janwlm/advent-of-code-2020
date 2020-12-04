def readInput():
    lines = open("input.txt", "r").readlines()
    outputArr = []
    for line in lines:
        outputArr.append(line)
    return outputArr

puzzleInput = readInput()
counter = 0
for password in puzzleInput:
    splitString = password.split(": ")
    numbersAndLetter = splitString[0].split(" ")
    numbers = numbersAndLetter[0].split("-")

    if(splitString[1][int(numbers[0])] == numbersAndLetter[1] or splitString[1][int(numbers[1])] == numbersAndLetter[1]):
        counter += 1

print(counter)