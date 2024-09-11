"""Cria o seu dobro, o seu triplo e sua raiz quadrada:"""
def main():
    n = int(input("Digite um número: \n"))
    print("O dobro de {} é: {}!".format(n, n * 2))
    print("O triplo de {} é: {}.".format(n, n * 3))
    print("A raiz quadrada de {} é: {}.".format(n, n**(1/2)))
if __name__ == "__main__":
    main()