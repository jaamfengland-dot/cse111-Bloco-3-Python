# Copyright 2020, Brigham Young University-Idaho. Todos os direitos reservados.

from estudantes import ler_dicionario
from inspect import signature
from os import path
from tempfile import mkstemp
import pytest
import os


def test_ler_dicionario():
    """Verifica se a função ler_dicionario está funcionando corretamente."""
    INDICE_ID = 0

    # Verifica se a função ler_dicionario usa seu parâmetro de nome de arquivo
    # da seguinte maneira:
    # 1. Obtém um nome de arquivo que não existe.
    # 2. Chama a função ler_dicionario com esse nome de arquivo.
    # 3. Verifica se a função open, dentro de ler_dicionario, levanta um FileNotFoundError.
    fd, arquivo_temporario = mkstemp(dir=".", prefix="nao_existe", suffix=".csv")  # Correção: nome correto da variável
    os.close(fd)  # Fecha o arquivo temporário
    os.remove(arquivo_temporario)  # Remove o arquivo temporário para simular "arquivo inexistente"

    with pytest.raises(FileNotFoundError):
        chamar_ler_dicionario(arquivo_temporario, INDICE_ID)  # Agora passando o nome correto do arquivo
        pytest.fail("A função ler_dicionario deve usar seu parâmetro de nome de arquivo")

    # Agora chama com o arquivo real
    nome_arquivo = path.join(path.dirname(__file__), "estudantes.csv")  # Certifique-se de que o arquivo existe
    dicionario_estudantes = chamar_ler_dicionario(nome_arquivo, INDICE_ID)

    # Verifica se a função retornou um dicionário.
    assert isinstance(dicionario_estudantes, dict), \
        "A função ler_dicionario deve retornar um dicionário: " \
        f"esperado um dicionário, mas foi retornado {type(dicionario_estudantes)}"

    # Verifica se o dicionário contém exatamente nove itens.
    tamanho = len(dicionario_estudantes)
    TAMANHO_ESPERADO = 9
    assert tamanho == TAMANHO_ESPERADO, \
        "O dicionário de estudantes contém " \
        f"{'menos' if tamanho < TAMANHO_ESPERADO else 'mais'} itens: " \
        f"esperava {TAMANHO_ESPERADO}, mas encontrou {tamanho}"

    # Verifica se os dados dos nove estudantes estão corretos.
    # Verifica se os dados dos nove estudantes estão corretos.
    verificar_estudante(dicionario_estudantes, "751766201", "Tiago Silva")
    verificar_estudante(dicionario_estudantes, "751762102", "Ester Oliveira")
    verificar_estudante(dicionario_estudantes, "052058203", "Carlos Benitez")
    verificar_estudante(dicionario_estudantes, "323021604", "Marcelo Rocha")
    verificar_estudante(dicionario_estudantes, "251041405", "Joel Rocha")
    verificar_estudante(dicionario_estudantes, "001152306", "Bruna Rios")
    verificar_estudante(dicionario_estudantes, "182706207", "Henrique Prado")
    verificar_estudante(dicionario_estudantes, "124712708", "Marina Tomas")
    verificar_estudante(dicionario_estudantes, "212505409", "Carlos Pereira")


def chamar_ler_dicionario(nome_arquivo, indice_coluna_chave):
    """Chama a função ler_dicionario com o número correto de parâmetros."""
    sig = signature(ler_dicionario)
    quantidade_parametros = len(sig.parameters)
    MIN_PARAM = 1
    MAX_PARAM = 2
    assert quantidade_parametros == MIN_PARAM or quantidade_parametros == MAX_PARAM, \
        "A função ler_dicionario contém " \
        f"{'poucos' if quantidade_parametros < MIN_PARAM else 'muitos'} parâmetros; " \
        f"esperava {MIN_PARAM} ou {MAX_PARAM}, mas encontrou {quantidade_parametros}"
    
    if quantidade_parametros == MIN_PARAM:
        dicionario = ler_dicionario(nome_arquivo)
    else:
        dicionario = ler_dicionario(nome_arquivo, indice_coluna_chave)
    return dicionario


def verificar_estudante(dicionario_estudantes, id_estudante, nome_esperado):
    """Verifica se os dados de um estudante no dicionário estão corretos."""

    # Verifica se o número de identificação está no dicionário.
    assert id_estudante in dicionario_estudantes, \
        f'"{id_estudante}" está ausente no dicionário de estudantes.'

    valor_obtido = dicionario_estudantes[id_estudante]
    assert isinstance(valor_obtido, str) or isinstance(valor_obtido, list), \
        "Cada valor no dicionário de estudantes deve ser uma string " \
        f"ou uma lista. O valor para {id_estudante} é do tipo {type(valor_obtido)} " \
        "que não é uma string nem uma lista."

    if isinstance(valor_obtido, str):
        # Verifica se o nome do estudante está correto.
        assert valor_obtido == nome_esperado, \
            f'Nome incorreto para "{id_estudante}"; ' \
            f'esperava "{nome_esperado}", mas encontrou"{valor_obtido}"'
    else:
        tamanho = len(valor_obtido)
        min_len = 1
        max_len = 2
        assert tamanho == min_len or tamanho == max_len, \
            f"A lista de valores para o estudante {id_estudante} contém " \
            f"{'poucos' if tamanho < min_len else 'muitos'} elementos; " \
            f"esperado {min_len} ou {max_len}, mas encontrado {tamanho}"

        if tamanho == min_len:
            # Verifica se o nome do estudante está correto.
            INDICE_NOME = 0
            nome_obtido = valor_obtido[INDICE_NOME]
            assert nome_obtido == nome_esperado, \
                f'Nome incorreto para "{id_estudante}"; ' \
                f'esperava "{nome_esperado}", mas encontrou "{nome_obtido}"'
        else:
            # Verifica se o número de identificação do estudante está correto.
            INDICE_ID = 0
            id_obtido = valor_obtido[INDICE_ID]
            assert id_obtido == id_estudante, \
                'Inconsistência entre a chave e o valor. ' \
                f'A chave é {id_estudante}, mas {id_obtido} está no valor correspondente.'

            # Verifica se o nome do estudante está correto.
            INDICE_NOME = 1
            nome_obtido = valor_obtido[INDICE_NOME]
            assert nome_obtido == nome_esperado, \
                f'Nome incorreto para "{id_estudante}"; ' \
                f'esperava "{nome_esperado}", mas encontrou "{nome_obtido}"'


# Chama a função principal do pytest para executar os testes neste arquivo.
pytest.main(["-v", "--tb=line", "-rN", __file__])
