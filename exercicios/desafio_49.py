"""Faz tabuada com laço em for"""
''' Refaça o desafio 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for'''
def main():
    num = int(input("Digite um número: \n"))
    for i in range(1, 11):
        print("{} x {} = {}".format(num, i, (num * i)))
if __name__ == "__main__":
    main()