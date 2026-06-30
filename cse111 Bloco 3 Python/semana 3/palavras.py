# Copyright 2020, Universidade Brigham Young-Idaho. Todos os direitos reservados.

def prefixo(texto1, texto2):
    """Retorna o prefixo, se houver, que aparece tanto em texto1
    quanto em texto2. Em outras palavras, retorna uma string com
    os caracteres que aparecem no início de texto1 e texto2.
    Exemplo: se texto1 for "inconcebível" e texto2 for
    "inconveniente", esta função retornará "incon".

    Parâmetros
        texto1: uma string de texto
        texto2: outra string de texto
    Retorna: uma string
    """
    # Converte ambas as strings para letras minúsculas.
    texto1 = texto1.lower()
    texto2 = texto2.lower()

    # Começa no início de ambas as strings.
    i = 0

    # Repete até encontrar dois caracteres diferentes.
    limite = min(len(texto1), len(texto2))
    while i < limite:
        if texto1[i] != texto2[i]:
            break
        i += 1

    # Extrai o prefixo de texto1 e retorna.
    pre = texto1[0:i]
    return pre


def sufixo(texto1, texto2):
    """Retorna o sufixo, se houver, que aparece tanto em texto1
    quanto em texto2. Em outras palavras, retorna uma string com
    os caracteres que aparecem no final de texto1 e texto2.
    Exemplo: se texto1 for "salada" e texto2 for "marinada",
    esta função retornará "ada".

    Parâmetros
        texto1: uma string de texto
        texto2: outra string de texto
    Retorna: uma string
    """
    # Converte ambas as strings para letras minúsculas.
    texto1 = texto1.lower()
    texto2 = texto2.lower()

    # Começa no final de ambas as strings.
    i1 = len(texto1) - 1
    i2 = len(texto2) - 1

    # Repete até encontrar dois caracteres diferentes.
    limite = min(len(texto1), len(texto2))
    for _ in range(limite):
        if texto1[i1] != texto2[i2]:
            break
        i1 -= 1
        i2 -= 1

    # Extrai o sufixo de texto1 e retorna.
    suf = texto1[i1+1:]
    return suf