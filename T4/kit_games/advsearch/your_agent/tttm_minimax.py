import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from typing import Tuple
from tttm.gamestate import GameState
from tttm.board import Board
from minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Retorna uma jogada calculada pelo algoritmo minimax para o estado de jogo fornecido.
    :param state: estado para fazer a jogada
    :return: tupla (int, int) com as coordenadas x, y da jogada (lembre-se: 0 é a primeira linha/coluna)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada do Jogo da Tic-Tac-Toe Misere
    # Remova-o e coloque uma chamada para o minimax_move com 
    # a sua implementacao da poda alpha-beta. Use profundidade ilimitada na sua entrega,
    # uma vez que o jogo tem profundidade maxima 9. 
    # Preencha a funcao utility com o valor de um estado terminal e passe-a como funcao de avaliação para seu minimax_move

    return minimax_move(state, -1, utility)

def utility(state, player:str) -> float:
    """
    Retorna a utilidade de um estado (terminal) 
    """
    board = str(state.get_board()).replace(' ','').replace('\n','')
    rows = [board[i:i+3] for i in [0,3,6]]
    cols = [board[i::3] for i in [0,1,2]]
    diags = [board[0::4], board[2:8:2]]

    options = rows + cols + diags

    losing_move = player*3
    
    print(options)

    return -1 if losing_move in options else 1

if __name__ == '__main__':
    b = Board.from_string('BWB\nWWB\nBW.')
    s = GameState(b, 'B')
    print(utility(s, 'W'))
    print(make_move(s))
