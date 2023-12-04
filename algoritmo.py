# Importa a biblioteca heapq para implementar a fila de prioridade
import heapq

# Classe que representa um Nodo no algoritmo A*
class Nodo:
    def __init__(self, x, y, custo, parente=None):
        self.x = x
        self.y = y
        self.custo = custo
        self.parente = parente

    def __lt__(self, outro):
        return self.custo < outro.custo  # Comparação para ordenar a fila de prioridade

# Função heurística para calcular a distância até o destino
def heuristica(x, y, destino):
    return abs(x - destino[0]) + abs(y - destino[1])

# Função para obter os vizinhos válidos de um Nodo no mapa
def getVizinhos(dadosMapa, nodo):
    largura, altura, obstaculos, _, _ = dadosMapa
    vizinhos = []

    # Percorre os possíveis movimentos: cima, baixo, esquerda, direita
    for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        x, y = nodo.x + i, nodo.y + j
        # Verifica se a posição é válida e não é um obstáculo
        if 0 <= x < largura and 0 <= y < altura and (x, y) not in obstaculos:
            custo = abs(i) + abs(j)  # Cálculo do custo considerando movimentos apenas na horizontal ou vertical
            vizinhos.append(Nodo(x, y, custo, parente=nodo))

    return vizinhos

# Função principal que implementa o algoritmo A*
def algoritmo(dadosMapa, inicio, destino):
    largura, altura, _, _, _ = dadosMapa
    nodo_inicio = Nodo(inicio[0], inicio[1], 0)
    coordenada = [nodo_inicio]  # Fila de prioridade (heapq) para os nodos a serem explorados
    coordenada2 = set()  # Conjunto para manter controle dos nodos já visitados

    while coordenada:
        atual = heapq.heappop(coordenada)

        # Verifica se o destino foi alcançado
        if (atual.x, atual.y) == destino:
            caminho = [(atual.x, atual.y)]
            custoTotal = atual.custo  # Inicializa o custo total com o custo do nó final
            while atual.parente:
                caminho.append((atual.parente.x, atual.parente.y))
                custoTotal += atual.parente.custo  # Soma o custo do deslocamento ao custo total
                atual = atual.parente
            caminho.reverse()
            return caminho, custoTotal

        coordenada2.add((atual.x, atual.y))

        for vizinho in getVizinhos(dadosMapa, atual):
            if (vizinho.x, vizinho.y) in coordenada2:
                continue

            custoTentativa = atual.custo + vizinho.custo  # Corrigido para considerar o custo do movimento
            # Verifica se o vizinho não foi explorado ou se o novo custo é menor
            if vizinho not in coordenada or custoTentativa < vizinho.custo:
                vizinho.custo = custoTentativa
                vizinho.parente = atual
                if vizinho not in coordenada:
                    heapq.heappush(coordenada, vizinho)

    return None, None

# Função para ler o mapa a partir de um arquivo
def lerMapa(caminhoArquivo):
    with open(caminhoArquivo, 'r') as arquivo:
        largura, altura = map(int, arquivo.readline().split())
        inicioX, inicioY = map(int, arquivo.readline().split())

        obstaculos = set()
        for i in range(altura):
            linha = list(map(int, arquivo.readline().split()))
            for j, valor in enumerate(linha):
                if valor == -1:
                    obstaculos.add((j, i))

    return largura, altura, obstaculos, inicioX, inicioY

# Função principal para execução do sistema
def main():
    caminhoArquivo = 'mapa.txt'  # Substitua pelo caminho do arquivo do seu mapa
    dadosMapa = lerMapa(caminhoArquivo)

    destinoX, destinoY = map(int, input("\nT2 - IMPLEMENTAÇÃO ALGORITMO A*\n\nPor favor, forneça as coordenadas do ponto de destino no formato (x y):\n").split())

    caminho, custo = algoritmo(dadosMapa, (dadosMapa[3], dadosMapa[4]), (destinoX, destinoY))

    if caminho:
        print(f"\nApós análise das coordenadas fornecidas, foi identificado o caminho:")
        for ponto in caminho:
            print(f"({ponto[0]}, {ponto[1]}); ", end="")
        print(f"\n\nCom um custo total de: {custo}.")
    else:
        print("Não foi possível identificar um caminho com as coordenadas fornecidas.")

if __name__ == "__main__":
    main()