import copy

def readInput():
    inputLines = open("input.txt", "r").readlines()
    newLines = []
    for line in inputLines:
        newLines.append((line.strip() + " False").split(" "))
    return newLines

def runProgram(newMemory):
    pointer = 0
    accumulator = 0
    memory = newMemory
    while True:
        if(pointer >= len(memory)):
            return True, accumulator

        if(memory[pointer][2] == "True"):
            return False, accumulator

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

freshMemory = readInput()
end = False
for i in range(len(freshMemory)):
    if(freshMemory[i][0] == "nop"):
        newMemory = copy.deepcopy(freshMemory)
        newMemory[i][0] = "jmp"
        end, accumulator = runProgram(newMemory)
    elif(freshMemory[i][0] == "jmp"):
        newMemory = copy.deepcopy(freshMemory)
        newMemory[i][0] = "nop"
        end, accumulator = runProgram(newMemory)
    
    if(end):
        print(accumulator)