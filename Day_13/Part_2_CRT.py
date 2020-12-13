def parse_input():
    lines = open("input.txt").read().split("\n")
    buses = []
    for bus in lines[1].split(","):
        if(bus != "x"):
            buses.append([int(bus), 0])
        else:
            buses.append("x")
    # Switch index of each element (needed for correct CRT)
    for i, j in enumerate(buses):
        if(j != "x"):
            buses[i][1] = abs(i - (len(buses) - 1))
    tempArr = []
    # Remove all 'x' elements from array
    for i in buses:
        if(i != "x"):
            tempArr.append(i)
    return tempArr

def calculate_z(Ni, mod):
    k = 1
    while True:
        if((Ni*k)%mod == 1):
            return k
        k += 1

buses = parse_input()
# Calculate N
N = 1
for i in buses:
    N *= i[0]

# Calculate Ni and result
result = 0
for i in buses:
    Ni = int(N/i[0])
    result += i[1]*Ni*calculate_z(Ni, i[0])

# Simplyfy result
while result > N:
    result -= N

print(result - buses[0][1])