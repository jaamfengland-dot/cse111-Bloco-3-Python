"""
Autor: João Augusto Ferreira

S02 - Projeto: forca da Senha

"""

MINUSCULAS=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
MAIUSCULAS=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITOS=["0","1","2","3","4","5","6","7","8","9"]
ESPECIAIS=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

# Adicionando a função palavra_no_arquivo

def palavra_no_arquivo(palavra, nome_do_arquivo, diferencia_maiusculas=False):

    arquivo = open(nome_do_arquivo, "r", encoding="utf-8")

    for linha in arquivo:

        linha = linha.strip()

        if diferencia_maiusculas:

            if palavra == linha:
                arquivo.close()
                return True

        else:

            if palavra.lower() == linha.lower():
                arquivo.close()
                return True

    arquivo.close()
    return False

# Adicionando a função palavra_tem_caracteres (corrigido)

def palavra_tem_caracteres(palavra, lista_de_caracteres):
    for c in palavra:
        if c in lista_de_caracteres:
            return True

    return False  
# Adicionando a função complexidade_de_palavras

def complexidade_de_palavras(palavra):

    forca  = 0

    if palavra_tem_caracteres(palavra, MINUSCULAS):
        forca  += 1

    if palavra_tem_caracteres(palavra, MAIUSCULAS):
        forca  += 1

    if palavra_tem_caracteres(palavra, DIGITOS):
        forca  += 1

    if palavra_tem_caracteres(palavra, ESPECIAIS):
        forca  += 1

    return forca

# Adicionando a função forca_da_senha

def forca_da_senha(senha, comprimento_min=10, comprimento_forte=16):

    # Arquivo do dicionário 
    if palavra_no_arquivo(senha, "lista_de_palavras.txt"):
        print("A  sua senha está no dicionário e não é segura.")
        return 0

    # senhas comuns
    if palavra_no_arquivo(senha, "senhas_mais_comuns.txt", True):
        print("A senha é muito comum e não é segura.")
        return 0

    # senhas curta
    if len(senha) < comprimento_min:
        print("A senha é muito curta e não é segura.")
        return 1

    # senha forte
    if len(senha) >= comprimento_forte:
        print("A senha é muito longa e muito forte.")
        return 5

    #  normal
    forca = complexidade_de_palavras(senha)

    return 1 + forca

# Adicionando a função main

def main():

    while True:

        senha = input("Digite uma senha (digite Q se quiser sair): ")

        if senha.lower() == "q":
         break

        forca = forca_da_senha(senha)

        print("forca da senha:", forca)

# Final
if __name__ == "__main__":
    main()