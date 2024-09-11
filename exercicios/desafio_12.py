"""Ler preço e mostre seu novo preço, com x% de desconto (modificado - tinha desconto fixo de 5%)"""
def main():
    n = float(input("Digite o preço de um produto: \nR$"))
    d = float(input("Digite o valor do desconto:(entre  0 e 100) \n%"))
    desconto = n * d / 100
    print("Na liquidação da loja, esse produto de R${:.2f} está com desconto de {:.2f}%, \nou seja, vai custar só R${:.2f}.".format(n,d, n - desconto))
if __name__ == "__main__":
    main()