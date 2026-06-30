import random

def main():
    numeros = [16.2, 75.1, 52.3]
    print(f"números {numeros}")

    anexar_numeros_aleatorios(numeros)
    print(f"números {numeros}")

    anexar_numeros_aleatorios(numeros, 3)
    print(f"números {numeros}")

    lista_palavras = []

    anexar_palavras_aleatorias(lista_palavras)
    print(f"palavras {lista_palavras}") 

    anexar_palavras_aleatorias(lista_palavras, 5)
    print(f"palavras {lista_palavras}") 


def anexar_numeros_aleatorios(lista_numeros, quantidade=1):
    for _ in range(quantidade):
        numero_aleatorio = random.uniform(0, 100)
        arredondado = round(numero_aleatorio, 1)
        lista_numeros.append(arredondado)


def anexar_palavras_aleatorias(lista_palavras, quantidade=1):

    candidatas = [
        "braço", "carro", "nuvem", "cabeça", "cura", "hidrogênio", "correr",
        "unir", "rir", "amor", "dormir", "sorrir", "falar",
        "sol", "escova de dentes", "árvore", "verdade", "andar", "água"
    ]

    for _ in range(quantidade):
        palavra = random.choice(candidatas)
        lista_palavras.append(palavra)


if __name__ == "__main__":
    main()