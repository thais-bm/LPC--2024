"""4) Número por extenso.
Escreva um programa que solicite ao usuário a digitação de um número
até 99 e imprima-o na tela por extenso.
"""

menor_vinte = [
    'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 
    'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 
    'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
    'Dezenove',
    ]
dezenas = [
    'Vinte', 'Trinta', 'Quarenta', 'Cinquenta', 'Sessenta', 'Setenta', 'Oitenta', 'Noventa',
    ]


def receber_numero():
    """ Recebe o numero + exibe o que o usuário escreveu
    - retorna: numero
    """
    print('--x--x-- Números por Extenso --x--x--')
    numero = str(input("Digite um número até 99: "))
    return numero


def numeracao_extenso(numero):
    """
    Função para escrever um numero por extenso
    Recebe: numero -- Retorna: numero_extenso
    """
    # Numeros até 19 possuem uma forma singular de escrever
    if numero <= '19':
        numero_extenso = menor_vinte[int(numero)]

    # A partir do 20, pode ser necessário montagem de 'frases'
    else:
        numero_extenso = ''
        # Dezenas a partir de 2 até 9 (vinte -> oventa)
        if '2' <= numero[0] <= '9':
            # O vinte ta no indice zero, mas é representado pelo 2
            numero_extenso = dezenas[int(numero[0])-2]
            if '0' < numero[1] <= '9':
                # É adicionado a casa das unidades + 'e'
                numero_extenso += ' e '+menor_vinte[int(numero[1])]

    return numero_extenso


NUMERACAO = receber_numero()
NUMERO_EXTENSO = numeracao_extenso(NUMERACAO)
print(f'Você digitou: {NUMERO_EXTENSO}.')
