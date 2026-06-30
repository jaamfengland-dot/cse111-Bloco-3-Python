class FormulaError(ValueError):
    """FormulaError é o tipo de erro que a função interpretar_formula
    irá lançar se uma fórmula for inválida.
    """


def interpretar_formula(formula, dic_da_tabela_periodica):
    """
    Converte uma fórmula química em uma lista de elementos com suas quantidades.
    """

    assert isinstance(formula, str), \
        "tipo de dado incorreto para o parâmetro formula"

    assert isinstance(dic_da_tabela_periodica, dict), \
        "tipo de dado incorreto para o parâmetro dic_da_tabela_periodica"

    def parse_quantidade(formula, indice):
        quantidade = 1

        if indice < len(formula) and formula[indice].isdecimal():

            if formula[indice] == "0":
                raise FormulaError(
                    "fórmula inválida, quantidade começa com 0",
                    formula,
                    indice
                )

            inicio = indice
            indice += 1

            while indice < len(formula) and formula[indice].isdecimal():
                indice += 1

            quantidade = int(formula[inicio:indice])

        return quantidade, indice

    def obter_quantidade(dicionario, simbolo):
        return 0 if simbolo not in dicionario else dicionario[simbolo]

    def interpretar_recursivo(formula, indice, nivel):
        inicio_indice = indice
        nivel_inicial = nivel
        elementos = {}

        while indice < len(formula):
            caractere = formula[indice]

            if caractere == "(":
                grupo, indice = interpretar_recursivo(formula, indice + 1, nivel + 1)
                quantidade, indice = parse_quantidade(formula, indice)

                for simbolo in grupo:
                    anterior = obter_quantidade(elementos, simbolo)
                    atual = anterior + grupo[simbolo] * quantidade
                    elementos[simbolo] = atual

            elif caractere.isalpha():
                simbolo = formula[indice:indice+2]

                if simbolo in dic_da_tabela_periodica:
                    indice += 2
                else:
                    simbolo = formula[indice:indice+1]
                    if simbolo in dic_da_tabela_periodica:
                        indice += 1
                    else:
                        raise FormulaError(
                            "fórmula inválida; símbolo desconhecido: " + simbolo,
                            formula,
                            indice
                        )

                quantidade, indice = parse_quantidade(formula, indice)
                anterior = obter_quantidade(elementos, simbolo)
                elementos[simbolo] = anterior + quantidade

            elif caractere == ")":
                if nivel == 0:
                    raise FormulaError(
                        "fórmula inválida; parêntese fechado sem abertura",
                        formula,
                        indice
                    )

                nivel -= 1
                indice += 1
                break

            else:
                if caractere.isdecimal():
                    mensagem = "fórmula inválida"
                else:
                    mensagem = "fórmula inválida; caractere ilegal: " + caractere

                raise FormulaError(mensagem, formula, indice)

        if nivel > 0 and nivel >= nivel_inicial:
            raise FormulaError(
                "fórmula inválida; parêntese aberto sem fechamento",
                formula,
                inicio_indice - 1
            )

        return elementos, indice

    elementos, _ = interpretar_recursivo(formula, 0, 0)
    return list(elementos.items())