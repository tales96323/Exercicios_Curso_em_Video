import os
import re
import importlib.util
from colorama import init, Fore, Style

# Inicializa o Colorama
init(autoreset=True)

def listar_exercicios(pasta):
    """Lista os arquivos de exercícios na pasta fornecida e os ordena numericamente."""
    arquivos = [f for f in os.listdir(pasta) if f.endswith('.py') and f != '__init__.py' and f != 'Menu.py']
    
    # Função auxiliar para extrair o número do exercício
    def extrair_numero(nome_arquivo):
        match = re.search(r'\d+', nome_arquivo)
        return int(match.group()) if match else 0
    
    # Ordena os arquivos pelo número do exercício
    arquivos_ordenados = sorted(arquivos, key=extrair_numero)
    return arquivos_ordenados

def mostrar_menu(exercicios):
    """Mostra o menu de exercícios disponíveis com formatação."""
    print(Fore.CYAN + Style.BRIGHT + "\n" + "="*40)
    print(Fore.YELLOW + Style.BRIGHT + "        MENU DE EXERCÍCIOS")
    print(Fore.CYAN + Style.BRIGHT + "="*40 + "\n")
    
    for i, exercicio in enumerate(exercicios, start=1):
        print(Fore.GREEN + Style.BRIGHT + f" {i}. {exercicio}")
    
    print(Fore.CYAN + Style.BRIGHT + "\n" + "="*40)
    print(Fore.MAGENTA + Style.BRIGHT + " Digite o número do exercício ou 0 para sair")
    print(Fore.CYAN + Style.BRIGHT + "="*40 + "\n")

def importar_modulo(caminho, nome_modulo):
    """Importa um módulo dado o caminho completo do arquivo e o nome do módulo."""
    spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo

def executar_exercicio(escolha, exercicios, pasta):
    """Importa e executa o módulo do exercício escolhido."""
    nome_arquivo = exercicios[escolha - 1]
    caminho_completo = os.path.join(pasta, nome_arquivo)
    nome_modulo = nome_arquivo.replace('.py', '')
    
    modulo = importar_modulo(caminho_completo, nome_modulo)
    
    # Pressupondo que cada exercício tem uma função main para executar
    if hasattr(modulo, 'main'):
        print(Fore.YELLOW + Style.BRIGHT + f"\nExecutando {nome_modulo}...\n")
        modulo.main()
    else:
        print(Fore.RED + Style.BRIGHT + f'\nO exercício {nome_modulo} não possui uma função main.\n')

if __name__ == "__main__":
    # Obtém o caminho da pasta atual e configura o caminho relativo para a pasta 'exercicios'
    pasta_exercicios = os.path.join(os.path.dirname(__file__), 'exercicios')
    exercicios = listar_exercicios(pasta_exercicios)
    
    mostrar_menu(exercicios)
    
    while True:
        try:
            escolha = int(input(Fore.CYAN + Style.BRIGHT + "Sua escolha: "))
            if escolha == 0:
                print(Fore.MAGENTA + Style.BRIGHT + "\nSaindo...\n")
                break
            elif 1 <= escolha <= len(exercicios):
                executar_exercicio(escolha, exercicios, pasta_exercicios)
            else:
                print(Fore.RED + Style.BRIGHT + "\nEscolha inválida, tente novamente.\n")
            
            # Perguntar ao usuário se ele deseja ver a lista novamente
            mostrar_novamente = input(Fore.CYAN + "\nDeseja ver a lista de exercícios novamente? (s/n): ").strip().lower()
            if mostrar_novamente == 's':
                mostrar_menu(exercicios)
                
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "\nPor favor, digite um número válido.\n")

        
