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
|Valor posicional |Contagem de peças | | | |
|Contagem de peças |Heurística customizada | | | |
|Heurística customizada | Contagem de peças| | | |
|Valor posicional |Heurística customizada | | | |
|Heurística customizada |Valor posicional | | | |