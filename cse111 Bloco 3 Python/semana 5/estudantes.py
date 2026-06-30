
"""
Uma tarefa comum para muitas pessoas que trabalham com informações
é usar um número, chave ou ID para buscar informações sobre uma pessoa.
Por exemplo, uma pessoa pode usar um número de telefone ou endereço de e-mail
como uma chave para encontrar (ou pesquisar) informações adicionais sobre um cliente.
Durante esta atividade, sua equipe escreverá um programa em Python que
usa o número de identificação (ID) de um estudante para buscar o nome do estudante.
"""
import csv


def main():
    # Os cabeçalhos das colunas e seus índices.
    INDICE_ID = 0
    INDICE_NOME = 1

    # Lê o conteúdo de um arquivo CSV chamado estudantes.csv
    # em um dicionário chamado dic_estudantes. Usa o ID
    # como a chave no dicionário.
    dic_estudantes = ler_dicionario("estudantes.csv", INDICE_ID)

    # Solicita ao usuário um número de identificação.
    id_usuario = input("Por favor, digite um número de identificação (xx-xxx-xxxx): ")

    # Os números de identificação estão armazenados no arquivo CSV como apenas dígitos
    # (sem traços), então removemos todos os traços da entrada do usuário.
    id_usuario = id_usuario.replace("-", "")

    # Verifica se a entrada do usuário está formatada corretamente.
    # "if not" significa "se não", ou seja, execute o bloco se a condição for falsa.
    if not id_usuario.isdigit():
        print("Número de identificação inválido: caractere inválido")
    else:
        if len(id_usuario) < 9:
            print("Número de identificação inválido: dígitos insuficientes")
        elif len(id_usuario) > 9:
            print("Número de identificação inválido: ultrapassa o limite de dígitos")
        else:
            # A entrada do usuário é um ID válido. Verifica
            # se o ID está presente na lista.
            if id_usuario not in dic_estudantes:
                print("Estudante inexistente")
            else:
                # Recupera o nome do estudante correspondente
                # ao ID informado pelo usuário.
                valor = dic_estudantes[id_usuario]
                nome = valor[INDICE_NOME]

                # Exibe o nome do estudante.
                print(nome)


def ler_dicionario(nome_arquivo, indice_coluna_chave):
    """Lê o conteúdo de um arquivo CSV em um dicionário composto
    e retorna o dicionário.

    Parâmetros:
        nome_arquivo: o nome do arquivo CSV a ser lido.
        indice_coluna_chave: o índice da coluna
            a ser usada como chave no dicionário.
    Retorno: um dicionário composto que contém
        o conteúdo do arquivo CSV.
    """
    # Cria um dicionário vazio que irá
    # armazenar os dados do arquivo CSV.
    dicionario = {}

    # Abre o arquivo CSV para leitura e armazena uma referência
    # ao arquivo aberto em uma variável chamada arquivo_csv.
    with open(nome_arquivo, "rt", encoding="utf-8") as arquivo_csv:

        # Usa o módulo csv para criar um objeto leitor
        # que irá ler do arquivo CSV aberto.
        leitor = csv.reader(arquivo_csv)

        # A primeira linha do arquivo CSV contém os cabeçalhos
        # das colunas e não os dados, então esta instrução pula
        # a primeira linha do arquivo.
        next(leitor)

        # Lê as linhas do arquivo CSV uma por uma.
        # O objeto leitor retorna cada linha como uma lista.
        for linha in leitor:

            # Da linha atual, recupera os dados
            # da coluna que contém a chave.
            chave = linha[indice_coluna_chave]

            # Armazena os dados da linha atual
            # no dicionário.
            dicionario[chave] = linha

    # Retorna o dicionário.
    return dicionario


# Se este arquivo for executado assim:
# > python estudantes.py
# então chama a função main. Entretanto, se este arquivo
# for apenas importado, a chamada ao main é ignorada.
if __name__ == "__main__":
    main()