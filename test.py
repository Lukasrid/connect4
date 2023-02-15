y = [8]
print(y[0])

board = [[0, 0, 0],
         [0, 0, 0],
         [1, 0, 0]]
ROWS = 3
def ai():
    for c in range(0, 4):
        for r in range(1, ROWS):
            if 1 == board[r][c]:
                print(board[r][c])

ai()