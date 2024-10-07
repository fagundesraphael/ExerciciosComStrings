"""
Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o
na vertical
"""

import sys
import time


class NomeNaVertical:
    def __init__(self, nome: str):
        self.nome = nome

    def imprime_nome_na_vertical(self):
        nome = self.nome

        for char in nome:
            sys.stdout.write(char.upper() + " \n")
            sys.stdout.flush()
            time.sleep(0.3)


if __name__ == "__main__":
    nome = input("Digite seu nome: \nUtilize letras maiúsculas e minúsculas\n")
    nome_na_vertical = NomeNaVertical(nome)
    print("Nome na vertical: ")
    nome_na_vertical.imprime_nome_na_vertical()
