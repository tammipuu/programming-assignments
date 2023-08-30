import random

number_of_player = 0
number_of_computer = 0

while True:
    number_of_player = int(input('Syötä luku: '))
    number_of_computer = random.randint(1, 10)
    if number_of_computer < number_of_player:
        print('Liian pieni arvaus')
    elif number_of_computer == number_of_player:
        print('Oikein')
        break
    elif number_of_computer > number_of_player:
        print('Liian suuri arvaus')
