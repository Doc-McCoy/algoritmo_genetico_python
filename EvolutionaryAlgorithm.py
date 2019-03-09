import random
from pprint import PrettyPrinter

'''
Este algoritmo genético irá tentar descobrir uma sequência
de 8 números pré estabelecida em RESULTADO_ESPERADO.
'''

class Individuo():

    def __init__(self, cromossomos):
        self.cromossomos = cromossomos
        self.fitness = 0

    def __str__(self):
        return str(self.cromossomos)

    def set_fitness(self, fitness):
        self.fitness = fitness
    
    def get_fitness(self):
        return self.fitness
    
    def altera_cromossomo(self, index, novo_valor):
        self.cromossomos[index] = novo_valor

class EvolutionaryAlgorithm():

    RESULTADO_ESPERADO  = (3, 4, 6, 2, 3, 3, 6, 8)

    TAMANHO_CROMOSSOMO  = 8
    TAMANHO_POPULACAO   = 10
    MAXIMO_GERACOES     = 10000
    TAXA_CROSSOVER      = 0.5
    TAXA_MUTACAO        = 0.03

    geracao             = 0

    def incrementar_geracao(self):
        self.geracao += 1
    
    def criarPopulacao(self):
        ''' Cria a população randomica inicial, com n
        indivíduos de acordo com o TAMANHO_POPULACAO. '''

        self.populacao = []

        for i in range(self.TAMANHO_POPULACAO):
            cromossomos = []

            for j in range(self.TAMANHO_CROMOSSOMO):
                cromossomos.append(random.randint(0, 9))

            individuo = Individuo(cromossomos)
            self.populacao.append(individuo)

        return self.populacao


    def validarFitness(self, populacao):
        ''' Testa uma população e retorna quantos pontos ela fez,
        baseado na comparação dos valores de seus elementos com a
        lista RESULTADO_ESPERADO. '''

        esperado    = self.RESULTADO_ESPERADO

        for individuo in populacao:
            cromossomos = individuo.cromossomos

            acertos = [i for i, j in zip(esperado, cromossomos) if i == j]
            quantidade_de_acertos = len(acertos)
            individuo.set_fitness(quantidade_de_acertos)


    def selecao(self, populacao):
        ''' Faz o ranqueamento da população de acordo com os
        respectivos fitness, e seleciona os pais da próxima
        geração. '''

        lista_fitness = []
        for individuo in populacao:
            lista_fitness.append(individuo.get_fitness())

        # Nota.: random.choices recebe a lista da população, e a lista dos valores
        # fitnes para usar de peso. Valores maiores tem mais chances de serem
        # selecionados.
        # K é a quantidade de itens da lista que a função seleciona.
        pais_selecionados = random.choices(populacao, k=2, weights=lista_fitness)

        return pais_selecionados        


    def crossover(self, pais):
        ''' Realiza o crossover dos cromossomos dos pais, gerando
        assim 2 filhos com as características de ambos. '''

        pai, mae            = pais
        cromossomos_filho_x = []
        cromossomos_filho_y = []

        for index in range(self.TAMANHO_CROMOSSOMO):
            valor_aleatorio = random.random()
            if valor_aleatorio < self.TAXA_CROSSOVER:
                cromossomos_filho_x.append(mae.cromossomos[index])
            else:
                cromossomos_filho_x.append(pai.cromossomos[index])

            valor_aleatorio = random.random()
            if valor_aleatorio < self.TAXA_CROSSOVER:
                cromossomos_filho_y.append(mae.cromossomos[index])
            else:
                cromossomos_filho_y.append(pai.cromossomos[index])

        filho_x = Individuo(cromossomos_filho_x)
        filho_y = Individuo(cromossomos_filho_y)

        self.mutacao(filho_x)
        self.mutacao(filho_y)

        return [filho_x, filho_y]


    def mutacao(self, individuo):
        ''' Realiza mutações nos cromossomos de um individuo,
        de acordo com a TAXA_MUTACAO. '''

        valor_aleatorio = random.random()

        if valor_aleatorio < self.TAXA_MUTACAO:
            cromossomo_escolhido = random.randint(0, self.TAMANHO_CROMOSSOMO - 1)
            novo_valor = random.randint(0, 9)
            individuo.altera_cromossomo(cromossomo_escolhido, novo_valor)



if __name__ == '__main__':
    pp          = PrettyPrinter(indent=4)
    EvAlg       = EvolutionaryAlgorithm()

    print("Sequencia de números que o algoritmo vai tentar descobrir:")
    print(EvAlg.RESULTADO_ESPERADO)
    populacao   = EvAlg.criarPopulacao()
    print("Geração inicial gerada aleatoriamente:")
    for i in populacao:
        print(i)
    EvAlg.validarFitness(populacao)
    print("Trabalhando....\n")

    while EvAlg.geracao < EvAlg.MAXIMO_GERACOES:
        nova_populacao = []

        while len(nova_populacao) < EvAlg.TAMANHO_POPULACAO:
            pais    = EvAlg.selecao(populacao)
            filhos  = EvAlg.crossover(pais)

            nova_populacao.append(filhos[0])
            nova_populacao.append(filhos[1])

        populacao = nova_populacao
        EvAlg.validarFitness(populacao)
        EvAlg.incrementar_geracao()

    print("Final do processo. A populacao atual é a seguinte")
    for i in populacao:
        print(i.cromossomos)
