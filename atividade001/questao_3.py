"""3) Verificação de cpf.
Desenvolva um programa que solicite a digitação de um número
de cpf no formato xxx.xxx.xxx-xx.
Indique se é um número válido ou inválido através da validação
dos dígitos verificadores e dos caracteres de formatação.
"""


def receber_cpf():
    """ Recebe o CPF + exibe o que o usuário escreveu
    - retorna: CPF
    """
    print('--x--x-- Verificador de CPFs --x--x--')
    cpf = str(input("Digite um CPF no formato xxx.xxx.xxx-xx: "))
    print(f'Você digitou: {cpf}.')
    return cpf


def analisar_caracteres_formacao(cpf):
    """ Verifica se o CPF corresponde a seguinte formação:
    - CPF possui 14 caracteres (11 numeros e 3 caract. especiais).
    - Posição do Ponto = 3 e 7; Posição do Traço = 11
    - retorna: valor booleano aux
    """
    aux = False
    if len(cpf) == 14:
        if (cpf[3] == '.' and
            cpf[7] == '.' and
                cpf[11] == '-'):
            aux = True
        else:
            print('CPF inválido!\n'
                  + 'Motivo: Posição incorreta dos pontos e/ou traço.')
    else:
        print('CPF inválido!\n'
              + 'Motivo: Número informado diferente de 14 caracteres.)')
    return aux


def analisar_digitos_verificadores(cpf):
    """Recebe cpf
    - Remove caracteres especiais + converte string -> numero
    - Verificacao via digito verificador (2 ultimos do cpf)
    retorna: aux
    """
    aux = False
    cpf_sem_caracteres = []
    for numero in cpf:
        if numero not in ('.', '-'):
            cpf_sem_caracteres.append(int(numero))

    # 1o digito = resto da divisao do termo do cpf x posicao (a partir do 1)) por 11
    soma_verificacao = 0
    for numero in range(len(cpf_sem_caracteres[:9])):
        soma_verificacao += (cpf_sem_caracteres[numero] * (numero+1))

    primeiro_digito_verificador = soma_verificacao % 11
    if primeiro_digito_verificador == 10:
        primeiro_digito_verificador = 0

    # 2o digito = resto da divisao do (termo do cpf+1o digito) * sua posicao (a partir do 0) por 11)
    soma_verificacao = 0
    for numero in range(len(cpf_sem_caracteres[:10])):
        soma_verificacao += (cpf_sem_caracteres[numero]*numero)

    segundo_digito_verificador = soma_verificacao % 11
    if segundo_digito_verificador == 10:
        segundo_digito_verificador = 0

    # Verifica se ambos os digitos sao válidos
    if (cpf_sem_caracteres[9] == primeiro_digito_verificador and
            cpf_sem_caracteres[10] == segundo_digito_verificador):
        aux = True
    else:
        print('CPF inválido!\n'
              + 'Motivo: Os dígitos verificadores não coincidem')
    return aux


def validar_cpf():
    """Inicia as funcoes
    2 analises validas: CPF válido
    """
    cpf = receber_cpf()
    if (analisar_caracteres_formacao(cpf) and
            analisar_digitos_verificadores(cpf)):
        print('CPF válido!')


validar_cpf()
