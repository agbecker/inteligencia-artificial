import numpy as np
from typing import Tuple, Callable

def MAX(state, alpha, beta, depth, utility, inciting_action):
    if depth == 0 or state.is_terminal():
        #print(f'In terminal state \n{state.board}\nbrought by {inciting_action}, utility = {utility(state, state.player)} for player {state.player}')
        return utility(state, state.player), inciting_action
    
    value, action = -np.inf, None
    legal_moves = state.legal_moves()
    next_states = [(state.next_state(move), move) for move in legal_moves]

    for next, move in next_states:
        # _ = print(next.board, move, utility(next,'B'), '\n') if depth == -1 else 0
        new_value, _ = MIN(next,alpha,beta,depth-1,utility,move)
        print('É DIFERENTE'*(new_value != 1))
        # print(f'{utility(next,"B")} and yet {new_value}')
        
        if new_value > value:
            value = new_value
            action = move
        
        alpha = max(alpha, value)
        if alpha >= beta:
            break
    
    # print(state.board.decorated_str())
    # print(f'MAX - Depth {depth}, Alpha {alpha}, Beta {beta}, Value = {value}, {action}')
    
    return value, action

def MIN(state, alpha, beta, depth, utility,inciting_action):
    if depth == 0 or state.is_terminal():
        #print(f'In terminal state \n{state.board}\nbrought by {inciting_action}, utility = {utility(state, state.player)} for player {state.player}')
        return utility(state, state.player), inciting_action
    
    value, action = np.inf, None
    legal_moves = state.legal_moves()
    next_states = [(state.next_state(move), move) for move in legal_moves]
    
    for next, move in next_states:
        # print(next.board, move, '\n')
        new_value, _ = MAX(next,alpha,beta,depth-1,utility,move)
        print('É DIFERENTE'*(new_value != 1))

        if new_value < value:
            value = new_value
            action = move
        
        beta = min(beta, value)
        if alpha >= beta:
            break
        
    # print(state.board.decorated_str())
    # print(f'MIN - Depth {depth}, Alpha {alpha}, Beta {beta}, Value = {value}, {action}')
    
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
    v, a = MAX(state, -np.inf, np.inf, max_depth, eval_func, None)
    return v, a


if __name__=='__main__':
    pass