"""
Nome na vertical em escada invertida. Altere o programa anterior de modo que
a escada seja invertid
"""

import sys
import time


class NomeNaVerticalEmEscadaInvertida:
    def __init__(self, nome: str):
        self.nome = nome

    def imprime_nome_na_vertical_em_escada_invertida(self):
        for i in range(len(self.nome), 0, -1):
            index = self.nome[:i]
            sys.stdout.write(index.upper() + "\n")
            sys.stdout.flush()
            time.sleep(0.3)


if __name__ == "__main__":
    nome = input("Digite seu nome: \nUtilize letras maiúsculas e minúsculas\n")
    nome_na_vertical_invertido = NomeNaVerticalEmEscadaInvertida(nome)
    print("Nome na vertical em escada invertida: ")
    nome_na_vertical_invertido.imprime_nome_na_vertical_em_escada_invertida()
