# Implementação do Algoritmo A*

Este sistema, desenvolvido como trabalho prático para a disciplina de Complexidade de Algoritmos e Avaliação de Desempenho da Universidade La Salle em Canoas - RS, implementa o algoritmo A\* para encontrar o caminho de menor custo entre dois pontos em um mapa.

## Instruções de Uso

### Formato do Mapa

O mapa é definido em um arquivo de texto e deve seguir o seguinte formato:

```
<largura:int> <altura:int>
<x_inicial:int> <y_inicial:int>
<matriz de valores inteiros>
```

* Os valores na matriz representam o custo de passar por cada ponto no mapa.
* O valor -1 indica um obstáculo intransponível.
* As coordenadas são baseadas em índices zero, começando no canto superior esquerdo.

Exemplo:

```
10 8
0 7
3 1 4 -1 -1 8 8 8 0 0
3 3 2 6 2 3 8 8 1 0
3 3 3 5 6 8 10 6 1 0
0 1 1 4 0 10 10 -1 1 0
0 1 1 4 5 0 0 -1 1 0
0 1 1 1 1 0 0 -1 1 0
0 1 1 1 1 1 10 10 3 0
0 0 0 0 0 0 10 10 10 0
```

### Saída

O programa mostrará o caminho de menor custo e o custo total no seguinte formato:

```
Caminho: (<x:int>, <y:int>); (<x:int>, <y:int>); ...
Custo: <custo:int>
```