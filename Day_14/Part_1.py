def parse_input():
    lines = open("input.txt").read().split("\n")
    tempArr = []
    for line in lines:
        tempArr.append(line.split(" = "))
    return tempArr

memory  = {}
mask = ""
for operation in parse_input():
    if(operation[0] == "mask"):
        mask = operation[1]
    elif(operation[0][:3] == "mem"):
        address = int(operation[0].split("[")[1][:-1])
        bin_value = "{0:b}".format(int(operation[1])).zfill(36)
        result = ""
        for i, j in enumerate(bin_value):
            if(mask[i] == "X"):
                result += j
            else:
                result += mask[i]
        memory[address] = int("".join(str(x) for x in result), 2)

print(sum(memory.values()))