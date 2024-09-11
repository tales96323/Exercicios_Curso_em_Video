"""Ve se um nome de cidade comeca com Santo"""
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"
def main():
    city = input("Digite uma cidade: \n").lower().strip().split()
    print(city[0] == "santo")
if __name__ == "__main__":
    main()