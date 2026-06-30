"""Verifique se as funções prefixo e sufixo funcionam corretamente."""

from palavras import prefixo, sufixo
import pytest


def test_prefixo():
    """Verifique se a função prefixo funciona corretamente.
    Parâmetros: nenhum
    Retorno: nada
    """
    # Chama a função prefixo e verifica se ela retorna uma string.
    pre = prefixo("antioxidante", "antiderrapante")
    assert isinstance(pre, str), "a função prefixo deve retornar uma string"

# Chama a função prefixo dez vezes e use uma instrução assert
# para verificar se a string retornada pela função prefixo
# está correta a cada vez.
    assert prefixo("", "") == ""
    assert prefixo("", "correto") == ""
    assert prefixo("imparcial", "") == ""
    assert prefixo("autoescola", "marinha") == ""
    assert prefixo("submarino", "subproduto") == "sub"
    assert prefixo("intermunicipal", "interestadual") == "inter"
    assert prefixo("antissocial", "alento") == "a"
    assert prefixo("supermercado", "superlotado") == "super"
    assert prefixo("hipermercado", "hipertexto") == "hiper"

# Chama a função principal que faz parte do pytest para que o
# computador executa as funções de teste neste arquivo.
pytest.main(["-v", "--tb=line", "-rN", __file__])
