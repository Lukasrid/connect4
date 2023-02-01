
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


def win():
    return False

player = '🔴'
while not win():
    print_board()
    x = int(input('Enter a column: '))
    place_chip(x, player)
    print_board()
    if player == '🔴':
        player = '🟡'
    else: player = '🔴'

'''
def play_game():
    print_board()
    x = int(input('Player 1 select a column(1-7): '))
    #validate_input(x)
    place_chip(x , '🔴')
    print_board()


play_game()
'''