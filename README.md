# Atividade Labirinto - AED 2

Trabalho da aula 9 sobre busca em labirinto usando DFS, BFS e Busca Gulosa.

## O Labirinto
O labirinto é 10x10. 
- `I`: início
- `F`: fim / saída
- `#`: parede
- `.`: caminho livre

O código lê a matriz e transforma numa estrutura de grafo (lista de adjacências com dicionário) pra poder rodar os algoritmos de busca.

## Algoritmos
- **DFS (Busca em Profundidade):** usa pilha, vai direto no fundo de uma rota antes de voltar.
- **BFS (Busca em Largura):** usa fila, testa os vizinhos em volta em ondas e acha o menor caminho.
- **Gulosa:** usa fila de prioridade com a distância de Manhattan pra tentar ir direto até a saída.

## Como rodar
No terminal, é só rodar:
```bash
python labirinto.py