from typing import Iterable, Set, Tuple
from heapq import heappush as push, heappop as pop

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai, acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        
    def __hash__(self) -> int:
        return hash(self.estado)
    
    def __eq__(self, outro: object) -> bool:
        return self.estado == outro.estado
    
    def __str__(self) -> str:
        return f'{self.estado} - obtido de {self.pai.estado} fazendo {self.acao}. Custo {self.custo}' if self.pai is not None else self.estado

    @classmethod
    def set_funcao(self, funcao):
        self.f = funcao

    def __lt__(self, outro):
        return self.f(self) < self.f(outro)

def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    cima = estado[:3]
    baixo = estado [6:]
    esquerda = estado[::3]
    direita = estado[2::3]
    
    acoes = []
    
    if '_' not in cima:
        acoes.append('acima')
    if '_' not in baixo:
        acoes.append('abaixo')
    if '_' not in esquerda:
        acoes.append('esquerda')
    if '_' not in direita:
        acoes.append('direita')
        
    return {(acao, resolver_acao(estado, acao)) for acao in acoes}

def resolver_acao(estado:str, acao:str)->str:
    """
    Recebe um estado e uma ação, e retorna o estado resultante da realização da ação
    """
    i = estado.index('_')
    match acao:
        case 'acima':
            return estado[:i-3] + '_' + estado[i-2:i] + estado[i-3] + estado[i+1:]*(i<8)
        case 'abaixo':
            return estado[:i] + estado[i+3] + estado[i+1:i+3] + '_' + estado[i+4:]*(i<8)
        case 'esquerda':
            return estado[:i-1] + '_' + estado[i-1] + estado[i+1:]*(i<8)
        case 'direita':
            return estado[:i] + estado[i+1] + '_' + estado[i+2:]*(i<8)

def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    sucs = sucessor(nodo.estado)
    filhos = set()
    
    for (acao, estado) in sucs:
        filho = Nodo(estado=estado, pai=nodo, acao=acao, custo=nodo.custo+1)
        filhos.add(filho)
    
    return filhos

def dist_hamming(estado:str) -> int:
    ref = '12345678_'
    
    return sum([1*(estado[i] != ref[i]) for i in range(9)])

def dist_manhattan(estado: str) -> int:
    ref = '12345678_'
    custo = 0
    
    for i, c in enumerate(estado):
        dx = abs(i%3 - (ref.index(c)%3))
        dy = abs(i//3 - (ref.index(c)//3))
        custo += dx + dy
        
    return custo

def insoluvel(estado:str) -> bool:
    inversoes = 0
    s = estado.replace('_','')
    
    for i, c in enumerate(s):
        for d in s[i+1:]:
            inversoes += 1*(c>d)
    
    return inversoes%2 == 1

def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    if insoluvel(estado):
        return None
    
    Nodo.set_funcao(lambda a, x: x.custo + dist_hamming(x.estado))

    explorados = set()
    fronteira = []
    push(fronteira, Nodo(estado=estado, pai=None, acao='', custo=0))
    caminho = []
    
    while len(fronteira) > 0:
        v = pop(fronteira)
        #print(v)
        if v.estado == '12345678_':
            print(f'Nós expandidos: {len(explorados) + len(fronteira)}')
            aux = v
            while aux.estado != estado:
                caminho.append(aux.acao)
                aux = aux.pai
            print(f'Custo da solução: {len(caminho)}')
            return caminho[::-1]
        
        explorados.add(v)
        vizinhos = expande(v)
        for u in vizinhos:
            if u not in explorados and u not in fronteira:
                push(fronteira, u)
    
    return None


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    if insoluvel(estado):
        return None
    
    Nodo.set_funcao(lambda a, x: x.custo + dist_manhattan(x.estado))

    explorados = set()
    fronteira = []
    push(fronteira, Nodo(estado=estado, pai=None, acao='', custo=0))
    caminho = []
    
    while len(fronteira) > 0:
        v = pop(fronteira)
        #print(v)
        if v.estado == '12345678_':
            print(f'Nós expandidos: {len(explorados) + len(fronteira)}')
            aux = v
            while aux.estado != estado:
                caminho.append(aux.acao)
                aux = aux.pai
            print(f'Custo da solução: {len(caminho)}')
            return caminho[::-1]
        
        explorados.add(v)
        vizinhos = expande(v)
        for u in vizinhos:
            if u not in explorados and u not in fronteira:
                push(fronteira, u)
    
    return None

#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

def dist_becker(estado: str)->int:
    ref = '123456789'
    estado = estado.replace('_','9')
    custo = 0
    for i, c in enumerate(estado):
        custo += abs(int(c)-int(ref[i]))
    return custo    

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """    
    # Heurística: a diferença entre o valor de um número e o valor do número que deveria ocupar a sua posição atual.
    
    # substituir a linha abaixo pelo seu codigo
    if insoluvel(estado):
        return None
    
    Nodo.set_funcao(lambda a, x: x.custo + dist_becker(x.estado))

    explorados = set()
    fronteira = []
    push(fronteira, Nodo(estado=estado, pai=None, acao='', custo=0))
    caminho = []
    
    while len(fronteira) > 0:
        v = pop(fronteira)
        #print(v)
        if v.estado == '12345678_':
            print(f'Nós expandidos: {len(explorados) + len(fronteira)}')
            aux = v
            while aux.estado != estado:
                caminho.append(aux.acao)
                aux = aux.pai
            print(f'Custo da solução: {len(caminho)}')
            return caminho[::-1]
        
        explorados.add(v)
        vizinhos = expande(v)
        for u in vizinhos:
            if u not in explorados and u not in fronteira:
                push(fronteira, u)
    
    return None

if __name__ == '__main__':
    from timeit import default_timer as time

    for f in [astar_hamming, astar_manhattan, astar_new_heuristic]:

        start = time()
        x = f('2_3541687')
        stop = time()
        print(f'Tempo decorrido: {stop-start}')
        print(x)
        print('--------')