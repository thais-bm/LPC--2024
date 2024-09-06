"""2) Palíndromo.
Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da
direita para esquerda ou vice−versa.
Por exemplo: OSSO e OVO são palíndromos.
Em textos mais complexos os espaços e pontuação são ignorados.
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram
ignorados.
Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um
palíndromo ou não.
"""


def receber_palavra_frase():
    """ Pede para o usuario digitar uma palavra/frase + exibir
    retorna: palavra_frase
    """
    print('--x--x-- Detector de Palíndromos --x--x--')
    palavra_frase = str(input("Digite uma palavra ou frase: "))
    print(f'Você digitou: {palavra_frase}')
    return palavra_frase


def analisar_palindromo(palavra_frase):
    """Remover todos os espacos + palavra minuscula
    Inverte a palavra
    Verifica se é igual a palavra recebida
    Recebe: palavra_frase -- retorna: Nada
    """
    palavra_frase_sem_espaco = palavra_frase.replace(' ', '').lower()
    string_invertida = palavra_frase_sem_espaco[::-1]

    if palavra_frase_sem_espaco == string_invertida:
        print(f'{palavra_frase} é um Palíndromo.')
    else:
        print(f'{palavra_frase} não é um Palíndromo.')


TEXTO = receber_palavra_frase()
analisar_palindromo(TEXTO)
