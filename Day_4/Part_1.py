def readInput():
    return open("input.txt", "r").readlines()

filteredInput = []
tempStr = ""
for element in readInput():
    if(element.strip() != ""):
        if(tempStr != "" and tempStr[-1] != " "):
            tempStr += " " 
        tempStr += element.strip()
    else:
        filteredInput.append(tempStr.split(" "))
        tempStr = ""
filteredInput.append(tempStr.split(" "))

result = 0
for passport in filteredInput:
    counter = 0
    for entry in passport:
        keyAndValue = entry.split(":")
        if(keyAndValue[0] != "cid"):
            counter += 1
    if(counter >= 7):
        result += 1
print(result)