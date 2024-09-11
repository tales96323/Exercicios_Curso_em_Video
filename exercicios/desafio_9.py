"""Faz tabuada de um numero"""
def main():
    n = int(input("Digite um número: \n"))
    print("Tabuada do {}:".format(n))

    print("{} x {} = {}".format(n, 1, (n * 1)))

    # Sem loop o código é repetitivo
if __name__ == "__main__":
    main()