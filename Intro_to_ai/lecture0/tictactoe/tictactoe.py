"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count_x += 1
            elif board[i][j] == O:
                count_o += 1

    if count_x == count_o:
        return X
    else:
        return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    set_actions = set({})
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                set_actions.add((i, j))
    return set_actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    deep_board = copy.deepcopy(board)
    i, j = action
    if deep_board[i][j] is not None:
        raise Exception("Invalid Action")

    deep_board[i][j] = player(board)

    return deep_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        answer1 = []
        answer2 = []
        for j in range(3):
            answer1.append(board[i][j])
            answer2.append(board[j][i])
        if answer1 == [X, X, X] or answer2 == [X, X, X]:
            return X
        elif answer1 == [O, O, O] or answer2 == [O, O, O]:
            return O

    answer3 = [board[0][0], board[1][1], board[2][2]]
    answer4 = [board[2][0], board[1][1], board[0][2]]

    if answer3 == [X, X, X] or answer4 == [X, X, X]:
        return X
    elif answer3 == [O, O, O] or answer4 == [O, O, O]:
        return O

    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:

        optionsx = []
        max_v = -math.inf
        for action in actions(board):
            deep_board = copy.deepcopy(board)
            k, l = action
            deep_board[k][l] = X
            optionsx.append([action, min_value(deep_board)])
        for i in range(len(optionsx)):
            if optionsx[i][1] >= max_v:
                optimal = optionsx[i][0]
                max_v = optionsx[i][1]
                print(max_v)

        return optimal

    if player(board) == O:
        optionsx = []
        min_v = math.inf
        for action in actions(board):
            deep_board = copy.deepcopy(board)
            k, l = action
            deep_board[k][l] = O
            print(actions(board))
            optionsx.append([action, max_value(deep_board)])
        print(optionsx)
        for i in range(len(optionsx)):
            if optionsx[i][1] <= min_v:
                optimal = optionsx[i][0]
                min_v = optionsx[i][1]
        print(optimal)

        return optimal

    raise NotImplementedError


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v
