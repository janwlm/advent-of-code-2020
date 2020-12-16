import copy

def parse_input():
    lines = open("input.txt").read().split("\n\n")
    my_ticket = lines[1].split("\n")[1].split(",")

    raw_nearby_tickets = lines[2].split("\n")[1:]
    nearby_tickets = []
    for i in raw_nearby_tickets:
        nearby_tickets.append(i.split(","))

    raw_fields = lines[0].split("\n")
    fields = []
    for i in raw_fields:
        fields.append([i.split(": ")[0], [int(i.split(": ")[1].split(" or ")[0].split("-")[0]), int(i.split(": ")[1].split(" or ")[0].split("-")[1])], [int(i.split(": ")[1].split(" or ")[1].split("-")[0]), int(i.split(": ")[1].split(" or ")[1].split("-")[1])]])
    return my_ticket, nearby_tickets, fields

def check_validity(ticket, fields):
    for i in ticket:
        check = False
        for x in fields:
            if((int(i) >= x[1][0] and int(i) <= x[1][1]) or (int(i) >= x[2][0] and int(i) <= x[2][1])):
                check = True
        if(not check):
            return False
    return True

my_ticket, nearby_tickets, fields = parse_input()
valid_nearby_tickets = []
for ticket in nearby_tickets:
    if(check_validity(ticket, fields)):
        valid_nearby_tickets.append(ticket)

valid_nearby_tickets.append(my_ticket)
order = [[] for i in range(len(my_ticket))]
for z, ticket in enumerate(valid_nearby_tickets):
    for i, j in enumerate(ticket):
        current_order = []
        for x in fields:
            if((int(j) >= x[1][0] and int(j) <= x[1][1]) or (int(j) >= x[2][0] and int(j) <= x[2][1])):
                if(current_order.count(x[0]) == 0):
                    current_order.append(x[0])
        if(z == 0):
            order[i] = current_order
        else:
            for y in order[i]:
                if(current_order.count(y) == 0):
                    order[i].remove(y)

ruled_out_order = copy.deepcopy(order)
while True:
    worked = False
    for i, j in enumerate(order):
        if(len(j) == 1):
            for x in range(len(order)):
                if(i != x and ruled_out_order[x].count(j[0]) != 0):
                    ruled_out_order[x].remove(j[0])
                    worked = True
    order = copy.deepcopy(ruled_out_order)
    if(not worked):
        break

new_order = []
for i in order:
    new_order.append(i[0])

result = 1
for i, j in enumerate(new_order):
    if "departure" in j:
        result *= int(my_ticket[i])

print(result)