""" Tic-Tac-Toe Checker """

'''
If we were to set up a Tic-Tac-Toe game, we would 
want to know whether the board's current state is solved, 
wouldn't we? Our goal is to create a function 
that will check that for us!

Assume that the board comes in the form of a 3x3 array, 
where the value is 0 if a spot is empty, 
1 if it is an "X", or 2 if it is an "O", 
like so:
[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
We want our function to return:
-1 if the board is not yet finished AND no one has won yet 
                                    (there are empty spots);
1 if "X" won;
2 if "O" won;
0 if it's a cat's game (i.e. a draw).
You may assume that the board passed in is valid 
in the context of a game of Tic-Tac-Toe.
'''

# MY SOLUTION 1:
# =====================================================

board = [[2, 1, 1],
       [1, 2, 2],
       [1, 2, 1]]


def finish_test(board):
    for i in board:
        if 0 in i:
            return -1
    return 0


def h_test(board):
    res = 0
    for i in board:
        if i[0] == i[1] == i[2] == 1:
            res = 1
        if i[0] == i[1] == i[2] == 2:
            res = 2
    return res


def v_test(board):
    lst2 = [[r[i] for r in board] for i in range(3)]
    return h_test(lst2)


def d1_test(board):
    res = 0
    if board[0][0] == board[1][1] == board[2][2] == 1:
        res = 1
    if board[0][0] == board[1][1] == board[2][2] == 2:
        res = 2
    return res


def d2_test(board):
    res = 0
    if board[0][2] == board[1][1] == board[2][0] == 1:
        res = 1
    if board[0][2] == board[1][1] == board[2][0] == 2:
        res = 2
    return res


def result(res):
    if 1 in res:
        return 1
    if 2 in res:
        return 2
    if -1 in res:
        return -1
    return 0


def is_solved(board):
    res = (h_test(board), v_test(board), d1_test(board), d2_test(board), finish_test(board))
    return result(res)


print(is_solved(board))


# THE BEST SOLUTION:
# ===================================================

import itertools


def is_solved2(board):
    b = list(itertools.chain(*board))
    for p, q, r in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if b[p] == b[q] == b[r] != 0: return b[p]
    return 0 if sum(b) == 13 else -1


print(is_solved2(board))
