from exercicio_1 import ComparadorDeString
from exercicio_2 import NomeAoContrarioMaiusculo
from exercicio_3 import NomeNaVertical
from exercicio_4 import NomeNaVerticalEmEscada
from exercicio_5 import NomeNaVerticalEmEscadaInvertida
from exercicio_6 import DataPorExtenso
from exercicio_7 import ContadorDeEspacosEVogais
from exercicio_8 import VerificaPalindromo
from exercicio_9 import VerificaCPF
from exercicio_10 import ConverteNumeroParaExtenso
from exercicio_11 import JogoDaForca
from exercicio_12 import CorrigeNumeroDeTelefone
from exercicio_13 import JogoPalavraEmbaralhada
from exercicio_14 import ConverteParaLeetSpeak


def main():
    """
    Resolução exercício 1
    """
    input_1 = "Brasil Hexa 2006"
    input_2 = "Brasil! Hexa 2006!"

    comparador = ComparadorDeString(input_1, input_2)
    comparador.compara_duas_strings()

    """
    Resolução exercício 2
    """
    nome = input("Digite seu nome: \nUtilize letras maiúsculas e minúsculas\n")
    nome_invertido = NomeAoContrarioMaiusculo(nome)
    print(f"Nome ao contrário: {nome_invertido.reverse_string()}")

    """
    Resolução exercício 3
    """
    nome_na_vertical = NomeNaVertical(nome)
    print("Nome na vertical: ")
    nome_na_vertical.imprime_nome_na_vertical()

    """
    Resolução exercício 4
    """
    nome_na_vertical = NomeNaVerticalEmEscada(nome)
    print("Nome na vertical em escada: ")
    nome_na_vertical.imprime_nome_na_vertical_em_escada()

    """
    Resolução exercício 5
    """
    nome_na_vertical_invertido = NomeNaVerticalEmEscadaInvertida(nome)
    print("Nome na vertical em escada invertida: ")
    nome_na_vertical_invertido.imprime_nome_na_vertical_em_escada_invertida()

    """
    Resolução exercício 6
    """
    aniversario = input("Digite seu aniversário (formato DD/MM/AAAA): ")
    data_nascimento = DataPorExtenso(aniversario)
    data_nascimento.imprime_data_por_extenso()

    """
    Resolução exercício 7
    """
    frase_usuario = input(" Digite uma frase: ")
    frase_contada = ContadorDeEspacosEVogais(frase_usuario)
    frase_contada.conta_espacos_e_vogais()

    """
    Resolução exercício 8
    """
    frase_palindromo = "subi no onibus"
    frase_verificada = VerificaPalindromo(frase_palindromo)
    if frase_verificada.eh_palindromo():
        print("É palindromo")
    else:
        print("Não é palíndromo")

    """
    Resolução exercício 9
    """
    cpf_usuario = input("Digite seu CPF: ")
    cpf_validado = VerificaCPF(cpf_usuario)
    if cpf_validado.validar_cpf():
        print("CPF válido")
    else:
        print("CPF inválido")

    """
    Resolução exercício 10
    """
    number = int(input("Digite um número: "))
    numero_por_extenso = ConverteNumeroParaExtenso(number)
    words = numero_por_extenso.converte_para_extenso()
    print(words)

    """
    Resolução exercício 11
    """
    JogoDaForca.jogar()

    """
    Resolução exercício 12
    """
    telefone_usuario = input(
        "Digite o número do telefone: (O número de telefone precisa ter 7 ou 8 dígitos)\n "
    )
    telefone_corrigido = CorrigeNumeroDeTelefone(telefone_usuario)
    telefone_corrigido.valida_e_corrige_telefone()

    """
    Resolução exercício 13
    """
    jogo = JogoPalavraEmbaralhada("palavras.txt")
    jogo.jogar()

    """
    Resolução exercício 14
    """
    texto_usuario = input("Digite uma frase qualquer: ")
    texto_traduzido = ConverteParaLeetSpeak()
    texto_leet_speak = texto_traduzido.transformar_para_leet_speak(texto_usuario)
    print(texto_leet_speak)


if __name__ == "__main__":
    main()
