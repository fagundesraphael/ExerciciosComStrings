""""
Data por extenso. Faça um programa que solicite a data de nascimento do usuário
e imprima a data com o nome do mês por extenso.
"""

import locale
from datetime import datetime


class DataPorExtenso:
    def __init__(self, data_nascimento: str):
        self.data_nascimento = data_nascimento

    def imprime_data_por_extenso(self):

        try:
            locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

            aniversario = datetime.strptime(self.data_nascimento, "%d/%m/%Y")

            data_por_extenso = aniversario.strftime("%d de %B de %Y")
            print(f"Você nasceu em: {data_por_extenso}")
        except Exception:
            print("Fomato de data inválido.")


if __name__ == "__main__":
    aniversario = input("Digite seu aniversário (formato DD/MM/AAAA): ")
    data_nascimento = DataPorExtenso(aniversario)
    data_nascimento.imprime_data_por_extenso()
