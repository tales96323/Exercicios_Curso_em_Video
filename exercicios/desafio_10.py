"""Converte Real em Dolar"""
def main():
# Considere R$ 3.27 = US$ 1
    n = float(input("Quanto dinheiro você tem? \nR$"))
    dolar = 3.27
    conversao = n / dolar
    print("Com R${} você pode comprar US$ {:.2f}.".format(n, conversao))
if __name__ == "__main__":
    main()