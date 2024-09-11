"""Mostra numeros pares de 1 a 50"""
# Crie um programa que mostre na tela todos os números pares
# que estão no intervalo entre 1 e 50
def main():
    for num in range(1, 51):
        if num % 2 == 0:
            print(num)
if __name__ == "__main__":
    main()