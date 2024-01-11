"""
Tic Tac Toe Player
"""
import copy
import math

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
    init_state = True
    X_num = 0
    O_num = 0
    X_turn = False

    # iterate through every cell on the board
    for sublist in board:
        for item in sublist:
            if item == X:
                X_num += 1
                init_state = False
            elif item == O:
                O_num += 1
                init_state = False

    # if number of X's equals number of O's, its X's turn
    if X_num - O_num == 0:
        X_turn = True

    # If it's X's turn or an initial board, return X
    if init_state or X_turn:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # create empty set to store tuples
    action_set = set()

    # iterate through all the cells using enumerate to get the index
    for row_index, sublist in enumerate(board):
        for col_index, item in enumerate(sublist):
            # if a cell is empty, add the tuple of the indices into the set
            if item == EMPTY:
                action_set.add((row_index, col_index))

    if len(action_set) == 0:
        return None
    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # if action isn't proper, raise exception
    if action not in actions(board):
        raise Exception

    # create copy of board
    copy_board = copy.deepcopy(board)

    # fill in the cell depending on the current player
    current_player = player(board)
    copy_board[action[0]][action[1]] = current_player
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # checks horizontally and vertically for a winner
    for i in range(len(board)):
        # reset counters to 0 for each row and column
        row_counter_X, row_counter_O = 0, 0
        col_counter_X, col_counter_O = 0, 0

        for j in range(len(board)):
            # check rows for X and O
            if board[i][j] == X:
                row_counter_X += 1
            elif board[i][j] == O:
                row_counter_O += 1

            # check columns for X and O
            if board[j][i] == X:
                col_counter_X += 1
            elif board[j][i] == O:
                col_counter_O += 1

            if row_counter_X == 3 or col_counter_X == 3:
                return X
            elif row_counter_O == 3 or col_counter_O == 3:
                return O

    # checks diagonally for a winner
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    # returns None if no winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # first check if there is a winner (then game is over)
    if winner(board) is not None:
        return True

    # If there is an empty cell, return false
    for row in board:
        if EMPTY in row:
            return False
    return True


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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # if terminal board, return None
    if terminal(board):
        return None

    # max value function
    def max_value(board, alpha, beta):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move

        v = -100

        for action in actions(board):
            minvalue = min_value(result(board, action), alpha, beta)[0]
            if minvalue > v:
                v = minvalue
                optimal_move = action
            # alpha pruning
            alpha = max(v, alpha)
            if beta <= alpha:
                break
        return v, optimal_move

    # min value function
    def min_value(board, alpha, beta):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move

        v = 100

        for action in actions(board):
            maxvalue = max_value(result(board, action), alpha, beta)[0]
            if maxvalue < v:
                v = maxvalue
                optimal_move = action
            # beta pruning
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v, optimal_move

    alpha = float('-inf')
    beta = float('inf')

    if player(board) == X:
        return max_value(board, alpha, beta)[1]
    else:
        return min_value(board, alpha, beta)[1]
