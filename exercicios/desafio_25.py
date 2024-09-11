"""Verifica se um nome tem Silva"""
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
def main():
    nome = str(input("Digite seu nome: \n"))
    nome = nome.lower().strip().split()
    print("silva" in nome)
if __name__ == "__main__":
    main()