import random

computer = input('Do you want to play against a computer? YES or NO? (Y/N): ').lower()


def play_computer():
    print('playing computer')

def play_human():
    print('playing human')


while True:
    if computer in ('yes', 'y'):
        play_computer()
        break
    elif computer in ('no', 'n'):
        play_human()
        break
    else:
        computer = input('Please enter YES or NO / Y or N: ').lower()
        continue