"""
Você trabalha para uma loja de varejo que deseja aumentar as vendas
às terças e quartas-feiras, que são os dias com menor movimento.
Nessas datas, se o subtotal da compra de um cliente for superior a R$50,
a loja aplicará um desconto de 10% na compra.
"""

# Importa o módulo datetime para que
# ele possa ser usado neste programa.
from datetime import datetime

# A taxa de desconto é 10% e a taxa de imposto sobre vendas é 6%.
TAXA_DESCONTO = 0.10
TAXA_IMPOSTO = 0.06

subtotal = 0

print("Digite o preço e a quantidade de cada item.")
preco = 1
while preco != 0:
    # Recebe o preço do usuário.
    preco = float(input("Digite o preço: "))
    if preco != 0:
        # Recebe a quantidade do usuário.
        quantidade = int(input("Digite a quantidade: "))

        subtotal += preco * quantidade

        # Exibe uma linha em branco.
        print()

# Arredonda o subtotal para duas casas decimais
# e exibe o subtotal.
subtotal = round(subtotal, 2)
print(f"Subtotal: R${subtotal:.2f}")
print()

# Obtém a data e hora atuais do sistema operacional.
data_hora_atual = datetime.now()

# Obtém o dia da semana (0 = segunda, 1 = terça, ..., 6 = domingo).
dia_semana = data_hora_atual.weekday()

# Se o subtotal for maior que 50 e hoje for terça (1) ou quarta (2),
# calcula o valor do desconto.
if dia_semana == 1 or dia_semana == 2:
    if subtotal < 50:
        faltando = 50 - subtotal
        print("Para receber o desconto, adicione"
              f" R${faltando:.2f} ao seu pedido.")
    else:
        desconto = round(subtotal * TAXA_DESCONTO, 2)
        print(f"Valor do desconto: R${desconto:.2f}")
        subtotal -= desconto

# Calcula o imposto sobre vendas (após o desconto).
imposto = round(subtotal * TAXA_IMPOSTO, 2)
print(f"Valor do imposto sobre vendas: R${imposto:.2f}")

# Calcula o total somando o subtotal com o imposto.
total = subtotal + imposto

# Exibe o total para o cliente.
print(f"Total: R${total:.2f}")
