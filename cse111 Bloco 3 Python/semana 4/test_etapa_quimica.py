# Direitos Autorais 2020, Brigham Young University-Idaho. Todos os direitos reservados.

from quimica import criar_tabela_periodica
from pytest import approx
import pytest


# Estes são os índices dos
# elementos na tabela periódica.
NOME_INDICE = 0
MASSA_ATOMICA_INDICE = 1


def test_criar_tabela_periodica():
    """Verifique se a função criar_tabela_periodica funciona corretamente.
    Parâmetros: nenhum
    Retorno: nenhum
    """
    # Chame a função criar_tabela_periodica e armazene o dicionário
    # retornado em uma variável chamada dic_da_tabela_periodica .
    dic_da_tabela_periodica = criar_tabela_periodica()

    # Verifique se a função criar_tabela_periodica retorna um dicionário.
    assert isinstance(dic_da_tabela_periodica, dict), \
        "A função criar_tabela_periodica deve retornar um dicionário: " \
        f" era esperado um dicionário, mas foi encontrado um {type(dic_da_tabela_periodica)}"

    # Verifique cada item no dicionário da tabela periódica.
    verificar_elemento(dic_da_tabela_periodica, "Ac", ["Actínio", 227])
    verificar_elemento(dic_da_tabela_periodica, "Ag", ["Prata", 107.8682])
    verificar_elemento(dic_da_tabela_periodica, "Al", ["Alumínio", 26.9815386])
    verificar_elemento(dic_da_tabela_periodica, "Ar", ["Argônio", 39.948])
    verificar_elemento(dic_da_tabela_periodica, "As", ["Arsênio", 74.9216])
    verificar_elemento(dic_da_tabela_periodica, "At", ["Astato", 210])
    verificar_elemento(dic_da_tabela_periodica, "Au", ["Ouro", 196.966569])
    verificar_elemento(dic_da_tabela_periodica, "B", ["Boro", 10.811])
    verificar_elemento(dic_da_tabela_periodica, "Ba", ["Bário", 137.327])
    verificar_elemento(dic_da_tabela_periodica, "Be", ["Berílio", 9.012182])
    verificar_elemento(dic_da_tabela_periodica, "Bi", ["Bismuto", 208.9804])
    verificar_elemento(dic_da_tabela_periodica, "Br", ["Bromo", 79.904])
    verificar_elemento(dic_da_tabela_periodica, "C", ["Carbono", 12.0107])
    verificar_elemento(dic_da_tabela_periodica, "Ca", ["Cálcio", 40.078])
    verificar_elemento(dic_da_tabela_periodica, "Cd", ["Cádmio", 112.411])
    verificar_elemento(dic_da_tabela_periodica, "Ce", ["Cério", 140.116])
    verificar_elemento(dic_da_tabela_periodica, "Cl", ["Cloro", 35.453])
    verificar_elemento(dic_da_tabela_periodica, "Co", ["Cobalto", 58.933195])
    verificar_elemento(dic_da_tabela_periodica, "Cr", ["Cromo", 51.9961])
    verificar_elemento(dic_da_tabela_periodica, "Cs", ["Césio", 132.9054519])
    verificar_elemento(dic_da_tabela_periodica, "Cu", ["Cobre", 63.546])
    verificar_elemento(dic_da_tabela_periodica, "Dy", ["Disprósio", 162.5])
    verificar_elemento(dic_da_tabela_periodica, "Er", ["Érbio", 167.259])
    verificar_elemento(dic_da_tabela_periodica, "Eu", ["Európio", 151.964])
    verificar_elemento(dic_da_tabela_periodica, "F", ["Flúor", 18.9984032])
    verificar_elemento(dic_da_tabela_periodica, "Fe", ["Ferro", 55.845])
    verificar_elemento(dic_da_tabela_periodica, "Fr", ["Frâncio", 223])
    verificar_elemento(dic_da_tabela_periodica, "Ga", ["Gálio", 69.723])
    verificar_elemento(dic_da_tabela_periodica, "Gd", ["Gadolínio", 157.25])
    verificar_elemento(dic_da_tabela_periodica, "Ge", ["Germânio", 72.64])
    verificar_elemento(dic_da_tabela_periodica, "H", ["Hidrogênio", 1.00794])
    verificar_elemento(dic_da_tabela_periodica, "He", ["Hélio", 4.002602])
    verificar_elemento(dic_da_tabela_periodica, "Hf", ["Háfnio", 178.49])
    verificar_elemento(dic_da_tabela_periodica, "Hg", ["Mercúrio", 200.59])
    verificar_elemento(dic_da_tabela_periodica, "Ho", ["Hólmio", 164.93032])
    verificar_elemento(dic_da_tabela_periodica, "I", ["Iodo", 126.90447])
    verificar_elemento(dic_da_tabela_periodica, "In", ["Índio", 114.818])
    verificar_elemento(dic_da_tabela_periodica, "Ir", ["Irídio", 192.217])
    verificar_elemento(dic_da_tabela_periodica, "K", ["Potássio", 39.0983])
    verificar_elemento(dic_da_tabela_periodica, "Kr", ["Criptônio", 83.798])
    verificar_elemento(dic_da_tabela_periodica, "La", ["Lantânio", 138.90547])
    verificar_elemento(dic_da_tabela_periodica, "Li", ["Lítio", 6.941])
    verificar_elemento(dic_da_tabela_periodica, "Lu", ["Lutécio", 174.9668])
    verificar_elemento(dic_da_tabela_periodica, "Mg", ["Magnésio", 24.305])
    verificar_elemento(dic_da_tabela_periodica, "Mn", ["Manganês", 54.938045])
    verificar_elemento(dic_da_tabela_periodica, "Mo", ["Molibdênio", 95.96])
    verificar_elemento(dic_da_tabela_periodica, "N", ["Nitrogênio", 14.0067])
    verificar_elemento(dic_da_tabela_periodica, "Na", ["Sódio", 22.98976928])
    verificar_elemento(dic_da_tabela_periodica, "Nb", ["Nióbio", 92.90638])
    verificar_elemento(dic_da_tabela_periodica, "Nd", ["Neodímio", 144.242])
    verificar_elemento(dic_da_tabela_periodica, "Ne", ["Neônio", 20.1797])
    verificar_elemento(dic_da_tabela_periodica, "Ni", ["Níquel", 58.6934])
    verificar_elemento(dic_da_tabela_periodica, "Np", ["Neptúnio", 237])
    verificar_elemento(dic_da_tabela_periodica, "O", ["Oxigênio", 15.9994])
    verificar_elemento(dic_da_tabela_periodica, "Os", ["Ósmio", 190.23])
    verificar_elemento(dic_da_tabela_periodica, "P", ["Fósforo", 30.973762])
    verificar_elemento(dic_da_tabela_periodica, "Pa", ["Protactínio", 231.03588])
    verificar_elemento(dic_da_tabela_periodica, "Pb", ["Chumbo", 207.2])
    verificar_elemento(dic_da_tabela_periodica, "Pd", ["Paládio", 106.42])
    verificar_elemento(dic_da_tabela_periodica, "Pm", ["Promécio", 145])
    verificar_elemento(dic_da_tabela_periodica, "Po", ["Polônio", 209])
    verificar_elemento(dic_da_tabela_periodica, "Pr", ["Praseodímio", 140.90765])
    verificar_elemento(dic_da_tabela_periodica, "Pt", ["Platina", 195.084])
    verificar_elemento(dic_da_tabela_periodica, "Pu", ["Plutônio", 244])
    verificar_elemento(dic_da_tabela_periodica, "Ra", ["Rádio", 226])
    verificar_elemento(dic_da_tabela_periodica, "Rb", ["Rubídio", 85.4678])
    verificar_elemento(dic_da_tabela_periodica, "Re", ["Rênio", 186.207])
    verificar_elemento(dic_da_tabela_periodica, "Rh", ["Ródio", 102.9055])
    verificar_elemento(dic_da_tabela_periodica, "Rn", ["Radônio", 222])
    verificar_elemento(dic_da_tabela_periodica, "Ru", ["Rutênio", 101.07])
    verificar_elemento(dic_da_tabela_periodica, "S", ["Enxofre", 32.065])
    verificar_elemento(dic_da_tabela_periodica, "Sb", ["Antimônio", 121.76])
    verificar_elemento(dic_da_tabela_periodica, "Sc", ["Escândio", 44.955912])
    verificar_elemento(dic_da_tabela_periodica, "Se", ["Selênio", 78.96])
    verificar_elemento(dic_da_tabela_periodica, "Si", ["Silício", 28.0855])
    verificar_elemento(dic_da_tabela_periodica, "Sm", ["Samário", 150.36])
    verificar_elemento(dic_da_tabela_periodica, "Sn", ["Estanho", 118.71])
    verificar_elemento(dic_da_tabela_periodica, "Sr", ["Estrôncio", 87.62])
    verificar_elemento(dic_da_tabela_periodica, "Ta", ["Tântalo", 180.94788])
    verificar_elemento(dic_da_tabela_periodica, "Tb", ["Térbio", 158.92535])
    verificar_elemento(dic_da_tabela_periodica, "Tc", ["Tecnécio", 98])
    verificar_elemento(dic_da_tabela_periodica, "Te", ["Telúrio", 127.6])
    verificar_elemento(dic_da_tabela_periodica, "Th", ["Tório", 232.03806])
    verificar_elemento(dic_da_tabela_periodica, "Ti", ["Titânio", 47.867])
    verificar_elemento(dic_da_tabela_periodica, "Tl", ["Tálio", 204.3833])
    verificar_elemento(dic_da_tabela_periodica, "Tm", ["Túlio", 168.93421])
    verificar_elemento(dic_da_tabela_periodica, "U", ["Urânio", 238.02891])
    verificar_elemento(dic_da_tabela_periodica, "V", ["Vanádio", 50.9415])
    verificar_elemento(dic_da_tabela_periodica, "W", ["Tungstênio", 183.84])
    verificar_elemento(dic_da_tabela_periodica, "Xe", ["Xenônio", 131.293])
    verificar_elemento(dic_da_tabela_periodica, "Y", ["Ítrio", 88.90585])
    verificar_elemento(dic_da_tabela_periodica, "Yb", ["Itérbio", 173.054])
    verificar_elemento(dic_da_tabela_periodica, "Zn", ["Zinco", 65.38])
    verificar_elemento(dic_da_tabela_periodica, "Zr", ["Zircônio", 91.224])


def verificar_elemento(dic_da_tabela_periodica, simbolo, esperado):
    """Verifique se o elemento real que veio do
    dic_da_tabela_periodica contém os mesmos valores que o
    elemento esperado.

    Parâmetros
        simbolo: um símbolo de um elemento químico
        esperado: uma lista que contém os valores esperados para o símbolo
    Retorno: nenhum
    """
    # Verifique se o símbolo está no dicionário da tabela periódica.
    assert simbolo in dic_da_tabela_periodica, \
        f'"{simbolo}" está ausente do dicionário da tabela periódica.'
    atual = dic_da_tabela_periodica[simbolo]

    # Verifique se o nome do elemento está correto.
    nome_atual = atual[NOME_INDICE]
    nome_esperado = esperado[NOME_INDICE]
    assert nome_atual == nome_esperado, \
            f'nome incorreto para "{simbolo}": ' \
            f'esperado {nome_esperado}, mas encontrado {nome_atual}'

    # Verifique se a massa atômica do elemento está correta.
    massa_atual = atual[MASSA_ATOMICA_INDICE]
    massa_esperada = esperado[MASSA_ATOMICA_INDICE]
    assert massa_atual == approx(massa_esperada), \
            f"massa atômica incorreta para {nome_esperado}: " \
            f"esperado {massa_esperada} mas encontrado {massa_atual}"


# Chame a função main que faz parte do pytest para que o
# computador execute as funções de teste neste arquivo.
pytest.main(["-v", "--tb=line", "-rN", __file__])
