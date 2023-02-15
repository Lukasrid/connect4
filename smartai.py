import random
import time


print('\nWelcome to Connect 4!\n')
time.sleep(1)
computer = input('Do you want to play against a computer? YES or NO? (Y/N): ').lower()

HUMAN = '🔴'
COMPUTER = '🟡'
EMPTY = '⚪'
C1 = '1️⃣ '
C2 = '2️⃣ '
C3 = '3️⃣ '
C4 = '4️⃣ '
C5 = '5️⃣ '
C6 = '6️⃣ '
C7 = '7️⃣'

board = [[EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
         [C1, C2, C3, C4, C5, C6, C7]]


ROWS = 8
COLUMNS = 7




def print_board():
    '''
    Prints out the game board
    '''
    for row in range(1, ROWS):
        for col in range(0, COLUMNS):
            print(board[row][col], end=' ')
        print(" ")


def validate_input(col, player):
    '''
    Chacks that the input entered is a number between 1-7 and that it is an integer in base 10
    '''
    while True:
            '''
            Checks that the input is an integer
            '''
            try:
                col = int(input(f'\n{player} Enter a column number between 1-7: '))
                break
            except ValueError as e:
                print(f'\nThat is an {e} is not a number. Please try again.\n')
    while col < 1 or col > 7:
        try:
            col = int(input(f'\nColumn number {col} does not exist. Please enter a column number between 1-7: \n'))
            continue
        except ValueError as e:
            print(f'\nThat is an {e} is not a number. Please try again.')
            col = int(input('Enter a coloumn number between 1-7: \n'))
            continue
    return col


def is_valid_location(board, col):
	return board[ROWS-1][col] == EMPTY


def get_next_open_row(board, col):
	for r in range(ROWS):
		if board[r][col] == EMPTY:
			return r


def drop_piece(board, row, col, player):
	board[row][col] = player


def score_position(board, player):
    score = 0
    for r in range(ROWS):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(COLUMNS-3):
            window = row_array[c:c+4]

            if window.count(player) == 4:
                score+= 100
            elif window.count(player) == 3 and window.count(EMPTY) == 1:
                score += 10

    return score


def get_valid_locations(board):
	valid_locations = []
	for col in range(COLUMNS):
		if is_valid_location(board, col):
			valid_locations.append(col)
	return valid_locations


def pick_best_move(board, player):
    valid_locations = get_valid_locations(board)
    print(valid_locations)
    best_score = 0
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(board, row, col, player)
        score = score_position(temp_board, player)
        if score > best_score:
            best_score = score
            best_col = col
    return best_col

def place_chip_computer(col, player):
    '''
    Places chip in the first empty slot from the bottom in a column and does not allow the computer to place a chip in a full column
    '''
    col = col - 1
        

    for rows in range(ROWS-1, -1, -1):
        if board[rows][col] == EMPTY:
            board[0][col] = EMPTY
            if [rows] == [0]:
                col = random.randint(1, 7)
                place_chip_computer(col, player)
                break             
            board[rows][col] = player
            print(f'Computer chose column number {col+1}')
            break
    

def place_chip_human(col, player):
    '''
    Places chip in the first empty slot from the bottom in a column and checks whether that column is full
    '''
    col = col - 1

    
    for rows in range(ROWS-1, -1, -1):
        if board[rows][col] == EMPTY:
            if [rows] == [0]:
                col = 0 
                print(f'\nColumn number {col+1} is full. Please choose a different column.\n')
                col = validate_input(col, player)
                place_chip_human(col, player)            
            board[rows][col] = player
            board[0][col] = EMPTY
            break


def horizontal_win():
    '''
    Checks for 4 in a row in the horizontal direction
    '''
    for c in range(0, 4):
        for r in range(1, ROWS):
            if board[r][c] != EMPTY:
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
        for r in range(1, 4):
            if board[r][c] != EMPTY:
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
        for r in range(4, ROWS):
            if board[r][c] != EMPTY:
                if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3]:
                    print_board()
                    print('\nPlayer', board[r][c], 'won!')
                    return True

    #Going to the right and down, negative slope (\)
    for c in range(0, 4):
        for r in range(1, 4):
            if board[r][c] != EMPTY:
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
    

def play_computer():
    '''
    Plays the game with one human player and one unintelligent computer player
    '''
    player = random.choice([HUMAN, COMPUTER])
    print(f'\nYour are {HUMAN}.\n')
    time.sleep(2)
    print(f'{player} Starts the game.')
    time.sleep(2)
    col = 0
    while not win():
        '''
        Kepps playing the game until one of the win criteria is fulfilled
        '''
        print(' ')
        print_board()
        if player == HUMAN:
            if EMPTY not in board[1]:
                print('\nThe game is a draw!\n')
                break
            col = validate_input(col, player)
            place_chip_human(col, player)
        elif player == COMPUTER:
            if EMPTY not in board[1]:
                print('\nThe game is a draw!\n')
                break
            print('\nComputer is thinking...\n')
            time.sleep(random.randint(1, 2))
            col = pick_best_move(board, player)
            #col = random.randint(1, 7)
            place_chip_computer(col, player)            
            

        if player == HUMAN:
            player = COMPUTER

        else:
            player = HUMAN
        

def play_human():
    '''
    Plays the game with two human players
    '''
    player = random.choice([HUMAN, COMPUTER])
    print(f'\n Player {player} starts the game.')
    time.sleep(2)
    col = 0
    while not win():
        '''
        Kepps playing the game until one of the win criteria is fulfilled
        '''
        print('')
        print_board()
        if EMPTY not in board[1]:
                print('\nThe game is a draw. You both suck...\n\n\n\n\n\nbye.\n\n\n\n')
                break
        col = validate_input(col, player)
        place_chip_human(col, player)
        if player == HUMAN:
            player = COMPUTER
        else: player = HUMAN
        

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