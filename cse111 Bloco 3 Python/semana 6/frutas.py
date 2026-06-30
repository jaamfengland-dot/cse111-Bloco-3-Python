def main():
    try:
        # Cria e exibe uma lista chamada lista_de_frutas.
        lista_de_frutas = ["pêra", "banana", "maçã", "manga"]
        print(f"original: {lista_de_frutas}")

        # Inverte e exibe a lista lista_de_frutas.
        lista_de_frutas.reverse()
        print(f"invertida: {lista_de_frutas}")

        # Anexa "laranja" ao final da lista_de_frutas e exibe a lista.
        lista_de_frutas.append("laranja")
        print(f"anexação de laranja ao final: {lista_de_frutas}")

        # Encontra onde "maçã" está localizada na lista_de_frutas e insere
        # "cereja" antes de "maçã" na lista, depois exibe a lista.
        indice = lista_de_frutas.index("maçã")
        lista_de_frutas.insert(indice, "cereja")
        print(f"inserção de cereja: {lista_de_frutas}")

        # Remove "banana" da lista_de_frutas e exibe a lista.
        lista_de_frutas.remove("banana")
        print(f"remoção de banana: {lista_de_frutas}")

        # Remove o último elemento da lista_de_frutas (pop)
        # e exibe o elemento removido e a lista.
        ultimo = lista_de_frutas.pop()
        print(f"remoção de {ultimo}: {lista_de_frutas}")

        # Ordena e exibe a lista_de_frutas.
        lista_de_frutas.sort()
        print(f"ordenada: {lista_de_frutas}")

        # Limpa e exibe a lista_de_frutas.
        lista_de_frutas.clear()
        print(f"vazia: {lista_de_frutas}")

    except IndexError as erro_indice:
        print(type(erro_indice).__name__, erro_indice, sep=": ")


# Se este arquivo for executado diretamente assim:
# > python frutas.py
# então chama a função main. Porém, se for importado (ex: por um arquivo de testes),
# a função main não será chamada automaticamente.
if __name__ == "__main__":
    main()