"""Apresenta a porcao inteira de um numero."""
# Desafio 16: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc
def main():
    num = float(input("Digite um número real: \n"))
    # print(math.trunc(num))

    print("O valor digitado é {} e a sua porção inteira é {}.".format(num, int(num)))

    print("O valor digitado é {} e a sua porção inteira é {}.".format(num, trunc(num)))
if __name__ == "__main__":
    main()