import random

cash = 1000


def create_winning_numbers():
    winning_numbers = set()
    while len(winning_numbers) < 6:
        winning_numbers.add(random.randint(1, 22))
    return winning_numbers


def buy_lottery_ticket():
    global cash
    cash -= 50
    chosen_numbers = input('Please, enter your 6 numbers from 1 to 22 separated by ",": ')
    chosen_numbers_list = chosen_numbers.split(',')
    ticket_numbers = {int(i) for i in chosen_numbers_list}
    return ticket_numbers


def draw_results(ticket_numbers, winning_numbers):
    print('Winning numbers are {}' .format(winning_numbers))
    matched_numbers = ticket_numbers.intersection(winning_numbers)
    prizes = [0, 0, 10, 50, 250, 1500, 6000]
    prize = prizes[len(matched_numbers)]
    if prize > 0:
        global cash
        cash += prize
        return 'You matched {} numbers! You just won {}$!' .format(len(matched_numbers), prize)
    else:
        return 'No luck this time. Try again!'

def run():
    while True:
        msg = input('Welcome to Lottery house! Here everyone can be a winner!\nDo you want to [b]uy ticket, [c]heck or [l]eave?')
        if msg == 'b':
            ticket_numbers = buy_lottery_ticket()
            winning_numbers = create_winning_numbers()
            results = draw_results(ticket_numbers,winning_numbers)
            print(results)
        elif msg == 'c':
            print(cash)
        elif msg == 'l':
            break
run()