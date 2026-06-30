"""
Autor: João Augusto Ferreira

S03 - Projeto: Pressão da Água

"""

from pytest import approx
import pytest
  
# Colocando as funções água altura e torre

from fluxo_de_agua import (
    calc_altura_coluna_agua, 
    calc_pressao_pela_altura, 
    calc_perda_pressao_tubo,
    calc_perda_pressao_conexoes,
    calc_num_reynolds,
    calc_perda_pressao_reducao_tubo
)
def test_calc_altura_coluna_agua():
    assert calc_altura_coluna_agua(0.0, 0.0) == approx(0.0)
    assert calc_altura_coluna_agua(0.0, 10.0) == approx(7.5)
    assert calc_altura_coluna_agua(25.0, 0.0) == approx(25.0)
    assert calc_altura_coluna_agua(48.3, 12.8) == approx(57.9)

def test_calc_pressao_pela_altura():
    assert calc_pressao_pela_altura(0.0) == approx(0.00, abs=0.001)
    assert calc_pressao_pela_altura(30.2) == approx(295.628, abs=0.001)
    assert calc_pressao_pela_altura(50.0) == approx(489.450, abs=0.001)
    
def test_calc_perda_pressao_tubo():
    assert calc_perda_pressao_tubo(0.048692, 0.00, 0.018, 1.75) == approx(0.000, abs=0.001)
    assert calc_perda_pressao_tubo(0.048692, 200.00, 0.00, 1.75) == approx(0.000, abs=0.001)
    assert calc_perda_pressao_tubo(0.048692, 200.00, 0.018, 0.00) == approx(0.000, abs=0.001)
    assert calc_perda_pressao_tubo(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert calc_perda_pressao_tubo(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert calc_perda_pressao_tubo(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert calc_perda_pressao_tubo(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)

# Segunda parte

def test_calc_perda_pressao_conexoes():
    assert calc_perda_pressao_conexoes(0.00, 3) == approx(0.000, abs=0.001)
    assert calc_perda_pressao_conexoes(1.65, 0) == approx(0.000, abs=0.001)
    assert calc_perda_pressao_conexoes(1.65, 2) == approx(-0.109, abs=0.001)
    assert calc_perda_pressao_conexoes(1.75, 2) == approx(-0.122, abs=0.001)
    assert calc_perda_pressao_conexoes(1.75, 5) == approx(-0.306, abs=0.001)

def test_calc_num_reynolds():
    assert calc_num_reynolds(0.048692, 0.00) == approx(0, abs=1)
    assert calc_num_reynolds(0.048692, 1.65) == approx(80069, abs=1)
    assert calc_num_reynolds(0.048692, 1.75) == approx(84922, abs=1)
    assert calc_num_reynolds(0.286870, 1.65) == approx(471729, abs=1)
    assert calc_num_reynolds(0.286870, 1.75) == approx(500318, abs=1)

def test_calc_perda_pressao_reducao_tubo():
    assert calc_perda_pressao_reducao_tubo(0.286870, 0.00, 1, 0.048692) == approx(0.000, abs=0.001)
    assert calc_perda_pressao_reducao_tubo(0.286870, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert calc_perda_pressao_reducao_tubo(0.286870, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)

# Chama a função main que faz parte do pytest para que o
# o computador execute as funções de teste neste arquivo.
pytest.main(["-v", "--tb=line", "-rN", __file__])