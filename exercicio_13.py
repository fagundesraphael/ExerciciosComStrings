"""
Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que
adivinhar uma palavra que será mostrada com as letras embaralhadas.
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá
uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra.
Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou
ou perdeu o jogo.
"""

import random


class JogoPalavraEmbaralhada:
    def __init__(self, arquivo_palavras, tentativas_max=6):
        self.arquivo_palavras = arquivo_palavras
        self.tentativas_max = tentativas_max
        self.palavra_secreta = ""
        self.palavra_embaralhada = ""

    def ler_palavra_aleatoria(self):
        with open(self.arquivo_palavras, "r") as file:
            palavras = file.readlines()
            palavras = [palavra.strip() for palavra in palavras]
        self.palavra_secreta = random.choice(palavras)
        return self.palavra_secreta

    def embaralhar_palavra(self):
        lista_palavra = list(self.palavra_secreta)
        random.shuffle(lista_palavra)
        self.palavra_embaralhada = "".join(lista_palavra)
        return self.palavra_embaralhada

    def jogar(self):
        self.ler_palavra_aleatoria()
        self.embaralhar_palavra()

        tentativas_restantes = self.tentativas_max
        venceu = False

        print(f"Você tem {tentativas_restantes} tentativas para adivinhar a palavra.")
        print(f"A palavra embaralhada é: {self.palavra_embaralhada}")

        while tentativas_restantes > 0:
            chute = input("Qual é a palavra correta? ").strip().lower()

            if chute == self.palavra_secreta:
                print("Parabéns! Você acertou!")
                venceu = True
                break
            else:
                tentativas_restantes -= 1
                print(f"Você errou! Restam {tentativas_restantes} tentativas.")

        if not venceu:
            print(f"Você perdeu! A palavra correta era: {self.palavra_secreta}")

        print("Fim do jogo!")


if __name__ == "__main__":
    jogo = JogoPalavraEmbaralhada("palavras.txt")
    jogo.jogar()
