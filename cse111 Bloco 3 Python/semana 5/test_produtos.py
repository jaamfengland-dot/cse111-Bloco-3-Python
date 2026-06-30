# Copyright 2020, Brigham Young University-Idaho. Todos os direitos reservados.

from recibo import ler_dicionario
from os import path
from tempfile import mktemp
from pytest import approx
import pytest


def test_ler_dicionario():
    """Verifica se a função ler_dicionario está funcionando corretamente.
    Parâmetros: nenhum
    Retorno: nenhum
    """
    INDICE_PRODUTO = 0

    # Verifica se a função ler_dicionario usa seu parâmetro de nome de arquivo
    # da seguinte maneira:
    # 1. Obtém um nome de arquivo que não existe.
    # 2. Chama a função ler_dicionario com esse nome de arquivo.
    # 3. Verifica se a função open, dentro de ler_dicionario, levanta um FileNotFoundError.
    # nome_arquivo = mktemp(dir=".", prefix="nao_existe", suffix=".csv")
    # with pytest.raises(FileNotFoundError):
    #     ler_dicionario(nome_arquivo, INDICE_PRODUTO)
    #     pytest.fail("A função ler_dicionario deve usar seu parâmetro de nome de arquivo")

    # Chama a função ler_dicionario e armazena o dicionário retornado
    # em uma variável chamada dic_produtos.
    nome_arquivo = path.join(path.dirname(__file__), "produtos.csv")
    dic_produtos = ler_dicionario(nome_arquivo, INDICE_PRODUTO)

    # Verifica se a função ler_dicionario retorna um dicionário.
    assert isinstance(dic_produtos, dict), \
        "A função ler_dicionario deve retornar um dicionário:" \
        f" esperado um dicionário mas foi retornado {type(dic_produtos)}"

    # Verifica se o dicionário de produtos contém exatamente 16 itens.
    tamanho = len(dic_produtos)
    TAMANHO_ESPERADO = 16
    assert tamanho == TAMANHO_ESPERADO, \
        "O dicionário de produtos contém " \
        f"{'menos' if tamanho < TAMANHO_ESPERADO else 'mais'} itens:" \
        f" esperado {TAMANHO_ESPERADO} mas encontrado {tamanho}"

    # Verifica cada item no dicionário de produtos.
    verificar_produto(dic_produtos, "D150", ["1 litro de leite", 2.85])
    verificar_produto(dic_produtos, "D083", ["1 copo de iogurte", 0.75])
    verificar_produto(dic_produtos, "D215", ["450g de queijo cheddar", 3.35])
    verificar_produto(dic_produtos, "P019", ["alface americana", 1.15])
    verificar_produto(dic_produtos, "P020", ["alface crespa", 1.79])
    verificar_produto(dic_produtos, "P021", ["alface manteiga", 1.83])
    verificar_produto(dic_produtos, "P025", ["embalagem de rúcula (227g)", 2.19])
    verificar_produto(dic_produtos, "P143", ["450g de mini cenouras", 1.39])
    verificar_produto(dic_produtos, "W231", ["pacote de granola (907g)", 3.21])
    verificar_produto(dic_produtos, "W112", ["pão de trigo", 2.55])
    verificar_produto(dic_produtos, "C013", ["barrinha de chocolate Twix", 0.85])
    verificar_produto(dic_produtos, "H001", ["8 rolos de papel higiênico", 6.45])
    verificar_produto(dic_produtos, "H014", ["1 caixa de cotonetes (75 unidades)", 2.49])
    verificar_produto(dic_produtos, "H020", ["1 esponja de limpeza", 2.39])
    verificar_produto(dic_produtos, "H021", ["frasco de detergente (354ml)", 3.19])
    verificar_produto(dic_produtos, "H025", ["limpador de vaso sanitário", 4.50])



def verificar_produto(dic_produtos, numero_produto, valor_esperado):
    """Verifica se os dados de um produto no dicionário estão corretos.

    Parâmetros:
        dic_produtos: um dicionário que contém dados dos produtos
        numero_produto: o número do produto que esta função vai verificar
        valor_esperado: os dados que deveriam estar no dicionário para este número de produto
    Retorno: nenhum
    """
    assert numero_produto in dic_produtos
    valor_obtido = dic_produtos[numero_produto]
    tamanho = len(valor_obtido)
    MIN_TAM = 2
    MAX_TAM = 3
    assert MIN_TAM <= tamanho <= MAX_TAM, \
        f"A lista de valores para o produto {numero_produto} contém " \
        f"{'poucos' if tamanho < MIN_TAM else 'muitos'} elementos:" \
        f" esperado {MIN_TAM} ou {MAX_TAM} elementos mas encontrado {tamanho}"

    if tamanho == MIN_TAM:
        INDICE_NOME = 0
        INDICE_PRECO = 1
    else:
        INDICE_NOME = 1
        INDICE_PRECO = 2

    # Verifica se o nome do produto está correto.
    nome_obtido = valor_obtido[INDICE_NOME]
    nome_esperado = valor_esperado[0]
    assert nome_obtido == nome_esperado, \
        f"Nome incorreto para o produto {numero_produto}: " \
        f"esperado {nome_esperado} mas encontrado {nome_obtido}"

    # Verifica se o preço do produto está correto.
    preco_obtido = valor_obtido[INDICE_PRECO]
    if isinstance(preco_obtido, str):
        preco_obtido = float(preco_obtido)
    preco_esperado = valor_esperado[1]
    assert preco_obtido == approx(preco_esperado), \
        f"Preço incorreto para o produto {numero_produto}: " \
        f"esperado {preco_esperado} mas encontrado {preco_obtido}"


# Chama a função principal do pytest para executar os testes neste arquivo.
pytest.main(["-v", "--tb=line", "-rN", __file__])
