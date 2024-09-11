"""# Conversor de temperaturas:ºC to ºF"""
def main():
    celsius = float(input("Digite a temperatura em Celsius: \n"))
    farenheit = ((1.8 * celsius) + 32)
    print("{}ºC correspondem a {:.1f}ºF.".format(celsius, farenheit))
if __name__ == "__main__":
    main()