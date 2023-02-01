
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

"""
def placed_chip(col, player):
    '''
    Places chip in the first empty slot from the bottom in a column
    '''
    col = col - 1
    for rows in range(ROWS-1, -1, -1):
        if board[rows][col] == '⚪':"""

print_board()