"""Mostra inteiro Sucessor e Antecessor"""
def main():
    n = int(input("Digite um número: \n"))
    print("O antecessor do número {} é: {}.".format(n, n - 1))
    print("O sucessor do número {} é: {}.".format(n, n + 1))
if __name__ == "__main__":
    main()