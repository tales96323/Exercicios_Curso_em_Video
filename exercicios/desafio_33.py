"""Mostra qual o menor e maior numero com if"""
'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor
'''
def main():
    a = int(input("Digite um primeiro número: \n"))
    b = int(input("Digite um segundo número: \n"))
    c = int(input("Digite um terceiro e último número: \n"))


    # Verificando os menores:
    menor = a

    if b < a and b < c:
        menor = b
    if c < a and c < b:
        menor = c

    # Verificando os maiores:
    maior = a

    if b > a and b > c:
        maior = b
    if c > a and c > b:
        maior = c

    # Printando os resultados onde a variável parou:

    print("O maior resultado foi: {}.".format(maior))
    print("O menor resultado foi: {}.".format(menor))
if __name__ == "__main__":
    main()
