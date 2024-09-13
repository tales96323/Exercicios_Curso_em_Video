"""Cria uma matriz preenchendo valores"""
'''
Crie um programa que crie uma matriz 3.3
e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela com a formatação correta
'''

def main():
    # Declarando variáveis
    lista = list()
    listb = list()


    for i in range(0, 3):  # Para cada linha
        for j in range(0, 3):  # Para cada coluna em cada linha
            listb.append(int(input(f"Digite um valor para [{i}, {j}]: \n")))

        lista.append(listb[:])  # Copie a linha para listb
        listb.clear()

    for l in lista:
        print(l)

if __name__ == "__main__":
    main()