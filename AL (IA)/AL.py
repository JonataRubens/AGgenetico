import random

# Define as cidades e suas distâncias
cidades = ["A", "B", "C", "D", "E"]
distancias = {
    ("A", "B"): 2,
    ("A", "C"): 9,
    ("A", "D"): 3,
    ("A", "E"): 6,
    ("B", "C"): 4,
    ("B", "D"): 3,
    ("B", "E"): 8,
    ("C", "B"): 4,
    ("C", "D"): 7,
    ("C", "E"): 3,
    ("D", "E"): 3,
    ("E", "A"): 6,
    ("E", 'B'): 8,
    ('D', 'B'): 3,
    ('D', 'C'): 7,
    ('D', 'A'): 3,
    ('C', 'A'): 9,
    ('C', 'E'): 3,
    ('C', 'B'): 4,
    ('B', 'C'): 4,
    ('B', 'E'): 8,
    ('B', 'D'): 3,
    ('A', 'E'): 6,
    ('A', 'D'): 3,
    ('A', 'C'): 9,
    ('A', 'B'): 2,
    ('E', 'D'): 3,
    ('E', 'C'): 3,
    ('E', 'B'): 8,
    ('E', 'A'): 6,
    ('D', 'A'): 3,
    ('D', 'B'): 3,
    ('D', 'C'): 7,
    ('D', 'E'): 3,
    ('C', 'E'): 3,
    ('C', 'B'): 4,
    ('C', 'A'): 9,
    ('C', 'D'): 7,
    ('B', 'A'): 2,
    ('B', 'C'): 4,
    ('B', 'D'): 3,
    ('B', 'E'): 8,
}

# Função para calcular a distância total de uma rota
def calcular_distancia(rota):
    distancia_total = 0
    for i in range(len(rota) - 1):
        distancia_total += distancias[(rota[i], rota[i+1])]
    distancia_total += distancias[(rota[-1], rota[0])]  # Considera o retorno à cidade inicial
    return distancia_total

# Função para gerar uma população inicial de rotas aleatórias
def gerar_populacao(tamanho_populacao):
    return [random.sample(cidades, len(cidades)) for _ in range(tamanho_populacao)]

# Função para selecionar os pais com base na aptidão (fitness)
def selecao(populacao, tamanho_torneio):
    torneio = random.sample(populacao, tamanho_torneio)
    return min(torneio, key=calcular_distancia)

# Função para realizar o crossover entre dois pais
def crossover(pai1, pai2):
    ponto_corte = random.randint(1, len(cidades) - 1)
    filho = pai1[:ponto_corte]
    for cidade in pai2:
        if cidade not in filho:
            filho.append(cidade)
    return filho

# Função para aplicar mutação em uma rota
def mutacao(rota, taxa_mutacao):
    if random.random() < taxa_mutacao:
        i, j = random.sample(range(len(rota)), 2)
        rota[i], rota[j] = rota[j], rota[i]
    return rota

# Algoritmo Genético
def algoritmo_genetico(tamanho_populacao, tamanho_torneio, taxa_mutacao, num_geracoes):
    populacao = gerar_populacao(tamanho_populacao)
    for _ in range(num_geracoes):
        nova_populacao = []
        for _ in range(tamanho_populacao):
            pai1 = selecao(populacao, tamanho_torneio)
            pai2 = selecao(populacao, tamanho_torneio)
            filho = crossover(pai1, pai2)
            filho = mutacao(filho, taxa_mutacao)
            nova_populacao.append(filho)
        populacao = nova_populacao
    melhor_rota = min(populacao, key=calcular_distancia)
    return melhor_rota, calcular_distancia(melhor_rota)

# Parâmetros do algoritmo genético
tamanho_populacao = 50
tamanho_torneio = 5
taxa_mutacao = 0.1
num_geracoes = 1000

# Execução do algoritmo genético
melhor_rota, distancia_minima = algoritmo_genetico(tamanho_populacao, tamanho_torneio, taxa_mutacao, num_geracoes)

# Exibição do resultado
print("Melhor rota encontrada:", melhor_rota)
print("Distância mínima encontrada:", distancia_minima)
