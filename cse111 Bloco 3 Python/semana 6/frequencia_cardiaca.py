# Copyright 2020, Brigham Young University-Idaho. Todos os direitos reservados.

import tkinter as tk
from tkinter import Frame, Label, Button
from entrada_numero import EntradaInteiro


def main():
    # Cria o objeto raiz (root) do Tk.
    raiz = tk.Tk()

    # Cria a janela/quadro principal dentro da raiz.
    janela_principal = Frame(raiz)
    janela_principal.master.title("Frequência Cardíaca")
    janela_principal.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Chama a função preencher_janela_principal, que adicionará
    # rótulos, caixas de entrada de texto e botões à janela principal.
    preencher_janela_principal(janela_principal)

    # Inicia o loop do tkinter que processa os eventos do usuário.
    raiz.mainloop()


# --- CONVENÇÃO DE NOMENCLATURA DE COMPONENTES EM PORTUGUÊS ---
# janela_: quadro/janela (frame)
# rotulo_: rótulo (label) de texto fixo (label) que o usuário apenas lê
# caixa_:  caixa de entrada numérica (entry) onde o usuário digitará dados
# botao_:  botão clicável (button)


def preencher_janela_principal(janela_principal):
    """Preenche a janela principal deste programa. Em outras palavras, coloca
    os rótulos, caixas de entrada de texto e botões na janela principal.

    Parâmetro
        janela_principal: o quadro (frame) principal onde tudo será inserido.
    """
    # Cria os rótulos de texto fixo orientativos
    rotulo_idade = Label(janela_principal, text="Idade (12 - 90):")
    rotulo_unidade_idade = Label(janela_principal, text="anos")
    rotulo_frequencias = Label(janela_principal, text="Frequências:")
    rotulo_unidade = Label(janela_principal, text="batimentos/minuto")

    # Cria os rótulos que servirão de caixas vazias para exibir os resultados obtidos
    rotulo_lenta = Label(janela_principal, width=3)
    rotulo_rapida = Label(janela_principal, width=3)

    # Cria a caixa de entrada customizada que só aceita números inteiros.
    caixa_idade = EntradaInteiro(janela_principal, width=4, limite_inferior=12, limite_superior=90)

    # Cria o botão de limpar a tela.
    botao_limpar = Button(janela_principal, text="Limpar")

    # --- ORGANIZAÇÃO EM GRADE (GRID) ---
    # Linha 0: Elementos para coletar a idade
    rotulo_idade.grid(         row=0, column=0, padx=3, pady=3)
    caixa_idade.grid(          row=0, column=1, padx=3, pady=3)
    rotulo_unidade_idade.grid( row=0, column=2, padx=0, pady=3)

    # Linha 1: Elementos que exibem os resultados calculados
    rotulo_frequencias.grid(   row=1, column=0, padx=(30, 3), pady=3)
    rotulo_lenta.grid(         row=1, column=1, padx=3, pady=3)
    rotulo_rapida.grid(        row=1, column=2, padx=3, pady=3)
    rotulo_unidade.grid(       row=1, column=3, padx=0, pady=3)

    # Linha 2: Botão limpar
    botao_limpar.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")


    # Esta função interna roda automaticamente sempre que o usuário solta uma tecla na caixa de idade.
    def calcular(evento):
        """Calcula e exibe as frequências cardíacas benéficas
        mais lenta e mais rápida do usuário.
        """
        try:
            # Obtém a idade do usuário da nossa caixa customizada.
            idade = caixa_idade.get()

            # Calcula a frequência cardíaca máxima do usuário.
            frequencia_maxima = 220 - idade

            # Calcula as frequências cardíacas benéficas (alvo) do usuário.
            lenta = frequencia_maxima * 0.65
            rapida = frequencia_maxima * 0.85

            # Atualiza o texto dos rótulos de resultado com os novos valores arredondados.
            rotulo_lenta.config(text=f"{lenta:.0f}")
            rotulo_rapida.config(text=f"{rapida:.0f}")

        except ValueError:
            # Quando a caixa de entrada fica vazia, limpa os rótulos de resultado.
            rotulo_lenta.config(text="")
            rotulo_rapida.config(text="")


    # Esta função roda automaticamente quando o usuário clica no botão "Limpar".
    def limpar():
        """Limpa todas as caixas de entrada e os resultados da tela."""
        botao_limpar.focus()
        caixa_idade.clear()
        rotulo_lenta.config(text="")
        rotulo_rapida.config(text="")
        caixa_idade.focus()


    # Vincula a função de cálculo em tempo real à nossa caixa de idade
    caixa_idade.bind("<KeyRelease>", calcular)

    # Configura a ação do botão Limpar
    botao_limpar.config(command=limpar)

    # Força o cursor do teclado a iniciar piscando direto no campo de idade
    caixa_idade.focus()


if __name__ == "__main__":
    main()