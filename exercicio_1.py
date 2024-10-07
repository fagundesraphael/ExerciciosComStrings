"""
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo
delas seguido do seu comprimento. Informe também se as duas strings possuem o
mesmo comprimento e são iguais ou diferentes no conteúdo.
"""


class ComparadorDeString:
    def __init__(self, input_1: str, input_2: str):
        self.input_1 = input_1
        self.input_2 = input_2

    def medidor_de_string(self, string):
        tamanho = len(string)
        print(f"Tamanho de '{string}': {tamanho} characteres")
        return tamanho

    def compara_duas_strings(self):
        tamanho_input_1 = self.medidor_de_string(self.input_1)
        tamanho_input_2 = self.medidor_de_string(self.input_2)

        if tamanho_input_1 == tamanho_input_2:
            print("As duas strings tem o mesmo tamanho.")
        else:
            print("As duas strings são de tamanhos diferentes.")

        if self.input_1 == self.input_2:
            print("As duas strings possuem o mesmo conteúdo.")
        else:
            print("As duas strings possuem conteúdo diferente.")


if __name__ == "__main__":
    input_1 = "Brasil Hexa 2006"
    input_2 = "Brasil! Hexa 2006!"

    comparador = ComparadorDeString(input_1, input_2)
    comparador.compara_duas_strings()
