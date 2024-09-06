"""5) Jogo de Forca.
 Desenvolva um jogo da forca.
 O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
 O jogador poderá errar 6 vezes antes de ser enforcado.
"""

import sys
import random


def ler_arquivos():
    """ leitura: caminho do arquivo .txt
    - Caso arquivo não seja txt -> Mostrar erro FileNotFound
    - Ler arquivo e salvar numa lista cada linha
    - remover o '\n' do final de cada elemento
    Return: lista_palavras
    """
    path_file = str(sys.argv[1])
    if path_file.endswith('.txt'):
        with open(path_file, 'r', encoding='UTF-8') as lista:
            palavras_com_quebra = lista.readlines()
        lista_palavras = []
        for item in palavras_com_quebra:
            lista_palavras.append(item.strip('\n').lower())
    else:
        raise FileNotFoundError("Arquivo inválido. Insira um caminho para arquivo .txt válido")
    return lista_palavras


def escolha_aleatoria(lista_palavras):
    """ Recebe: lista_palavras,
    Via random: escolhe uma palavra da lista + separacao por letra da palavra
    """
    index_palavra = random.randint(0, len(lista_palavras))
    palavra_sorteada = lista_palavras[index_palavra].lower()
    lista_letras = list(palavra_sorteada)

    return palavra_sorteada, lista_letras


def desenho_forca(chances):
    """Recebe: Chances
    De acordo com a quantidade de chances, um bonequinho vai aparecer
    """
    stickman_forca = ['''
  +----+
  |    |
  O    |
 /|\\   |
 / \\   |
       |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +----+
  |    |
  O    |
 /|\\   |
       |
       |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']
    print(stickman_forca[chances])


def jogo_da_forca(palavra, lista_letras):
    """ Recebe: palavra, lista letras
    - Apresentacao do jogo + dica + chances
    - Gameloop
    """
    letra_user = []
    chances = 6

    print('--xx--xx-- JOGO DA FORCA --xx--xx--')
    print('--xx-- Adivinhe a palavra da lista de palavras --xx--')
    print(f'Dica: A Palavra possui {len(palavra)} letras.')
    print(f"Você tem {chances} chances.")

    while True:
        # Se usr acertou uma letra, ela será exibida, caso não, aparece traço
        for letra in palavra:
            if letra.lower() in letra_user:
                print(letra, end=" ")
            else:
                print("_", end=" ")

        # Recebe letra, se tiver errada, perde uma chace + desenho da forca exibido
        tentativa = input('\n\nDigite uma letra: ')
        letra_user.append(tentativa.lower())

        if tentativa.lower() not in palavra.lower():
            chances = chances-1

        # Situação de vitória
        # Se tds letras_usr presentes na lista_letras
        vitoria = True
        for letra in lista_letras:
            if letra.lower() not in letra_user:
                vitoria = False
                break

        # Informação: qtde chances + desenho
        desenho_forca(chances)
        print(f"Você tem {chances} chances.")

        # Quebra do loop principal: acabou chances ou vitória
        if chances == 0 or vitoria:
            break

    if vitoria:
        print(f"Parabéns, você ganhou. A palavra era: {palavra}")
    else:
        print(f"Você perdeu! A palavra era: {palavra}")


lista_de_palavras = ler_arquivos()
palavra_escolhida, lista_de_letras = escolha_aleatoria(lista_de_palavras)
jogo_da_forca(palavra_escolhida, lista_de_letras)
