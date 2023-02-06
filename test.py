import random
import time


print('\nWelcome to Connect 4!\nPlayer 🔴 starts the game.\n')
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


def is_valid_location(board, col):
	return board[ROW_COUNT-1][col] == EMPTY

def get_next_open_row(board, col):
	for r in range(ROW_COUNT):
		if board[r][col] == EMPTY:
			return r

def drop_piece(board, row, col, piece):
	board[row][col] = piece


def validate_input(x):
    '''
    Chacks that the input entered is a number between 1-7 and that it is an integer in base 10
    '''
    while True:
            '''
            Checks that the input is an integer
            '''
            try:
                x = int(input('\nEnter a column number between 1-7: \n'))
                break
            except ValueError as e:
                print(f'\nThat is an {e} is not a number. Please try again.\n')
    while x < 1 or x > 7:
        try:
            x = int(input(f'\nColumn number {x} does not exist. Please enter a column number between 1-7: \n'))
            continue
        except ValueError as e:
            print(f'\nThat is an {e} is not a number. Please try again.')
            x = int(input('Enter a coloumn number between 1-7: \n'))
            continue
    return x


def place_chip(col, player):
    '''
    Places chip in the first empty slot from the bottom in a column and checks whether that column is full
    '''
    col = col - 1

    
    for rows in range(ROWS-1, -1, -1):
        if board[rows][col] == EMPTY:
            if [rows] == [0]:
                x = 0
                print(f'\nColumn number {col+1} is full. Please choose a different column.\n')
                if player == COMPUTER:
                    #x = random.randint(1, 7)
                    x = pick_best_move(board, COMPUTER)
                    place_chip(x, player)
                x = validate_input(x)
                place_chip(x, player)            
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


def score_position(board, piece):
    score = 0
    for r in range(ROWS):
        row_array = [int(i) for i in list(board)[r,:]]
        for c in range(COLUMNS-3):
            window = row_array[c:c+4]
            if window.count(piece) == 4:
                score += 100
            elif window.count(piece) == 3 and window.count(EMPTY) == 1:
                score += 10
    return score

def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMNS):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations
    

def pick_best_move(board, piece):
    
    valid_locations = get_valid_locations(board)
    best_score = 0
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, piece)
        score = score_position(temp_board, piece)
        if score > best_score:
            best_score = score
            best_col = col

    return best_col

   

def play_computer():
    '''
    Plays the game with one human player and one unintelligent computer player
    '''
    player = HUMAN
    x = 0
    while not win():
        '''
        Kepps playing the game until one of the win criteria is fulfilled
        '''
        print_board()
        x = validate_input(x)
        place_chip(x, player)
        print_board()
        
        
        if player == HUMAN:
            player = COMPUTER

        if player == COMPUTER:
            if win():
                return
            print('\nComputer is thinking...\n')
            time.sleep(random.randint(1, 2))
            x = random.randint(1, 7)
            place_chip(x, player)
            print(f'Computer chose column number {x}\n')
            player = HUMAN
        


def play_human():
    '''
    Plays the game with two human players
    '''
    player = HUMAN
    x = 0
    while not win():
        '''
        Kepps playing the game until one of the win criteria is fulfilled
        '''
        print_board()
        x = validate_input(x)
        place_chip(x, player)
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