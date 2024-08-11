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


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    MAX_DEPTH = 5
    return minimax_move(state, MAX_DEPTH, evaluate_count)


def evaluate_count(state, player:str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on the number of pieces of each color.
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    board = state.get_board()
    opponent = other_player(player)
    
    player_count = board.num_pieces(player)
    opponent_count = board.num_pieces(opponent)
    
    return player_count - opponent_count


if __name__=='__main__':
    s = GameState(Board(), 'B')
    s = s.next_state((5,4))
    print(s.board.decorated_str(False))
    print(evaluate_count(s,'B'))