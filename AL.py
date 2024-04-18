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
    ('A','A') : 0,
    ('B','B') : 0,
    ('C','C') : 0,
    ('D','D') : 0,
    ('E','E') : 0
}

# Função para calcular a distância total de uma rota
def calcular_distancia_total(rota):
    distancia_total = 0
    for i in range(len(rota) - 1):
        distancia_total += distancias[(rota[i], rota[i+1])]
    distancia_total += distancias[(rota[-1], rota[0])]  # Considera o retorno à cidade inicial
    return distancia_total

# Função de aptidão para avaliar a qualidade de um cromossomo
def funcao_aptidao(cromossomo):
    return 1 / calcular_distancia_total(cromossomo)

# Função para gerar uma população inicial de rotas aleatórias
def gerar_populacao(tamanho_populacao):
    return [random.sample(cidades, len(cidades)) for _ in range(tamanho_populacao)]

# Função para selecionar os pais com base na aptidão (fitness)
def selecao(populacao, tamanho_torneio):
    torneio = random.sample(populacao, tamanho_torneio)
    return min(torneio, key=funcao_aptidao)

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
    melhor_rota = min(populacao, key=funcao_aptidao)
    return melhor_rota, calcular_distancia_total(melhor_rota)

def crossover_ponto_unico(pai1, pai2):
    ponto_corte = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
    filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
    return filho1, filho2

def mutacao_troca(cromossomo, taxa_mutacao):
    if random.random() < taxa_mutacao:
        i, j = random.sample(range(len(cromossomo)), 2)
        cromossomo[i], cromossomo[j] = cromossomo[j], cromossomo[i]
    return cromossomo

# Parâmetros do algoritmo genético
tamanho_populacao = 50
tamanho_torneio = 5
taxa_mutacao = 0.1
num_geracoes = 1000

#_______________________________________________________________#


# Função de aptidão para avaliar a qualidade de um cromossomo
def funcao_aptidao(cromossomo):
    return 1 / calcular_distancia_total(cromossomo)

cromossomo1 = random.sample(cidades, len(cidades))
cromossomo2 = random.sample(cidades, len(cidades))

aptidao_cromossomo1 = funcao_aptidao(cromossomo1)
aptidao_cromossomo2 = funcao_aptidao(cromossomo2)

filho1, filho2 = crossover_ponto_unico(cromossomo1, cromossomo2)


filho1_mutado = mutacao_troca(filho1, taxa_mutacao)
filho2_mutado = mutacao_troca(filho2, taxa_mutacao)

aptidao_filho1 = funcao_aptidao(filho1_mutado)
aptidao_filho2 = funcao_aptidao(filho2_mutado)


print("Aptidão do Filho 1:", aptidao_filho1)
print("Aptidão do Filho 2:", aptidao_filho2)


if aptidao_filho1 > aptidao_cromossomo1 or aptidao_filho2 > aptidao_cromossomo2:
    print("Pelo menos um dos descendentes tem uma aptidão melhor do que os pais.")
else:
    print("Nenhum dos descendentes tem uma aptidão melhor do que os pais.")



#_______________________________________________________________#


#Dois cromossomos
#cromossomo1 = random.sample(cidades, len(cidades))
#cromossomo2 = random.sample(cidades, len(cidades))

#print("Cromossomo 1 antes do crossover:", cromossomo1)
#print("Cromossomo 2 antes do crossover:", cromossomo2)

#filho1, filho2 = crossover_ponto_unico(cromossomo1, cromossomo2)

#print("\nFilho 1 após o crossover:", filho1)
#print("Filho 2 após o crossover:", filho2)

# Avaliação da aptidão dos cromossomos
#aptidao_cromossomo1 = funcao_aptidao(cromossomo1)
#aptidao_cromossomo2 = funcao_aptidao(cromossomo2)

# Exibição da aptidão dos cromossomos
#print("Cromossomo 1:", cromossomo1)
#print("Aptidão do Cromossomo 1:", aptidao_cromossomo1)

#print("\nCromossomo 2:", cromossomo2)
#print("Aptidão do Cromossomo 2:", aptidao_cromossomo2)








# Geração de um cromossomo aleatório
cromossomo = random.sample(cidades, len(cidades))

# Exibição do cromossomo antes da mutação
#print("Cromossomo antes da mutação:", cromossomo)

# Aplicação da mutação
cromossomo_mutado = mutacao_troca(cromossomo, taxa_mutacao)

# Exibição do cromossomo após a mutação
#print("Cromossomo após a mutação:", cromossomo_mutado)


#_______________________________________________________________#

# Execução do algoritmo genético
melhor_rota, distancia_minima = algoritmo_genetico(tamanho_populacao, tamanho_torneio, taxa_mutacao, num_geracoes)

# Exibição do resultado
#print("Melhor rota encontrada:", melhor_rota)
#print("Distância mínima encontrada:", distancia_minima)
