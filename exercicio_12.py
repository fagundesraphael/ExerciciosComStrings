"""
Valida e corrige número de telefone. Faça um programa que leia um número
de telefone, e corrija o número no caso deste conter somente 7 dígitos,
acrescentando o '3' na frente. O usuário pode informar o número com ou sem
o traço separador.
exemplo:
Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
"""


class CorrigeNumeroDeTelefone:
    def __init__(self, numero: str):
        self.numero = numero.replace("-", "")

    def valida_e_corrige_telefone(self):
        numero_telefone = self.numero

        if len(numero_telefone) < 7 or len(numero_telefone) > 8:
            print("Erro: O número de telefone precisa ter 7 ou 8 dígitos.")
            return "Número inválido"

        if len(numero_telefone) == 7:
            print("Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.")
            numero_telefone = "3" + numero_telefone

        telefone_corrigido_com_formatacao = (
            f"{numero_telefone[:4]}-{numero_telefone[4:]}"
        )

        print("Telefone corrigido sem formatação: ", numero_telefone)
        print("Telefone corrigido com formatação: ", telefone_corrigido_com_formatacao)


if __name__ == "__main__":
    telefone_usuario = input(
        "Digite o número do telefone: (O número de telefone precisa ter 7 ou 8 dígitos)\n "
    )
    telefone_corrigido = CorrigeNumeroDeTelefone(telefone_usuario)
    telefone_corrigido.valida_e_corrige_telefone()
