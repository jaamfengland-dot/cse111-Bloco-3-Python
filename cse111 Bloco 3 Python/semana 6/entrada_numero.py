# Copyright 2020, Brigham Young University-Idaho. Todos os direitos reservados.

"""
Módulo de Componentes de Interface Gráfica para Entrada Numérica.

Este módulo contém duas classes, EntradaInteiro e EntradaFloat, que permitem
a um usuário inserir um número inteiro ou um número de ponto flutuante em um
widget Entry do tkinter.
"""

import tkinter as tk
from tkinter import Entry
from numbers import Number
from sys import float_info


class _EntradaNumerica(Entry):
    _ESTILO_ERRO = {"bg": "pink", "fg": "black"}

    def __init__(self, pai, tipo_dado, nome_tipo,
                 limite_inferior, limite_superior, padrao, argumentos_tk):
        super().__init__(pai)

        # Garante que a classe base não seja instanciada diretamente (Salvaguarda)
        assert type(self) != _EntradaNumerica, \
            "não é possível criar um objeto _EntradaNumerica diretamente; " \
            "apenas classes filhas de _EntradaNumerica podem ser instanciadas"
        assert isinstance(limite_inferior, tipo_dado), f"limite_inferior deve ser {nome_tipo}"
        assert isinstance(limite_superior, tipo_dado), f"limite_superior deve ser {nome_tipo}"
        assert limite_inferior < limite_superior, "limite_inferior deve ser menor que limite_superior"

        self.__tipo_dado = tipo_dado
        self.__nome_tipo = nome_tipo
        self.__limite_inferior = limite_inferior
        self.__limite_superior = limite_superior

        if padrao is not None:
            assert isinstance(padrao, tipo_dado), f"padrão deve ser {nome_tipo}"
            assert self._dentro_dos_limites(padrao), f"padrão deve estar entre {limite_inferior} e {limite_superior}"
            self.delete(0, tk.END)
            self.insert(0, str(padrao))

        self.__configurar_argumentos_tk(argumentos_tk)
        self.bind("<FocusIn>", _EntradaNumerica.__selecionar_tudo)

    def __configurar_argumentos_tk(self, argumentos_tk):
        """Define e injeta as propriedades de validação nativas do Tkinter."""
        if "justify" not in argumentos_tk:
            argumentos_tk["justify"] = "right"
        if "width" not in argumentos_tk:
            argumentos_tk["width"] = max(
                len(str(self.__limite_inferior)), 
                len(str(self.__limite_superior))
            )
        argumentos_tk["validate"] = "focusin"
        argumentos_tk["validatecommand"] = (
            self.register(self.__validar_tudo), "%V", "%s", "%P"
        )
        self.config(**argumentos_tk)
        self._estilo_original = {"bg": self["bg"], "fg": self["fg"]}

    # Sempre que o campo recebe o foco do teclado, seleciona todo o texto.
    @staticmethod
    def __selecionar_tudo(evento):
        """Seleciona todos os caracteres na caixa de entrada."""
        entrada = evento.widget
        entrada.select_range(0, tk.END)
        entrada.icursor(tk.END)

    @staticmethod
    def _contem_espaco(texto):
        """Detecta a presença de espaços em branco invalidantes."""
        for caractere in texto:
            if caractere.isspace():
                return True
        return False

    def __validar_tudo(self, motivo, texto_atual, texto_se_permitido):
        """Callback intermediário principal do sistema de validação do Tkinter."""
        valido = False
        if motivo == "key":
            valido = self._validar_tecla(texto_atual, texto_se_permitido)
        elif motivo == "focusin":
            valido = self.__foco_entrou(texto_atual)
        elif motivo == "focusout":
            valido = self.__foco_saiu(texto_atual)
        return valido

    def __foco_entrou(self, texto_atual):
        # Altera dinamicamente para 'all' para monitorar teclas enquanto focado
        self.config({"validate": "all"})
        return self.__validar_foco(texto_atual)

    def __foco_saiu(self, texto_atual):
        # Retorna para 'focusin' ao perder o foco do teclado
        self.config({"validate": "focusin"})
        return self.__validar_foco(texto_atual)

    def __validar_foco(self, texto_atual):
        """Aplica o estilo visual de erro caso o número final esteja fora dos limites."""
        valido = False
        try:
            n = self._converter(texto_atual)
            valido = self._dentro_dos_limites(n)
        except ValueError:
            pass
        estilo = self._estilo_original if valido else _EntradaNumerica._ESTILO_ERRO
        self.config(estilo)
        return valido

    def _dentro_dos_limites(self, n):
        return self.__limite_inferior <= n <= self.__limite_superior

    def set(self, n):
        """Exibe um número para o usuário ver via código."""
        assert isinstance(n, self.__tipo_dado), f"n deve ser {self.__nome_tipo}"
        assert self._dentro_dos_limites(n), f"n deve estar entre {self.__limite_inferior} e {self.__limite_superior}"
        self.delete(0, tk.END)
        self.insert(0, str(n))

    def get(self):
        """Retorna o número que o usuário digitou convertido para o tipo correto."""
        n = self._converter(super().get())
        if not self._dentro_dos_limites(n):
            raise ValueError(f"o número deve estar entre {self.__limite_inferior} e {self.__limite_superior}")
        return n

    def clear(self):
        """Limpa o campo de texto e restaura a paleta de cores original."""
        self.config({"validate": "focusin"})
        self.config(self._estilo_original)
        self.delete(0, tk.END)


class EntradaInteiro(_EntradaNumerica):
    """Um widget Entry que aceita apenas inteiros entre
    um limite inferior opcional e um limite superior opcional.
    """
    def __init__(self, pai, *, limite_inferior=-2**63,
                 limite_superior=2**63 - 1, padrao=None, **argumentos_tk):
        super().__init__(pai, int, "um inteiro",
                         limite_inferior, limite_superior, padrao, argumentos_tk)

        self.__limite_tecla_inferior = limite_inferior if limite_inferior <= 1 else 1
        self.__limite_tecla_superior = limite_superior if limite_superior >= -1 else -1
        self.__permite_negativo = (limite_inferior < 0)

    def _validar_tecla(self, texto_atual, texto_se_permitido):
        permitido = valido = False
        try:
            if not _EntradaNumerica._contem_espaco(texto_se_permitido):
                n = int(texto_se_permitido)
                permitido = self.__limite_tecla_inferior <= n <= self.__limite_tecla_superior
                # Se texto_se_permitido for permitido, validamos apenas ele.
                if permitido:
                    valido = self._dentro_dos_limites(n)
        except ValueError:
            permitido = (len(texto_se_permitido) == 0 or
                         (self.__permite_negativo and texto_se_permitido == "-"))

        # Se texto_se_permitido não for permitido, validamos apenas o texto_atual antigo.
        if not permitido:
            try:
                n = int(texto_atual)
                valido = self._dentro_dos_limites(n)
            except ValueError:
                pass

        estilo = self._estilo_original if valido else _EntradaNumerica._ESTILO_ERRO
        self.config(estilo)
        return permitido

    @staticmethod
    def _converter(texto): 
        return int(texto)


class EntradaFloat(_EntradaNumerica):
    """Um widget Entry que aceita apenas números decimais entre
    um limite inferior opcional e um limite superior opcional.
    """
    def __init__(self, pai, *, limite_inferior=-float_info.max,
                 limite_superior=float_info.max, padrao=None, **argumentos_tk):
        super().__init__(pai, Number, "um número",
                         limite_inferior, limite_superior, padrao, argumentos_tk)

        # Lógica matemática original elástica de digitação parcial da BYU
        if limite_inferior < 0:      # [-, 0)
            self.__limite_tecla_inferior = limite_inferior
        elif limite_inferior < 1:    # [0, 1)
            self.__limite_tecla_inferior = 0
        else:                        # [1, +]
            self.__limite_tecla_inferior = 1

        if limite_superior <= -1:    # [-, -1]
            self.__limite_tecla_superior = -1
        elif limite_superior <= 0:    # (-1, 0]
            self.__limite_tecla_superior = 0
        else:                        # (0, +]
            self.__limite_tecla_superior = limite_superior

        self.__permite_negativo = (limite_inferior < 0)
        self.__permite_ponto_inicial = (
                (-1 < limite_inferior < 1) or
                (-1 < limite_superior < 1) or
                (limite_inferior <= -1 and 1 <= limite_superior))

    def _validar_tecla(self, texto_atual, texto_se_permitido):
        permitido = valido = False
        try:
            if not _EntradaNumerica._contem_espaco(texto_se_permitido):
                n = float(texto_se_permitido)
                permitido = self.__limite_tecla_inferior <= n <= self.__limite_tecla_superior
                if permitido:
                    valido = self._dentro_dos_limites(n)
        except ValueError:
            permitido = (len(texto_se_permitido) == 0 or
                         (self.__permite_negativo and texto_se_permitido == "-") or
                         (self.__permite_ponto_inicial and texto_se_permitido == ".") or
                         (self.__permite_negativo and self.__permite_ponto_inicial
                          and texto_se_permitido == "-."))

        if not permitido:
            try:
                n = float(texto_atual)
                valido = self._dentro_dos_limites(n)
            except ValueError:
                pass

        estilo = self._estilo_original if valido else _EntradaNumerica._ESTILO_ERRO
        self.config(estilo)
        return permitido

    @staticmethod
    def _converter(texto): 
        return float(texto)