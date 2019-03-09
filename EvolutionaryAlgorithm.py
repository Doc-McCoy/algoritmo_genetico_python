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

class EvolutionaryAlgorithm():

    RESULTADO_ESPERADO  = (3, 4, 6, 2, 3, 3, 6, 8)

    TAMANHO_CROMOSSOMO  = 8
    TAMANHO_POPULACAO   = 10
    MAXIMO_GERACOES     = 100
    TAXA_CROSSOVER      = 0.5
    TAXA_MUTACAO        = 0.01

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
        assim 2 filhos com as características de ambos.
        Tipo assim:
            0000|0000 => 00001111
            1111|1111 => 11110000
        '''

        pai, mae = pais
        metade_do_cromossomo = int(self.TAMANHO_CROMOSSOMO / 2)

        cromossomos_filho_x = pai.cromossomos[: metade_do_cromossomo] + mae.cromossomos[metade_do_cromossomo :]
        cromossomos_filho_y = mae.cromossomos[: metade_do_cromossomo] + pai.cromossomos[metade_do_cromossomo :]

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
            cromossomo_escolhido = random.randint(0, self.TAMANHO_CROMOSSOMO)
            novo_valor = random.randint(0, 9)
            individuo.cromossomos[cromossomo_escolhido] = novo_valor



if __name__ == '__main__':
    pp          = PrettyPrinter(indent=4)
    EvAlg       = EvolutionaryAlgorithm()

    populacao   = EvAlg.criarPopulacao()
    EvAlg.validarFitness(populacao)

    while EvAlg.geracao < EvAlg.MAXIMO_GERACOES:
        nova_populacao = []
        print("rodando geracao " + str(EvAlg.geracao))
        while len(nova_populacao) < EvAlg.TAMANHO_POPULACAO:
            pais    = EvAlg.selecao(populacao)
            filhos  = EvAlg.crossover(pais)
            nova_populacao.append(filhos[0])
            nova_populacao.append(filhos[1])

        populacao = nova_populacao
        EvAlg.validarFitness(populacao)

    print("Final do processo. A populacao atual é a seguinte")
    for i in populacao:
        print(i.cromossomos)