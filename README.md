**AL

Este script implementa um algoritmo genético para resolver o Problema do Caixeiro Viajante (PCV) para um conjunto fixo de cidades e distâncias entre elas.

1. **Definição das cidades e distâncias**:
   - As cidades são representadas como uma lista de strings.
   - As distâncias entre as cidades são armazenadas em um dicionário, onde as chaves são tuplas de cidades e os valores são as distâncias correspondentes.

2. **Funções de Avaliação de Aptidão**:
   - A função `funcao_aptidao(cromossomo)` calcula a aptidão de um cromossomo, que é definida como o inverso da distância total da rota.
   
3. **Geração Inicial da População**:
   - A função `gerar_populacao(tamanho_populacao)` cria uma população inicial de rotas aleatórias, onde cada rota é uma permutação das cidades.

4. **Seleção de Pais**:
   - A função `selecao(populacao, tamanho_torneio)` seleciona os pais com base em um torneio de tamanho especificado, onde os indivíduos mais aptos têm maior probabilidade de serem escolhidos.

5. **Crossover**:
   - A função `crossover(pai1, pai2)` realiza o crossover de ponto único entre dois pais, criando dois filhos.

6. **Mutação**:
   - A função `mutacao(rota, taxa_mutacao)` aplica a mutação de troca em uma rota com uma certa probabilidade.

7. **Execução do Algoritmo Genético**:
   - A função `algoritmo_genetico(tamanho_populacao, tamanho_torneio, taxa_mutacao, num_geracoes)` executa o algoritmo genético completo por um número especificado de gerações, retornando a melhor rota encontrada e sua distância total mínima.

8. **Crossover de Ponto Único e Mutação**:
   - Aqui, uma versão alternativa do crossover de ponto único e da mutação de troca é implementada para fins de comparação.

9. **Testes e Avaliação**:
   - Os resultados da aptidão dos cromossomos antes e depois do crossover, mutação e avaliação do algoritmo genético são exibidos para fins de análise e comparação.

Esse código demonstra como implementar um algoritmo genético para resolver o Problema do Caixeiro Viajante, uma tarefa comum em otimização combinatória.



++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
script 2

**AG

Este script implementa um algoritmo genético para otimização de uma função univariada \( f(x) = x^2 - 3x + 4 \), onde \( x \) está no intervalo \([0, 10]\). 

1. **Importação do Módulo Random**:
   - O módulo `random` é importado para geração de números aleatórios.

2. **Função de Fitness**:
   - A função `calcular_fitness(x)` recebe um valor \( x \) decodificado a partir de uma representação binária e retorna o valor da função de fitness \( f(x) = x^2 - 3x + 4 \).

3. **Decodificação do Indivíduo**:
   - A função `decodificar(x_binario)` decodifica um vetor binário representando um indivíduo para o intervalo \([0, 10]\) usando conversão binária para decimal.

4. **Mutação**:
   - A função `mutacao(individuo)` aplica uma mutação em um indivíduo, selecionando aleatoriamente um bit e realizando uma inversão (bit flip).

5. **População Inicial**:
   - A população inicial é composta por 4 indivíduos, onde cada indivíduo é representado por um vetor binário de comprimento 4.

6. **Execução do Algoritmo Genético**:
   - O algoritmo é executado por 3 gerações.
   - Para cada geração:
     - Calcula-se a função de fitness para cada indivíduo na população.
     - Realiza-se a seleção por torneio simples para escolher os pais.
     - Aplica-se uma mutação em um dos filhos gerados.
     - Realiza-se a reinserção com elitismo, mantendo o melhor indivíduo da geração anterior.
     - Exibe-se a população atual e o melhor indivíduo da geração.

O código demonstra a implementação de um algoritmo genético básico para otimização de uma função univariada, utilizando codificação binária para representar os indivíduos e seleção por torneio para escolha dos pais.

