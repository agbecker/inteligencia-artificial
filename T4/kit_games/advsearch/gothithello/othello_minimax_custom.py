import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from typing import Tuple
from othello.gamestate import GameState
from othello.board import Board
from minimax import minimax_move, other_player

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


EVAL_TEMPLATE = [
    [100, -30, 6, 2, 2, 6, -30, 100],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [100, -30, 6, 2, 2, 6, -30, 100]
]


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada 
    # Remova-o e coloque uma chamada para o minimax_move (que vc implementara' no modulo minimax).
    # A chamada a minimax_move deve receber sua funcao evaluate como parametro.

    MAX_DEPTH = 5
    return minimax_move(state, MAX_DEPTH, evaluate_custom)


def evaluate_custom(state, player:str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on your custom heuristic
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    board = str(state.get_board()).replace('\n','')
    opponent = other_player(player)
    
    if state.player is None:
        state.player = player
        
    opp_state = state.copy()
    opp_state.player = opponent
    
    player_moves = state.legal_moves()
    opponent_moves = opp_state.legal_moves()
    
    player_mobility = len(player_moves)
    opponent_mobility = len(opponent_moves)
    
    mobility = 100 * (player_mobility - opponent_mobility)/(player_mobility + opponent_mobility) if player_mobility + opponent_mobility != 0 else 0
    
    corners = board[0] + board[7] + board[63] + board[56]
    
    return mobility*(corners.count(player)+1)