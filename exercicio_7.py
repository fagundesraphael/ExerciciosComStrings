"""
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário
(incluindo espaços em branco), conte:
    a - quantos espaços em branco existem na frase.
    b - quantas vezes aparecem as vogais a, e, i, o, u.
"""


class ContadorDeEspacosEVogais:
    def __init__(self, frase_usuario: str):
        self.frase_usuario = frase_usuario

    def conta_espacos(self):
        espacos_contados = self.frase_usuario.count(" ")
        print(f"Existem {espacos_contados} espaços em branco.")

    def conta_vogais(self):
        vogais = "aeiou"
        for vogal in vogais:
            contagem = self.frase_usuario.lower().count(vogal)
            print(f"Vogal '{vogal}' aparece {contagem} vezes.")

    def conta_espacos_e_vogais(self):
        self.conta_espacos()
        self.conta_vogais()


if __name__ == "__main__":
    frase_usuario = input(" Digite uma frase: ")
    frase_contada = ContadorDeEspacosEVogais(frase_usuario)
    frase_contada.conta_espacos_e_vogais()
