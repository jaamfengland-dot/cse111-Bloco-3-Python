import csv
from datetime import datetime


def ler_dicionario(nome_arquivo, indice_coluna_chave):
    dicionario = {}

    with open(nome_arquivo, "rt", encoding="utf-8") as arquivo_csv:
        leitor = csv.reader(arquivo_csv)

        next(leitor)

        for linha in leitor:
            chave = linha[indice_coluna_chave]
            dicionario[chave] = linha

    return dicionario


def main():
    try:
        dic_produtos = ler_dicionario("produtos.csv", 0)

        print("Empório Inkom")

        total_itens = 0
        subtotal = 0

        with open("pedido.csv", "rt", encoding="utf-8") as arquivo_csv:
            leitor = csv.reader(arquivo_csv)

            next(leitor)

            for linha in leitor:
                numero_produto = linha[0]
                quantidade = int(linha[1])

                produto = dic_produtos[numero_produto]

                nome_produto = produto[1]
                preco = float(produto[2])

                print(f"{nome_produto}: {quantidade} @ {preco:.2f}")

                total_itens += quantidade
                subtotal += quantidade * preco

        imposto = subtotal * 0.06
        total = subtotal + imposto

        print(f"Número de itens: {total_itens}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Imposto sobre vendas: {imposto:.2f}")
        print(f"Total: {total:.2f}")

        print("Obrigado por comprar no Empório Inkom.")

        data_hora = datetime.now()
        print(data_hora.strftime("%d/%m/%Y %H:%M:%S"))

    except FileNotFoundError as erro:
        print("Error: missing file")
        print(erro)

    except KeyError as erro:
        print("Error: unknown product ID in the request.csv file")
        print(erro)


if __name__ == "__main__":
    main()