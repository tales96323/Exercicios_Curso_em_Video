"""Informacoes sobre o tipo de variavel"""
def main():
    entrada = input("Digite algo: \n")
    print("Tipo primitivo: {}.".format(type(entrada)))

    print("É numérico? {}".format(entrada.isnumeric()))
    print("É alfanumérico? {}.".format(entrada.isalpha()))
    print("É um decimal? {}.".format(entrada.isdecimal()))
    print("Está em caixa baixa? {}.".format(entrada.islower()))
    print("É apenas espaço em branco? {}.".format(entrada.isspace()))
    print("Está em caixa alta? {}.".format(entrada.isupper()))
if __name__ == "__main__":
    main()
