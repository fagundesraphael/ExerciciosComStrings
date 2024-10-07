"""
Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário
digitar o seu nome e em seguida mostre o nome do usuário de trás para frente
utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome
o usuário pode digitar letras maiúsculas ou minúsculas.
"""


class NomeAoContrarioMaiusculo:
    def __init__(self, nome: str):
        self.nome = nome

    def reverse_string(self):
        # nome = str(self.input)
        return "".join(reversed(self.nome)).upper()


if __name__ == "__main__":
    nome = input("Digite seu nome: \nUtilize letras maiúsculas e minúsculas\n")
    nome_invertido = NomeAoContrarioMaiusculo(nome)
    print(f"Nome ao contrário: {nome_invertido.reverse_string()}")
