"""
Verificação de CPF. Desenvolva um programa que solicite a digitação de um
número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou
inválido através da validação dos dígitos verificadores edos caracteres de
formatação.
"""

import re


class VerificaCPF:
    def __init__(self, cpf: str):
        self.cpf = cpf

    def validar_cpf(self):
        self.cpf = "".join(re.findall(r"\d", str(self.cpf)))

        if not self.cpf or len(self.cpf) < 11:
            return False

        antigo = [int(d) for d in self.cpf]

        novo = antigo[:9]
        while len(novo) < 11:
            resto = sum([v * (len(novo) + 1 - i) for i, v in enumerate(novo)]) % 11

            digito_verificador = 0 if resto <= 1 else 11 - resto

            novo.append(digito_verificador)

        if novo == antigo:
            return self.cpf

        return False


if __name__ == "__main__":
    cpf_usuario = input("Digite seu CPF: ")
    cpf_validado = VerificaCPF(cpf_usuario)
    if cpf_validado.validar_cpf():
        print("CPF válido")
    else:
        print("CPF inválido")
