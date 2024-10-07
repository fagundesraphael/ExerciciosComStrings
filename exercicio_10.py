"""
Número por extenso. Escreva um programa que solicite ao usuário a digitação de
um número até 99 e imprima-o na tela por extenso.
"""


class ConverteNumeroParaExtenso:
    def __init__(self, numero: int):
        self.numero = numero

    def converte_para_extenso(self):
        if self.numero == 0:
            return "zero"

        unidades = [
            "",
            "um",
            "dois",
            "três",
            "quatro",
            "cinco",
            "seis",
            "sete",
            "oito",
            "nove",
        ]
        dezenas = [
            "",
            "",
            "vinte",
            "trinta",
            "quarenta",
            "cinquenta",
            "sessenta",
            "setenta",
            "oitenta",
            "noventa",
        ]
        especiais = [
            "dez",
            "onze",
            "doze",
            "treze",
            "quatorze",
            "quinze",
            "dezesseis",
            "dezessete",
            "dezoito",
            "dezenove",
        ]
        centenas = [
            "",
            "cento",
            "duzentos",
            "trezentos",
            "quatrocentos",
            "quinhentos",
            "seiscentos",
            "setecentos",
            "oitocentos",
            "novecentos",
        ]

        extenso = ""

        if self.numero >= 1000:
            if self.numero // 1000 == 1:
                extenso += "mil "
            else:
                extenso += unidades[self.numero // 1000] + " mil "
            self.numero %= 1000

        if self.numero >= 100:
            if self.numero == 100:
                extenso += "cem "
                self.numero = 0
            else:
                extenso += centenas[self.numero // 100] + " "
                self.numero %= 100

        if 10 <= self.numero <= 19:
            extenso += especiais[self.numero - 10] + " "
            self.numero = 0
        elif self.numero >= 20:
            extenso += dezenas[self.numero // 10] + " "
            self.numero %= 10

        if self.numero >= 1:
            if extenso and extenso[-1] != " ":
                extenso += "e "
            extenso += unidades[self.numero] + " "

        return extenso.strip()


if __name__ == "__main__":
    number = int(input("Digite um número: "))
    numero_por_extenso = ConverteNumeroParaExtenso(number)
    words = numero_por_extenso.converte_para_extenso()
    print(words)
