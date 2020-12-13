def parse_input():
    lines = open("input.txt").read().split("\n")
    return lines

inputLines = parse_input()
earliest = int(inputLines[0])
buses = inputLines[1].split(",")

difference = 1000
budID = 0
for bus in buses:
    if(bus != "x"):
        counter = 0
        while counter < earliest:
            counter += int(bus)
        
        if(counter - earliest < difference):
            difference = counter - earliest
            busID = int(bus)

print(difference * busID)