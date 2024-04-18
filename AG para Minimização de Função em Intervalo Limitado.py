import random

# Função para calcular o valor de f(x)
def calcular_fitness(x):
    return x**2 - 3*x + 4

# Função para decodificar um vetor binário para o intervalo [0, 10]
def decodificar(x_binario):
    return int(''.join(map(str, x_binario)), 2) / 15 * 10

# Função para aplicar a mutação em um indivíduo (bit flip)
def mutacao(individuo):
    indice_mutacao = random.randint(0, len(individuo) - 1)
    individuo[indice_mutacao] = 1 - individuo[indice_mutacao]

# População inicial (4 indivíduos)
populacao = [[random.randint(0, 1) for _ in range(4)] for _ in range(4)]

# Execução por 3 gerações
for geracao in range(3):
    print("Geração", geracao + 1)
    
    # Avaliação da aptidão dos indivíduos
    fitness_populacao = [calcular_fitness(decodificar(individuo)) for individuo in populacao]
    
    # Seleção por torneio simples
    filhos = []
    for _ in range(2):
        torneio = random.sample(list(enumerate(fitness_populacao)), 2)
        vencedor = max(torneio, key=lambda x: x[1])[0]
        filhos.append(populacao[vencedor])
    
    # Aplicação da mutação em um filho
    mutacao(filhos[random.randint(0, 1)])
    
    # Reinserção com elitismo
    melhor_individuo_geracao_anterior = populacao[fitness_populacao.index(max(fitness_populacao))]
    populacao = filhos + [melhor_individuo_geracao_anterior]
    
    # Exibição da população e do melhor indivíduo da geração
    for i, individuo in enumerate(populacao):
        print("Indivíduo", i + 1, ":", individuo, "- Fitness:", fitness_populacao[i])
    print("Melhor indivíduo da geração:", melhor_individuo_geracao_anterior, "- Fitness:", max(fitness_populacao))
    print()
