"""
Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica
se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são
palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços
foram ignorados. Faça um programa que leia uma seqüência de caracteres,
mostre−a e diga se é um palíndromo ou não.
"""


class VerificaPalindromo:
    def __init__(self, frase_palindromo: str):
        self.frase_palindromo = frase_palindromo

    def eh_palindromo(self):
        remove_espacos = self.frase_palindromo.replace(" ", "").lower()

        return remove_espacos == remove_espacos[::-1]


if __name__ == "__main__":

    frase_qualquer = "subi no onibus"
    frase_verificada = VerificaPalindromo(frase_qualquer)
    if frase_verificada.eh_palindromo():
        print("É palindromo")
    else:
        print("Não é palíndromo")
