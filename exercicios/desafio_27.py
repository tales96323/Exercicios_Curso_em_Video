"""Separa nome completo"""
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

# Ex.: Ana Maria de Souza
# Primeiro = Ana
# Último: Souza
def main():
    nome = "Tertuliano da Silva Moraes Menezes Bueno de Andrada"
    nome = nome.split()
    print(nome)
    print("Primeiro = {}".format(nome[0]))
    print("Último = {}".format(nome[-1]))
if __name__ == "__main__":
    main()