import random

computer = input('Do you want to play against a computer? YES or NO? (Y/N): ').lower()


def play_computer():
    print('playing computer')

def play_human():
    print('playing human')


while True:
    if computer == 'y' or 'yes':
        play_computer()
        break
    elif computer == 'n' or 'no':
        play_human()
        break
    else:
        computer = input('Do you want to play against a computer? (Y/N)').lower()
        continue
        