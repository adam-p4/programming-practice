# Given a completed sudoku board, asserts if the board configuration is legal or not.


def done_or_not(board): #board[i][j]
    for row in board: # test rows
        if set([i for i in row]) != set(range(1,10)):
            return 'Try again!'
        
    for i in range(9): # test cols
        if set([row[i] for row in board]) != set(range(1,10)):
            return 'Try again!'
        
    for i in [0, 3, 6]: # test squares
        for j in [0, 3, 6]:
            if set([board[i][j], board[i+1][j], board[i+2][j],
                     board[i+1][j+1], board[i+1][j+2], board[i+2][j+1],
                       board[i+2][j+2], board[i][j+1], board[i][j+2]]) != set(range(1,10)):
                return 'Try again!'

    return 'Finished!'




# Test
board =                 [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]

print(done_or_not(board))