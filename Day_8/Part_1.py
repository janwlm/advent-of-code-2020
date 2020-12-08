def readInput():
    inputLines = open("input.txt", "r").readlines()
    newLines = []
    for line in inputLines:
        newLines.append((line.strip() + " False").split(" "))
    return newLines

pointer = 0
accumulator = 0
memory = readInput()
while True:
    if(memory[pointer][2] == "True"):
        print(accumulator)
        break

    if(memory[pointer][0] == "acc"):
        accumulator += int(memory[pointer][1])
        memory[pointer][2] = "True"
        pointer += 1
    elif(memory[pointer][0] == "jmp"):
        memory[pointer][2] = "True"
        pointer += int(memory[pointer][1])
    elif(memory[pointer][0] == "nop"):
        memory[pointer][2] = "True"
        pointer += 1