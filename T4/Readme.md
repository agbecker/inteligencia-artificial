## INF01048 - Inteligência Artificial <br/> Trabalho 4 - Busca com Adversário

#### Álvaro Guglielmin Becker - 00301391 <br/> Enzo Borges Segala - 00335314 <br/> Tomás Ruschel Canales da Trindade - 00326448
**Turma B**
**Professor Joel Carbonera**

---

### 1. Bibliotecas adicionais
Nenhuma foi usada

### 2. Avaliação dos agentes
#### a) Tic-tac-toe misere
(i) Foram feitas 20 partidas entre o minimax e o randomplayer: 10 com o minimax fazendo o primeiro movimento, e 10 com ele fazendo o segundo.

No primeiro caso, o minimax ganhou 6/10 partidas, com as outras 4 sendo empates. No segundo caso, ele ganhou todas as partidas.

(ii) O minimax sempre empata consigo mesmo. Só é necessário testar isto uma vez, pois ele sempre adotará a mesma estratégia neste caso.

(iii) Testando contra os membros da equipe, o minimax sempre ganhou ou empatou, nunca perdeu.

#### b) Othello

A tabela abaixo mostra os resultados do mini-torneio entre diferentes algoritmos.

| Pretas | Brancas |     | Vencedor | Placar | 
| ---    | ---     | --- | ---      | ---    |
|Contagem de peças |Valor posicional | |Valor posicional |24 x 40 |
|Valor posicional |Contagem de peças | |Valor posicional |33 x 31 |
|Contagem de peças |Heurística customizada | |Heurística customizada |12 x 52 |
|Heurística customizada | Contagem de peças| |Heurística customizada |44 x 20 |
|Valor posicional |Heurística customizada | |Heurística customizada |27 x 37 |
|Heurística customizada |Valor posicional | |Valor posicional |29 x 35 |

As heurísticas de valor posicional e customizadas empataram em termos de número de vitórias, com cada uma ganhando 3 jogos. Entretanto, a de valor posicionou ganhou com uma média de 3.5 pontos de vantagem sobre seus oponentes, enquanto a customizada ganhou com uma média de 17 pontos de vantagem. Nesse sentido, seria possível afirmar que a customizada é melhor na média.

#### 3. Implementação do Othello
A heurística customizada usada foi planejada como uma expansão da heurística de valor posicional. Realiza o mesmo cálculo de utilidade que esta última, mas adicionalmente calcula quantas possibilidades de movimento cada jogador teria no turno seguinte. A diferença entre o número de possibilidades do jogador e do oponente é somado ao valor retornado pela função.

Esta heurística foi bolada baseada no critério de mobilidade apresentada em
https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/miniproject1_vaishu_muthu/Paper/Final_Paper.pdf

Para todos os modelos, foi usada profundidade máxima fixa 5, pois valores maiores causaram estouro do limite de tempo.

Para o torneio, usaremos a heurística customizada.