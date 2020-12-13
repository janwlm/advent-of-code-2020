def parse_input():
    lines = open("input.txt").read().split("\n")
    buses = []
    for idx, bus in enumerate(lines[1].split(",")):
        if(bus != "x"):
            buses.append([int(bus), idx])
    return buses

def merge_buses1(buses, remainder):
    # Combine the two first buses into one bus
    value = buses[0]
    while True:
        correct = True
        if(value%int(buses[0]) != 0 or (value + remainder)%int(buses[1]) != 0):
            correct = False

        if(correct):
            return [value, buses[0]*buses[1]]
        else:
            value += buses[0]

def merge_buses2(bus, remainder, start, increment):
    # Calculate first correct value
    value = start
    working_value = 0
    while True:
        correct = True
        if((value + remainder)%int(bus) != 0):
            correct = False

        if(correct):
            working_value = value
            break
        else:
            value += increment
    
    # Look for repetition (loop) and return difference bewteen each repetition
    value = working_value + increment
    while True:
        correct = True
        if((value + remainder)%int(bus) != 0):
            correct = False

        if(correct):
            return [working_value, value - working_value]
        else:
            value += increment

buses = parse_input()
new_bus = []
pointer = 0
while pointer < len(buses):
    if(pointer != 0):
        new_bus = merge_buses2(buses[pointer][0], buses[pointer][1], new_bus[0], new_bus[1])
        pointer += 1
    else:
        new_bus = merge_buses1([buses[pointer][0], buses[pointer + 1][0]], buses[pointer + 1][1] - buses[pointer][1])
        pointer += 2

print(new_bus[0])