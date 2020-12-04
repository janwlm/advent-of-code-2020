import re

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

presentPassports = []
for passport in filteredInput:
    counter = 0
    for entry in passport:
        keyAndValue = entry.split(":")
        if(keyAndValue[0] != "cid"):
            counter += 1
    if(counter == 7):
        presentPassports.append(passport)

patternHcl = re.compile("[a-f0-9]+")
patternPid = re.compile("[0-9]+")
result = 0
for passport in presentPassports:
    counter = 0
    for entry in passport:
        keyAndValue = entry.split(":")
        key = keyAndValue[0]
        value = keyAndValue[1]
        if(key == "byr"):
            if(int(value) >= 1920 and int(value) <= 2002):
                counter += 1
        elif(key == "iyr"):
            if(int(value) >= 2010 and int(value) <= 2020):
                counter += 1
        elif(key == "eyr"):
            if(int(value) >= 2020 and int(value) <= 2030):
                counter += 1
        elif(key == "hgt"):
            if(value[-2:] == "cm"):
                if(int(value.replace("cm", "")) >= 150 and int(value.replace("cm", "")) <= 193):
                    counter += 1
            elif(value[-2:] == "in"):
                if(int(value.replace("in", "")) >= 59 and int(value.replace("in", "")) <= 76):
                    counter += 1
        elif(key == "hcl"):
            if(value[0] == "#"):
                if(patternHcl.fullmatch(value[-6:]) != None):
                    counter += 1
        elif(key == "ecl"):
            if(value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth"):
                counter += 1
        elif(key == "pid"):
            if(len(value) == 9 and patternPid.fullmatch(value) != None):
                counter += 1
    if(counter == 7):
        result += 1
print(result)