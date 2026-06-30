# Importa a função sleep do módulo time,
# para que possamos usá-la neste programa.
from time import sleep

# Pede ao usuário para digitar seu nome.
nome = input("Olá! Qual é o seu nome? ")

# Imprime os números 3, 2, 1.
for i in range(3, 0, -1):
    print(i, flush=True)
    sleep(0.5)  # Pausa por 1/2 segundo

# Usa uma f-string do Python para formatar
# uma saudação ao usuário e depois a imprime.
print(f"Bem-vindo(a) ao CSE 111, {nome}!")
