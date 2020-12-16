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
        fields.append([[int(i.split(": ")[1].split(" or ")[0].split("-")[0]), int(i.split(": ")[1].split(" or ")[0].split("-")[1])], [int(i.split(": ")[1].split(" or ")[1].split("-")[0]), int(i.split(": ")[1].split(" or ")[1].split("-")[1])]])
    return my_ticket, nearby_tickets, fields

def check_validity(ticket, fields):
    invalid = []
    for i in ticket:
        check = False
        for x in fields:
            if((int(i) >= x[0][0] and int(i) <= x[0][1]) or (int(i) >= x[1][0] and int(i) <= x[1][1])):
                check = True
        if(not check):
            invalid.append(int(i))
    if(invalid):
        return False, invalid
    else:
        return True, 0

my_ticket, nearby_tickets, fields = parse_input()
wrong_numbers = []
for ticket in nearby_tickets:
    valid, invalid = check_validity(ticket, fields)
    if(not valid):
        for i in invalid: 
            wrong_numbers.append(i)

print(sum(wrong_numbers))