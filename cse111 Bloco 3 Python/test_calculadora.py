import pytest
from calculadora_de_notas import calcular_media, verificar_aprovacao

#  Testes para a função calcular_media()

# Testa se a média é calculada corretamente com notas altas.
def test_calcular_media_aprovado():
    notas = {"Ciências": 8.0, "Matemática": 7.0, "Língua Portuguesa": 9.0}
    assert calcular_media(notas) == 8.0

# Testa se a média é calculada corretamente com notas baixas.
def test_calcular_media_reprovado():
    notas = {"Ciências": 5.0, "Matemática": 4.0, "Língua Portuguesa": 6.0}
    assert calcular_media(notas) == 5.0

# Testa o caso exato do limite de aprovação (média 7.0).
def test_calcular_media_limite():
    notas = {"Ciências": 7.0, "Matemática": 7.0, "Língua Portuguesa": 7.0}
    assert calcular_media(notas) == 7.0

# Testes para a função verificar_aprovacao

# Testa'Aprovado' para média igual a 7.0.
def test_verificar_aprovacao():
    assert verificar_aprovacao(7.0) == "Aprovado"

# Testa 'Aprovado' para média acima de 7.0.
def test_verificar_aprovacao_acima():
    assert verificar_aprovacao(9.0) == "Aprovado"

# Testa'Reprovado' para média abaixo de 7.0.
def test_verificar_reprovacao():
    assert verificar_aprovacao(6.9) == "Reprovado"
