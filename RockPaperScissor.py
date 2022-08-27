from random import randint
from time import sleep

option_continue = str('y')
while option_continue == 'y' or option_continue == 'Y':
    print('=-=' * 5 + ' Rock, Paper, Scissor ' + '=-=' * 5 + '-=')
    print(' ' * 19 + ' Game Options ')
    print('''                    { 1 } - Rock
                    { 2 } - Paper
                   { 3 } - Scissor''')
    print('=-=' * 18)
    option_value_player = str()
    option_value_computer = str()
    user_option_select = int(input('Choose your option: '))
    while user_option_select != 1 and user_option_select != 2 and user_option_select != 3:
        print('ERROR: Invalid option selected.')
        user_option_select = int(input('Choose your option again: '))
    if user_option_select == 1:
        option_value_player = 'Rock'
    elif user_option_select == 2:
        option_value_player = 'Paper'
    elif user_option_select == 3:
        option_value_player = 'Scissor'
    computer_option_select = randint(1, 3)
    if computer_option_select == 1:
        option_value_computer = 'Rock'
    elif computer_option_select == 2:
        option_value_computer = 'Paper'
    elif computer_option_select == 3:
        option_value_computer = 'Scissor'
    print('Rock')
    sleep(1)
    print('Paper')
    sleep(1)
    print('Scissor!')
    sleep(0.3)
    print('=-=' * 18)
    if user_option_select == computer_option_select:  # Player and Computer chosen the same option.
        print(' ' * 15 + f'Computer chosen {option_value_computer}.')
        print(' ' * 15 + f'Player chosen {option_value_player}.')
        print('=-=' * 18)
        print(' ' * 20 + 'DRAW GAME!')
    elif user_option_select == 1 and computer_option_select == 3:  # Player chosen Rock, Computer chosen Scissor.
        print(' ' * 15 + f'Computer chosen {option_value_computer}.')
        print(' ' * 15 + f'Player chosen {option_value_player}.')
        print('=-=' * 18)
        print(' ' * 20 + 'PLAYER WINS!')
    elif user_option_select == 1 and computer_option_select == 2:  # Player chosen Rock, Computer chosen Paper.
        print(' ' * 15 + f'Computer chosen {option_value_computer}.')
        print(' ' * 15 + f'Player chosen {option_value_player}.')
        print('=-=' * 18)
        print(' ' * 20 + 'COMPUTER WINS!')
    elif user_option_select == 2 and computer_option_select == 1:  # Player chosen Paper, Computer chosen Rock.
        print(' ' * 15 + f'Computer chosen {option_value_computer}.')
        print(' ' * 15 + f'Player chosen {option_value_player}.')
        print('=-=' * 18)
        print(' ' * 20 + 'PLAYER WINS!')
    elif user_option_select == 2 and computer_option_select == 3:  # Player chosen Paper, Computer chosen Scissor.
        print(' ' * 15 + f'Computer chosen {option_value_computer}.')
        print(' ' * 15 + f'Player chosen {option_value_player}.')
        print('=-=' * 18)
        print(' ' * 20 + 'COMPUTER WINS!')
    elif user_option_select == 3 and computer_option_select == 1:  # Player chosen Scissor, Computer chosen Rock.
        print(' ' * 15 + f'Computer chosen {option_value_computer}.')
        print(' ' * 15 + f'Player chosen {option_value_player}.')
        print('=-=' * 18)
        print(' ' * 20 + 'COMPUTER WINS!')
    elif user_option_select == 3 and computer_option_select == 2:  # Player chosen Scissor, Computer chosen Paper.
        print(' ' * 15 + f'Computer chosen {option_value_computer}.')
        print(' ' * 15 + f'Player chosen {option_value_player}.')
        print('=-=' * 18)
        print(' ' * 20 + 'PLAYER WINS')
    option_continue = str(input('Play Again? (Y/N): '))
    if option_continue != 'y' and option_continue != 'Y' and option_continue != 'n' and option_continue != 'N':
        print('ERROR: Invalid Option')
        option_continue = str(input('Play Again? (Y/N): '))
print('Thanks for playing!')
sleep(3)
