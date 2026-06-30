"""
Autor: João Augusto Ferreira

S01 - Projeto: Volume do Pneu

"""

# Pegando data atual do usuário e calculando pi usando math

import math
from datetime import date

# Pegando as informações do usuário

largura = float(input("Digite a largura do pneu em mm (por exemplo: 205): "))
proporcao = float(input("Digite a proporção do pneu (por exemplo: 60): "))
diametro = float(input("Digite o diâmetro da roda em polegadas (por exemplo: 15): "))

# Calculando a partir das informações do usuário

volume = (math.pi * largura**2 * proporcao * (largura * proporcao + 2540 * diametro)) / 10**10

# Exibindo o volume calculado

print(f"O volume aproximado é de {volume:.2f} litros")

# Pegando a data atual do sistema operacional usando strftime , e colocando os cinco dados no final do arquivo volumes.txt

data_atual = date.today().strftime("%d/%m/%Y")

with open("volumes.txt", "at", encoding="utf-8") as arquivo:
    print(f"{data_atual}, {largura}, {proporcao}, {diametro}, {volume:.2f}", file=arquivo)