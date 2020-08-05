# https://medium.com/@rinu.gour123/python-genetic-algorithms-with-artificial-intelligence-b8d0c7db60ac

'''
    A idéia aqui é criar um algoritmo que vá dando palpites até descobrir
    a palavra secreta 'Hello World".

    Este algoritmo usa os seguintes operadores:
    - Operador de seleção: Seleciona os indivíduos com melhores fitness.
    - Operador de crossover: Mistura os cromossomos de 2 indivíduos para criar um novo.
    - Operador de mutação: Aleatoriamente altera um ou dois cromossomos para manter a diversidade.
'''

geneSet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.'
target = 'Hello.World!'

import random, datetime

def generate_parent(length):
    ''' Gera o primeiro gene de maneira aleatória e confusa. '''
    genes = []
    while len(genes) < length:
        sampleSize = min(length-len(genes), len(geneSet))
        genes.extend(random.sample(geneSet,sampleSize))
    return ''.join(genes)

def get_fitness(guess):
    ''' Verifica se a letra do cromossomo é a letra certa da palavra secreta. '''
    return sum(1 for expected, actual in zip(target, guess) if expected == actual)

def mutate(parent):
    index = random.randrange(0, len(parent))
    childGenes = list(parent)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate if newGene==childGenes[index] else newGene
    return ''.join(childGenes)

def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print("{}\t{}\t{}".format(guess, fitness, timeDiff))

random.seed()
startTime = datetime.datetime.now()
bestParent = generate_parent(len(target))
bestFitness = get_fitness(bestParent)
display(bestParent)

while True:
    child = mutate(bestParent)
    childFitness = get_fitness(child)
    if bestFitness >= childFitness:
        continue
    display(child)
    if childFitness >= len(bestParent):
        break
    bestFitness = childFitness
    bestParent = child
