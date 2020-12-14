def parse_input():
    lines = open("input.txt").read().split("\n")
    tempArr = []
    for line in lines:
        tempArr.append(line.split(" = "))
    return tempArr

def get_floating_addresses(addr):
    i = addr.find('X')
    if i == -1:
        return [addr]
    option1 = get_floating_addresses(addr[:i] + '0' + addr[i + 1:])
    option2 = get_floating_addresses(addr[:i] + '1' + addr[i + 1:])
    return option1 + option2

memory  = {}
mask = ""
for operation in parse_input():
    if(operation[0] == "mask"):
        mask = operation[1]
    elif(operation[0][:3] == "mem"):
        address = int(operation[0].split("[")[1][:-1])
        bin_address = "{0:b}".format(address).zfill(36)
        result = ""
        for i, j in enumerate(bin_address):
            if(mask[i] == "0"):
                result += j
            else:
                result += mask[i]

        for i in get_floating_addresses(result):
            memory[int("".join(str(x) for x in i), 2)] = int(operation[1])

print(sum(memory.values()))