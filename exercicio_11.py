"""
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de
palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador poderá errar 6 vezes antes de ser enforcado.
"""

from random import choice


class JogoDaForca:
    def __init__(self, chute: str):
        self.chute = chute

    def jogar():

        palavras = ["uva", "melancia", "sapato", "camisa"]
        palavra_secreta = choice(palavras).lower()
        letras_acertadas = ["_" for letra in palavra_secreta]
        erros = 0
        tentativas_max = 3

        print("Bem-vindo ao jogo da Forca!")
        print("A palavra secreta tem", len(palavra_secreta), "letras.")
        print(" ".join(letras_acertadas))

        while True:
            chute = input("Digite uma letra: ").strip().lower()

            if len(chute) != 1:
                print("Por favor, insira apenas uma letra.")
                continue

            if chute in palavra_secreta:
                for index, letra in enumerate(palavra_secreta):
                    if chute == letra:
                        letras_acertadas[index] = chute

                print("A palavra é: ", " ".join(letras_acertadas))
            else:
                erros += 1
                sufixo = "ª vez" if erros == 1 else "ª vez"
                print(f"-> Você errou pela {erros}{sufixo}. Tente de novo!\n")

            if "_" not in letras_acertadas:
                print("Parabéns, você venceu!!!")
                break

            if erros == tentativas_max:
                print(f"Você perdeu! A palavra era '{palavra_secreta}'.")
                break

        print("Fim do jogo")


if __name__ == "__main__":
    JogoDaForca.jogar()
