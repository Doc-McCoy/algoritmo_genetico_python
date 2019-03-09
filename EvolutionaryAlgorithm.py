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


    def validarFitness(self, individuo):
        ''' Testa uma população e retorna quantos pontos ela fez,
        baseado na comparação dos valores de seus elementos com a
        lista RESULTADO_ESPERADO. '''

        esperado    = self.RESULTADO_ESPERADO
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

        pai_a, pai_b = pais
        metade_do_cromossomo = int(self.TAMANHO_CROMOSSOMO / 2)

        cromossomos_iniciais_pai_a  = pai_a.cromossomos[ : metade_do_cromossomo]
        cromossomos_finais_pai_a    = pai_a.cromossomos[metade_do_cromossomo : ]

        

    def mutacao(self):
        pass



pp = PrettyPrinter(indent=4)

EvAlg       = EvolutionaryAlgorithm()
populacao   = EvAlg.criarPopulacao()
for individuo in populacao:
    EvAlg.validarFitness(individuo)
selecionados = EvAlg.selecao(populacao)
filhos = EvAlg.crossover(selecionados)
