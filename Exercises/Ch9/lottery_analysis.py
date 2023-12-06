from random import choice


def generate_ticket(lottery):
    """generates a random ticket from given lottery list of letters & numbers"""
    ticket = []

    while len(ticket) < 4:
        temp = choice(lottery)
        if temp not in ticket:
            ticket.append(temp)

    return ticket


def check_ticket(some_ticket, winning_ticket):
    """checks if some_ticket is the winning_ticket"""
    for temp in some_ticket:
        if temp not in winning_ticket:
            return False

    return True


lottery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']
print('\nDrawing the Winning Ticket...\n')
winning_ticket = generate_ticket(lottery)
print(f'Winning Ticket is {winning_ticket}')
times = 0
limit = 1_000_000
flag = False

while not flag:
    new_ticket = generate_ticket(lottery)
    times += 1
    if times % 1000 == 0:
        print(f'crossed {times} tries.')
    flag = check_ticket(new_ticket, winning_ticket)
    if times >= limit:
        break

if flag:
    print(f'\nWon the prize in {times} tries with {winning_ticket} ticket.')
else:
    print(f'\nLost after {times} tries, winning ticket is {winning_ticket}.')
