"""
Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando
outros símbolos em lugar das letras, como números por exemplo.
A própria palavra leet admite muitas variações, como l33t ou 1337.
O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de
computador e internet, sendo muito usada para confundir os iniciantes e
afirmar-se como parte de um grupo. Pesquise sobre as principais formas de
traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o
para a grafia leet speak.
"""


class ConverteParaLeetSpeak:
    def __init__(self):
        self.mapeamento = {
            "A": "4",
            "B": "8",
            "E": "3",
            "G": "9",
            "I": "1",
            "O": "0",
            "S": "5",
            "T": "7",
            "Z": "2",
        }

    def transformar_para_leet_speak(self, texto):
        leet_texto = ""
        for char in texto:
            if char.upper() in self.mapeamento:
                leet_texto += self.mapeamento[char.upper()]
            else:
                leet_texto += char
        return leet_texto


if __name__ == "__main__":
    texto_usuario = input("Digite uma frase qualquer: ")
    texto_traduzido = ConverteParaLeetSpeak()
    texto_leet_speak = texto_traduzido.transformar_para_leet_speak(texto_usuario)
    print(texto_leet_speak)
