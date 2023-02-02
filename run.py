
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

'''
def validate_input(x):
    while True:
        if x < 1:
            x = int(input(f'Column {x} does not exist. Please choose column 1-7: '))
        elif x > 7:
            x = int(input(f'Column {x} does not exist. Please choose column 1-7: '))
        else:
            break
    return x
'''


def horizontal_win():
    '''
    Checks for 4 in a row in the horizontal direction
    '''
    for c in range(0, 4):
        for r in range(0, ROWS):
            if board[r][c] != '⚪':
                if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3]:
                    print_board()
                    print('Player', board[r][c], 'won!')
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
                    print('Player', board[r][c], 'won!')
                    return True
    return False


def diagonal_win():
    return False


def win():
    if horizontal_win() or vertical_win() or diagonal_win():
        return True


def validate_input(x):
    while x < 1 or x > 7:
        x = int(input(f'Coloumn number {x} does not exist. Please enter a coloumn number between 1-7: '))
        continue
    return x

player = '🔴'
while not win():
    print_board()
    while True:
        try:
            x = int(input('Enter a coloumn number between 1-7: '))
            break
        except ValueError as e:
            print(f'That is an {e} is not a number. Please try again.')
    x = validate_input(x)
    place_chip(x, player)
    if player == '🔴':
        player = '🟡'
    else: player = '🔴'
