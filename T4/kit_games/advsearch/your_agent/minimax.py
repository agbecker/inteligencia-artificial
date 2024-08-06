import random, numpy as np
from typing import Tuple, Callable

def MAX(state, alpha, beta, depth, eval_func):
    if state.is_terminal() or depth == 0:
        return eval_func(state, 'max')
    value = -np.inf
    action = None

    moves = list(state.legal_moves())
    successors = [state.next_state(move) for move in moves]

    for i, next_state in enumerate(successors):
        new_value, x = MIN(next_state,alpha,beta,depth-1,eval_func)
        if new_value > value:
            value = new_value
            action = moves[i]
        alpha = max(alpha, value)
        if alpha >= beta:
            break

    return value, action

def MIN(state, alpha, beta, depth, eval_func):
    if state.is_terminal() or depth == 0:
        return eval_func(state, 'min')
    value = np.inf
    action = None

    moves = list(state.legal_moves())
    successors = [state.next_state(move) for move in moves]

    for i, next_state in enumerate(successors):
        new_value, x = MAX(next_state,alpha,beta,depth-1,eval_func)
        if new_value < value:
            value = new_value
            action = moves[i]
        beta = min(beta, value)
        if alpha >= beta:
            break

    return value, action


def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    raise NotImplementedError()
