import numpy as np
from typing import Tuple, Callable

def MAX(state, alpha, beta, depth, utility, inciting_action):
    if depth == 0 or state.is_terminal():
        player = state.player
        if player is None: # Retrieves player that last played
            i,j = inciting_action
            player = str(state.get_board()).split('\n')[j][i]
        
        return utility(state, player), inciting_action
    
    value, action = -np.inf, None
    legal_moves = state.legal_moves()
    next_states = [(state.next_state(move), move) for move in legal_moves]

    for next, move in next_states:
        new_value, _ = MIN(next,alpha,beta,depth-1,utility,move)
        
        if new_value > value:
            value = new_value
            action = move

        alpha = max(alpha, value)
        if alpha >= beta:
            break
    
    return value, action

def other_player(player):
    return 'W' if player == 'B' else 'B'

def MIN(state, alpha, beta, depth, utility,inciting_action):
    if depth == 0 or state.is_terminal():
        player = state.player
        if player is None: # Retrieves player that last played
            i,j = inciting_action
            player = str(state.get_board()).split('\n')[j][i]
        
        return utility(state, other_player(player)), inciting_action
    
    value, action = np.inf, None
    legal_moves = state.legal_moves()
    next_states = [(state.next_state(move), move) for move in legal_moves]
    
    for next, move in next_states:
        new_value, _ = MAX(next,alpha,beta,depth-1,utility,move)

        if new_value < value:
            value = new_value
            action = move
        
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
    _, a = MAX(state, -np.inf, np.inf, max_depth, eval_func, None)
    return a


if __name__=='__main__':
    pass