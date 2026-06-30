from formula import interpretar_formula

def criar_tabela_periodica():

    dic_da_tabela_periodica = {
        "Ac": ["Actínio", 227],
        "Ag": ["Prata", 107.8682],
        "Al": ["Alumínio", 26.9815386],
        "Ar": ["Argônio", 39.948],
        "As": ["Arsênio", 74.9216],
        "At": ["Astato", 210],
        "Au": ["Ouro", 196.966569],
        "B": ["Boro", 10.811],
        "Ba": ["Bário", 137.327],
        "Be": ["Berílio", 9.012182],
        "Bi": ["Bismuto", 208.9804],
        "Br": ["Bromo", 79.904],
        "C": ["Carbono", 12.0107],
        "Ca": ["Cálcio", 40.078],
        "Cd": ["Cádmio", 112.411],
        "Ce": ["Cério", 140.116],
        "Cl": ["Cloro", 35.453],
        "Co": ["Cobalto", 58.933195],
        "Cr": ["Cromo", 51.9961],
        "Cs": ["Césio", 132.9054519],
        "Cu": ["Cobre", 63.546],
        "Dy": ["Disprósio", 162.5],
        "Er": ["Érbio", 167.259],
        "Eu": ["Európio", 151.964],
        "F": ["Flúor", 18.9984032],
        "Fe": ["Ferro", 55.845],
        "Fr": ["Frâncio", 223],
        "Ga": ["Gálio", 69.723],
        "Gd": ["Gadolínio", 157.25],
        "Ge": ["Germânio", 72.64],
        "H": ["Hidrogênio", 1.00794],
        "He": ["Hélio", 4.002602],
        "Hf": ["Háfnio", 178.49],
        "Hg": ["Mercúrio", 200.59],
        "Ho": ["Hólmio", 164.93032],
        "I": ["Iodo", 126.90447],
        "In": ["Índio", 114.818],
        "Ir": ["Irídio", 192.217],
        "K": ["Potássio", 39.0983],
        "Kr": ["Criptônio", 83.798],
        "La": ["Lantânio", 138.90547],
        "Li": ["Lítio", 6.941],
        "Lu": ["Lutécio", 174.9668],
        "Mg": ["Magnésio", 24.305],
        "Mn": ["Manganês", 54.938045],
        "Mo": ["Molibdênio", 95.96],
        "N": ["Nitrogênio", 14.0067],
        "Na": ["Sódio", 22.98976928],
        "Nb": ["Nióbio", 92.90638],
        "Nd": ["Neodímio", 144.242],
        "Ne": ["Neônio", 20.1797],
        "Ni": ["Níquel", 58.6934],
        "Np": ["Neptúnio", 237],
        "O": ["Oxigênio", 15.9994],
        "Os": ["Ósmio", 190.23],
        "P": ["Fósforo", 30.973762],
        "Pa": ["Protactínio", 231.03588],
        "Pb": ["Chumbo", 207.2],
        "Pd": ["Paládio", 106.42],
        "Pm": ["Promécio", 145],
        "Po": ["Polônio", 209],
        "Pr": ["Praseodímio", 140.90765],
        "Pt": ["Platina", 195.084],
        "Pu": ["Plutônio", 244],
        "Ra": ["Rádio", 226],
        "Rb": ["Rubídio", 85.4678],
        "Re": ["Rênio", 186.207],
        "Rh": ["Ródio", 102.9055],
        "Rn": ["Radônio", 222],
        "Ru": ["Rutênio", 101.07],
        "S": ["Enxofre", 32.065],
        "Sb": ["Antimônio", 121.76],
        "Sc": ["Escândio", 44.955912],
        "Se": ["Selênio", 78.96],
        "Si": ["Silício", 28.0855],
        "Sm": ["Samário", 150.36],
        "Sn": ["Estanho", 118.71],
        "Sr": ["Estrôncio", 87.62],
        "Ta": ["Tântalo", 180.94788],
        "Tb": ["Térbio", 158.92535],
        "Tc": ["Tecnécio", 98],
        "Te": ["Telúrio", 127.6],
        "Th": ["Tório", 232.03806],
        "Ti": ["Titânio", 47.867],
        "Tl": ["Tálio", 204.3833],
        "Tm": ["Túlio", 168.93421],
        "U": ["Urânio", 238.02891],
        "V": ["Vanádio", 50.9415],
        "W": ["Tungstênio", 183.84],
        "Xe": ["Xenônio", 131.293],
        "Y": ["Ítrio", 88.90585],
        "Yb": ["Itérbio", 173.054],
        "Zn": ["Zinco", 65.38],
        "Zr": ["Zircônio", 91.224]
    }
    return dic_da_tabela_periodica

#Adicionando a função calcular_massa_molar

def calcular_massa_molar(lista_quantidade_simbolos, tabela_periodica):

    INDICE_SIMBOLO = 0
    INDICE_QUANTIDADE = 1
    INDICE_MASSA_ATOMICA = 1

    massa_molar = 0

    for elemento in lista_quantidade_simbolos:
        simbolo = elemento[INDICE_SIMBOLO]
        quantidade = elemento[INDICE_QUANTIDADE]

        massa_atomica = tabela_periodica[simbolo][INDICE_MASSA_ATOMICA]

        massa_molar += quantidade * massa_atomica

    return massa_molar

#Adicionando a função main
def main():
    tabela_periodica = criar_tabela_periodica()

    formula = input("Insira a fórmula molecular da amostra: ")
    massa = float(input("Insira a massa em gramas da amostra: "))

    lista_quantidade_simbolos = interpretar_formula(
        formula,
        tabela_periodica
    )

    massa_molar = calcular_massa_molar(
        lista_quantidade_simbolos,
        tabela_periodica
    )

    mols = massa / massa_molar

    print(f"{massa_molar:.5f} gramas/mol")
    print(f"{mols:.5f} mols")

if __name__ == "__main__":
    main()