"""Le numero e retorna se é primo"""
''' Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo'''

def main():
    num = int(input("Descubra se um número é primo: \n"))

    isPrime = True
    current = (num // 2)

    for i in range(current, 0, -1):
        if num % i == 0 and i != 1:
            isPrime = False

    if isPrime:
        print("O número {} é primo.".format(num))
    else:
        print("O número {} não é primo.".format(num))
if __name__ == "__main__":
    main()