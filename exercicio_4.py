"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar
o nome em formato de escada.
"""

import sys
import time


class NomeNaVerticalEmEscada:
    def __init__(self, nome: str):
        self.nome = nome

    def imprime_nome_na_vertical_em_escada(self):
        for i in range(1, len(self.nome) + 1):
            index = self.nome[:i]
            sys.stdout.write(index.upper() + "\n")
            sys.stdout.flush()
            time.sleep(0.3)


if __name__ == "__main__":
    nome = input("Digite seu nome: \nUtilize letras maiúsculas e minúsculas\n")
    nome_na_vertical = NomeNaVerticalEmEscada(nome)
    print("Nome na vertical em escada: ")
    nome_na_vertical.imprime_nome_na_vertical_em_escada()
