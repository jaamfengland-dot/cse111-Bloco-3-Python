
import math
import tkinter as tk
from tkinter import Frame, Label, Button
from entrada_numero import EntradaInteiro, EntradaFloat


def main():
    # Cria o objeto raiz (root) do Tk.
    raiz = tk.Tk()

    # Cria a janela/quadro principal dentro da raiz.
    janela_principal = Frame(raiz)
    janela_principal.master.title("Volume do Pneu")
    janela_principal.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Chama a função preencher_janela_principal, que adicionará
    # rótulos, caixas de entrada de texto e botões à janela principal.
    preencher_janela_principal(janela_principal)

    # Inicia o loop do tkinter que processa eventos do usuário.
    raiz.mainloop()


# --- CONVENÇÃO DE NOMENCLATURA DE COMPONENTES EM PORTUGUÊS ---
# janela_: quadro/janela (frame)
# rotulo_: rótulo de texto fixo (label) que o usuário apenas lê
# caixa_:  caixa de entrada numérica (entry) onde o usuário digitará dados
# botao_:  botão clicável (button)


def preencher_janela_principal(janela_principal):
    """Popula a janela principal deste programa. Em outras palavras, coloca
    os rótulos, caixas de entrada de texto e botões na janela principal.

    Parâmetro
        janela_principal: o quadro (frame) principal onde tudo será inserido.
    Retorno: nada
    """
    # Cria rótulos descritivos para as caixas de entrada e para o resultado.
    rotulo_largura = Label(janela_principal, text="Largura (80 - 300):")
    rotulo_proporcao = Label(janela_principal, text="Proporção (30 - 90):")
    rotulo_diametro = Label(janela_principal, text="Diâmetro (7 - 30):")
    rotulo_volume = Label(janela_principal, text="Volume:")

    # Cria as três caixas de entrada numéricas customizadas com limites em português.
    caixa_largura = EntradaInteiro(janela_principal, width=5, limite_inferior=80, limite_superior=300)
    caixa_proporcao = EntradaInteiro(janela_principal, width=5, limite_inferior=30, limite_superior=90)
    caixa_diametro = EntradaFloat(janela_principal, width=5, limite_inferior=7, limite_superior=30)

    # Cria um rótulo alinhado à direita para exibir a string numérica do resultado.
    rotulo_resultado_volume = Label(janela_principal, width=5, anchor="e")

    # Cria rótulos estáticos para exibir as unidades de medida.
    rotulo_unidades_largura = Label(janela_principal, text="milímetros")
    rotulo_unidades_diametro = Label(janela_principal, text="polegadas")
    rotulo_unidades_volume = Label(janela_principal, text="litros")

    # Cria o botão Limpar.
    botao_limpar = Button(janela_principal, text="Limpar")

    # --- ORGANIZAÇÃO EM GRADE (GRID) ---
    # Linha 0: Elementos da Largura
    rotulo_largura.grid(          row=0, column=0, padx=3, pady=2, sticky="e")
    caixa_largura.grid(           row=0, column=1, padx=3, pady=2, sticky="w")
    rotulo_unidades_largura.grid( row=0, column=2, padx=0, pady=2, sticky="w")

    # Linha 1: Elementos da Proporção (Proporções não possuem unidades de medida)
    rotulo_proporcao.grid(        row=1, column=0, padx=3, pady=2, sticky="e")
    caixa_proporcao.grid(         row=1, column=1, padx=3, pady=2, sticky="w")

    # Linha 2: Elementos do Diâmetro
    rotulo_diametro.grid(         row=2, column=0, padx=3, pady=2, sticky="e")
    caixa_diametro.grid(          row=2, column=1, padx=3, pady=2, sticky="w")
    rotulo_unidades_diametro.grid(row=2, column=2, padx=0, pady=2, sticky="w")

    # Linha 3: Elementos do Volume Final e o Botão Limpar
    rotulo_volume.grid(           row=3, column=0, padx=3, pady=2, sticky="e")
    rotulo_resultado_volume.grid( row=3, column=1, padx=3, pady=2, sticky="w")
    rotulo_unidades_volume.grid(  row=3, column=2, padx=0, pady=2, sticky="w")
    botao_limpar.grid(            row=3, column=3, padx=3, pady=2)


    # Esta função interna roda automaticamente sempre que o usuário solta uma tecla.
    def calcular(evento):
        """Calcula o volume aproximado de um pneu em litros."""
        try:
            # Obtém e valida as entradas do usuário.
            largura = caixa_largura.get()
            proporcao = caixa_proporcao.get()
            diametro = caixa_diametro.get()

            # Calcula o volume do pneu em litros usando a fórmula padrão.
            volume = (math.pi * largura * largura * proporcao * (largura * proporcao + 2540 * diametro)) / 10_000_000_000

            # Exibe o volume arredondado com duas casas decimais.
            rotulo_resultado_volume.config(text=f"{volume:.2f}")

        except ValueError:
            # Quando o usuário apaga caracteres deixando o campo vazio, limpa o resultado anterior.
            rotulo_resultado_volume.config(text="")


    # Esta função roda automaticamente quando o usuário clica no botão "Limpar".
    def limpar():
        """Limpa todas as caixas de entrada e os resultados da tela."""
        botao_limpar.focus()
        caixa_largura.clear()
        caixa_proporcao.clear()
        caixa_diametro.clear()
        rotulo_resultado_volume.config(text="")
        caixa_largura.focus()


    # Vincula o gatilho de cálculo em tempo real às três caixas de texto
    caixa_largura.bind("", calcular)
    caixa_proporcao.bind("", calcular)
    caixa_diametro.bind("", calcular)

    # Configura a ação do botão Limpar
    botao_limpar.config(command=limpar)

    # Dá o foco inicial do teclado para o campo de texto da largura.
    caixa_largura.focus()


if __name__ == "__main__":
    main()

