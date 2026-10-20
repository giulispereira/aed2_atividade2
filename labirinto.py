import heapq
from collections import deque

LABIRINTO = [
    "I.........",
    "#########.",
    ".........#",
    ".#########",
    ".........#",
    "#########.",
    ".........#",
    ".#########",
    ".........#",
    "#########F",
]

DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def achar(lab, simbolo):
  for i, linha in enumerate(lab):
    if simbolo in linha:
      return (i, linha.index(simbolo))
  return None


def livre(lab, i, j):
  dentro = 0 <= i < len(lab) and 0 <= j < len(lab[0])
  return dentro and lab[i][j] != "#"


def montar_grafo(lab):
  grafo = {}
  for i in range(len(lab)):
    for j in range(len(lab[0])):
      if not livre(lab, i, j):
        continue
      grafo[(i, j)] = []
      for di, dj in DIRECOES:
        if livre(lab, i + di, j + dj):
          grafo[(i, j)].append((i + di, j + dj))
  return grafo


def reconstruir_caminho(veio_de, inicio, fim):
  atual = fim
  caminho = []
  while atual != inicio and atual in veio_de:
    caminho.append(atual)
    atual = veio_de[atual]
  caminho.append(inicio)
  caminho.reverse()
  return caminho


# 1. DFS (Busca em profundidade)
def dfs(grafo, inicio, saida):
  pilha = [inicio]
  veio_de = {inicio: None}
  visitados = set([inicio])
  casas_visitadas = 0

  while pilha:
    v = pilha.pop()
    casas_visitadas += 1

    if v == saida:
      break

    for vizinho in grafo[v]:
      if vizinho not in visitados:
        visitados.add(vizinho)
        veio_de[vizinho] = v
        pilha.append(vizinho)

  caminho = reconstruir_caminho(veio_de, inicio, saida) if saida in veio_de else []
  return caminho, casas_visitadas


# 2. BFS (busca em largura)
def bfs(grafo, inicio, saida):
  fila = deque([inicio])
  veio_de = {inicio: None}
  visitados = set([inicio])
  casas_visitadas = 0

  while fila:
    v = fila.popleft()
    casas_visitadas += 1

    if v == saida:
      break

    for vizinho in grafo[v]:
      if vizinho not in visitados:
        visitados.add(vizinho)
        veio_de[vizinho] = v
        fila.append(vizinho)

  caminho = reconstruir_caminho(veio_de, inicio, saida) if saida in veio_de else []
  return caminho, casas_visitadas


# 3. Busca Gulosa (greedy best-first search)
def h(v, saida):
  return abs(v[0] - saida[0]) + abs(v[1] - saida[1])


def gulosa(grafo, inicio, saida):
  contador = 0
  fronteira = [(h(inicio, saida), contador, inicio)]
  veio_de = {inicio: None}
  visitados = set([inicio])
  casas_visitadas = 0

  while fronteira:
    _, _, v = heapq.heappop(fronteira)
    casas_visitadas += 1

    if v == saida:
      break

    for vizinho in grafo[v]:
      if vizinho not in visitados:
        visitados.add(vizinho)
        veio_de[vizinho] = v
        contador += 1
        heapq.heappush(fronteira, (h(vizinho, saida), contador, vizinho))

  caminho = reconstruir_caminho(veio_de, inicio, saida) if saida in veio_de else []
  return caminho, casas_visitadas


def desenhar(lab, caminho):
  grade = [list(linha) for linha in lab]
  for i, j in caminho:
    if grade[i][j] == ".":
      grade[i][j] = "*"
  for linha in grade:
    print("".join(linha))


# Execução principal
inicio = achar(LABIRINTO, "I")
saida = achar(LABIRINTO, "F")
grafo = montar_grafo(LABIRINTO)

c_dfs, v_dfs = dfs(grafo, inicio, saida)
c_bfs, v_bfs = bfs(grafo, inicio, saida)
c_gulosa, v_gulosa = gulosa(grafo, inicio, saida)

print("=== CAMINHO DFS ===")
desenhar(LABIRINTO, c_dfs)

print("\n=== CAMINHO BFS ===")
desenhar(LABIRINTO, c_bfs)

print("\n=== CAMINHO GULOSA ===")
desenhar(LABIRINTO, c_gulosa)

print("\n" + "=" * 55)
print(f"{'Algoritmo':<15} | {'Tamanho do Caminho':<18} | {'Casas Visitadas':<15}")
print("-" * 55)
print(f"{'DFS':<15} | {len(c_dfs):<18} | {v_dfs:<15}")
print(f"{'BFS':<15} | {len(c_bfs):<18} | {v_bfs:<15}")
print(f"{'Gulosa':<15} | {len(c_gulosa):<18} | {v_gulosa:<15}")
print("=" * 55)