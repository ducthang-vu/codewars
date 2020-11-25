# Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter. If the board is valid return
# 'Finished!', otherwise return 'Try again!'


def done_or_not(board):
    rows = [set(row) for row in board]
    columns = [set([row[y] for row in board]) for y in range(0, 9)]
    regions = [set([row[y] for y in range(3 * a, 3 + 3 * a) for row in board[3 * z: 3 * z + 3]]) for a in range(2) for z
               in range(2)]
    array = rows + columns + regions
    return 'Finished!' if all(combo == set([i for i in range(1, 10)]) for combo in array) else 'Try again!'


# SOLUTION:
# import numpy as np
# def done_or_not(aboard): #board[i][j]
#   board = np.array(aboard)
#
#   rows = [board[i,:] for i in range(9)]
#   cols = [board[:,j] for j in range(9)]
#   sqrs = [board[i:i+3,j:j+3].flatten() for i in [0,3,6] for j in [0,3,6]]
#
#   for view in np.vstack((rows,cols,sqrs)):
#       if len(np.unique(view)) != 9:
#           return 'Try again!'
#
#   return 'Finished!'