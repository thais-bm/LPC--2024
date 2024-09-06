""" 1) Dados
Faça um programa que simule um lançamento de dados.
Lance o dado 100 vezes e armazene os resultados em um vetor.
Depois, mostre quantas vezes cada valor foi conseguido.
Dica: use um vetor de contadores (1-6) e uma função para gerar
numeros aleatórios, simulando os lançamentos dos dados.
"""
import random


def lancamento_dados():
    """ Lançamento do dado 100 vezes via biblioteca random
    return: vetor_contador
    """
    vetor_contador = []
    for _ in range(100):
        vetor_contador.append(random.randint(1, 6))

    return vetor_contador

def contagem_dados(vetor_contador):
    """ Realiza a contagem de quantas vezes cada valor apareceu
    retorna: nada
    """
    for valor in range(1, 7):
        numero_aparicao = vetor_contador.count(valor)
        print(f'O número {valor} apareceu {numero_aparicao} vezes')


dado_lancado = lancamento_dados()
contagem_dados(dado_lancado)
