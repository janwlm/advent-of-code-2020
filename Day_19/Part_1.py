import re

def parse_input():
    with open("input.txt") as file:
        return list(map(lambda x: x.strip(), file.readlines()))

def create_regex(r="0"):
    if rules[r][0][0][0] == '"':
        return rules[r][0][0].strip('"')
    return "(" + "|".join(["".join([create_regex(sub) for sub in subrule]) for subrule in rules[r]]) + ")"

puzzle_input = parse_input()
split_index = puzzle_input.index("")
raw_rules = puzzle_input[:split_index]
messages = puzzle_input[split_index+1:]

rules = dict()
for rule in raw_rules:
    num, r = rule.split(": ")
    rules[num] = [s.split() for s in r.split(" | ")]

reg = re.compile(create_regex())
result = [reg.fullmatch(message) for message in messages]
result = len([x for x in result if x != None])

print(result)