import copy

def parse_input():
    lines = open("input.txt").read().split("\n")
    tempArr = []
    for line in lines:
        tempArr.append(list(line.replace(" ", "")))
    return tempArr

def different_calculation(expression):
    tempStr = ""
    expressionArr = []
    for j, i in enumerate(expression):
        if(i != "+" and i != "*"):
            if(j != len(expression) - 1 and (expression[j+1] != "+" and expression[j+1] != "*")):
                tempStr += i
            else:
                tempStr += i
                expressionArr.append(tempStr)
                tempStr = "" 
        else:
            tempStr += i
            expressionArr.append(tempStr)
            tempStr = ""

    while True:
        if "+" in expressionArr or "*" in expressionArr:
            last_part = []
            for i in range(3, len(expressionArr)):
                last_part.append(expressionArr[i])
            last_part.insert(0, str(eval(expressionArr[0] + expressionArr[1] + expressionArr[2])))
            expressionArr = copy.deepcopy(last_part)
        else:
            break        
    return expressionArr[0]

result = 0
for expression in parse_input():
    while "(" in expression:
        startIndex = 0
        stopIndex = 0
        tempArr = []
        value = ""
        for i, j in enumerate(expression):
            if(j == "("):
                startIndex = i
            elif(j == ")"):
                stopIndex = i
                for i in range(startIndex+1, stopIndex):
                    value += expression[i]
                for a in range(len(expression)):
                    if(a < startIndex):
                        tempArr.append(expression[a])
                    elif(a == startIndex):
                        tempArr.append(different_calculation(value))
                    elif(a > stopIndex):
                        tempArr.append(expression[a])
                expression = copy.deepcopy(tempArr)
                break
    result += int(different_calculation(expression))
print(result)