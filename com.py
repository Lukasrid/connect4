import random


print('\nWelcome to Connect 4!\nPlayer 🔴 starts the game.\n')
computer = input('Do you want to play against a computer? YES or NO? (Y/N): ').lower()

board = [['⚪', '⚪', '⚪', '⚪', '⚪', '⚪', '⚪'],
         ['⚪', '⚪', '⚪', '⚪', '⚪', '⚪', '⚪'],
         ['⚪', '⚪', '⚪', '⚪', '⚪', '⚪', '⚪'],
         ['⚪', '⚪', '⚪', '⚪', '⚪', '⚪', '⚪'],
         ['⚪', '⚪', '⚪', '⚪', '⚪', '⚪', '⚪'],
         ['⚪', '⚪', '⚪', '⚪', '⚪', '⚪', '⚪'],
         ['1️⃣ ', '2️⃣ ', '3️⃣ ', '4️⃣ ', '5️⃣ ', '6️⃣ ', '7️⃣']]


ROWS = 7
COLUMNS = 7


def print_board():
    '''
    Prints out the game board
    '''
    for row in range(0, ROWS):
        for col in range(0, COLUMNS):
            print(board[row][col], end=' ')
        print(" ")


def place_chip(col, player):
    '''
    Places chip in the first empty slot from the bottom in a column
    '''
    col = col - 1
    for rows in range(ROWS-1, -1, -1):
        if board[rows][col] == '⚪':
            board[rows][col] = player
            break


def horizontal_win():
    '''
    Checks for 4 in a row in the horizontal direction
    '''
    for c in range(0, 4):
        for r in range(0, ROWS):
            if board[r][c] != '⚪':
                if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3]:
                    print_board()
                    print('\nPlayer', board[r][c], 'won!')
                    return True
    return False


def vertical_win():
    '''
    Checks for 4 in a row in the vertical direction
    '''
    for c in range(0, COLUMNS):
        for r in range(0, 3):
            if board[r][c] != '⚪':
                if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c]:
                    print_board()
                    print('\nPlayer', board[r][c], 'won!')
                    return True
    return False


def diagonal_win():
    '''
    Checks for 4 in a row in both diagonal directions
    '''
    # Going to the right and up, positive slope (/)
    for c in range(0, 4):
        for r in range(3, ROWS):
            if board[r][c] !='⚪':
                if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3]:
                    print_board()
                    print('\nPlayer', board[r][c], 'won!')
                    return True

    #Going to the right and down, negative slope (\)
    for c in range(0, 4):
        for r in range(0, 3):
            if board[r][c] !='⚪':
                if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3]:
                    print_board()
                    print('\nPlayer', board[r][c], 'won!')
                    return True
    return False


def win():
    '''
    Checks if any winning direction has one and end the game 
    '''
    if horizontal_win() or vertical_win() or diagonal_win():
        return True


def validate_input(x):
    '''
    Chacks that the input entered is a number between 1 and 7
    '''
    while x < 1 or x > 7:
        try:
            x = int(input(f'\nColumn number {x} does not exist. Please enter a column number between 1-7: \n'))
            continue
        except ValueError as e:
            print(f'\nThat is an {e} is not a number. Please try again.')
            x = int(input('Enter a coloumn number between 1-7: \n'))
            continue
    return x

def play_computer():
    '''
    Plays the game with one human player and one unintelligent computer player
    '''
    player = '🔴'
    while not win():
        '''
        Kepps playing the game until one of the win criteria is fulfilled
        '''
        print_board()
        while True:
            '''
            Checks that the input is an integer
            '''
            try:
                x = int(input('\nEnter a coloumn number between 1-7: \n'))
                break
            except ValueError as e:
                print(f'\nThat is an {e} is not a number. Please try again.\n')
        x = validate_input(x)
        place_chip(x, player)
        
        
        if player == '🔴':
            player = '🟡'
        else: player = '🔴'

        if player == '🟡':
            place_chip(random.randint(1, 7), player)
            player = '🔴'
        


def play_human():
    '''
    Plays the game with two human players
    '''
    player = '🔴'
    while not win():
        '''
        Kepps playing the game until one of the win criteria is fulfilled
        '''
        print_board()
        while True:
            '''
            Checks that the input is an integer
            '''
            try:
                x = int(input('\nEnter a coloumn number between 1-7: \n'))
                break
            except ValueError as e:
                print(f'\nThat is an {e} is not a number. Please try again.\n')
        x = validate_input(x)
        place_chip(x, player)
        if player == '🔴':
            player = '🟡'
        else: player = '🔴'

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