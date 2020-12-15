def parse_input():
    lines = open("input.txt").read().split(",")
    tempDict = {}
    for i, line in enumerate(lines[:-1]):
        tempDict[int(line)] = i + 1
    return tempDict, int(lines[-1]), tempDict[int(lines[-2])] + 2

words_dict, last_spoken, current_turn = parse_input()
while current_turn != 2021:
    if last_spoken in words_dict:
        new_number = current_turn - 1 - words_dict[last_spoken]
    else:
        new_number = 0
    words_dict[last_spoken] = current_turn - 1
    last_spoken = new_number
    current_turn += 1

print(last_spoken)