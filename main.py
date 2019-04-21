import random
from besouro import Besouro

TAMANHO_POPULACAO = 10


def inicializarPopulacao():
    print('Inicializando a população')

    def besouroAleatorio():
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return Besouro(red, green, blue)

    populacaoInicial = [besouroAleatorio() for x in range(TAMANHO_POPULACAO)]
    return populacaoInicial


def printarPopulacao(populacao: list):
    for individuo in populacao:
        print(fitnessFunction(individuo))


def fitnessFunction(besouro: Besouro):
    corTotal = besouro.getRed() + besouro.getGreen() + besouro.getBlue()
    return 1 - (corTotal / 765)


def selecionarIndividuos(populacao: list, quantidadeParaSelecionar):
    print('Selecionando individuos')
    populacao.sort(key=fitnessFunction)
    individuosSelecionados = [populacao.pop() for i in range(quantidadeParaSelecionar)]
    return individuosSelecionados


quantidadeParaSelecionar = int(round(TAMANHO_POPULACAO / 2))

populacaoInicial = inicializarPopulacao()
individuosSelecionados = selecionarIndividuos(populacaoInicial, quantidadeParaSelecionar)
