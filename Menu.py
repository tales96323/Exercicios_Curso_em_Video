import os
import re
import importlib.util

def listar_exercicios_com_primeira_linha(pasta):
    """Lista os arquivos de exercícios na pasta fornecida, com a primeira linha de cada um, e os ordena numericamente."""
    arquivos = [f for f in os.listdir(pasta) if f.endswith('.py') and f != '__init__.py' and f != 'Menu.py']
    
    exercicios_com_primeira_linha = []

    for arquivo in arquivos:
        caminho_completo = os.path.join(pasta, arquivo)
        try:
            with open(caminho_completo, 'r', encoding='utf-8') as f:
                primeira_linha = f.readline().strip()  # Lê a primeira linha do arquivo
                exercicios_com_primeira_linha.append((arquivo, primeira_linha))
        except Exception as e:
            exercicios_com_primeira_linha.append((arquivo, "Erro ao ler o arquivo"))
    
    # Função auxiliar para extrair o número do exercício
    def extrair_numero(nome_arquivo):
        match = re.search(r'\d+', nome_arquivo)
        return int(match.group()) if match else 0
    
    # Ordena os arquivos pelo número do exercício
    exercicios_ordenados = sorted(exercicios_com_primeira_linha, key=lambda x: extrair_numero(x[0]))
    return exercicios_ordenados

def mostrar_menu(exercicios):
    """Mostra o menu de exercícios disponíveis com a primeira linha de cada arquivo."""
    print("\n" + "="*50)
    print("          MENU DE EXERCÍCIOS")
    print("="*50 + "\n")
    
    for i, (nome_arquivo, primeira_linha) in enumerate(exercicios, start=1):
        print(f" {i}. {nome_arquivo} - {primeira_linha}")
    
    print("\n" + "="*50)
    print(" Digite o número do exercício ou 0 para sair")
    print("="*50 + "\n")

def importar_modulo(caminho, nome_modulo):
    """Importa um módulo dado o caminho completo do arquivo e o nome do módulo."""
    spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo

def executar_exercicio(escolha, exercicios, pasta):
    """Importa e executa o módulo do exercício escolhido."""
    nome_arquivo = exercicios[escolha - 1][0]  # Pega o nome do arquivo
    caminho_completo = os.path.join(pasta, nome_arquivo)
    nome_modulo = nome_arquivo.replace('.py', '')
    
    modulo = importar_modulo(caminho_completo, nome_modulo)
    
    # Pressupondo que cada exercício tem uma função main para executar
    if hasattr(modulo, 'main'):
        print(f"\nExecutando {nome_modulo}...\n")
        modulo.main()
    else:
        print(f'\nO exercício {nome_modulo} não possui uma função main.\n')

if __name__ == "__main__":
    # Obtém o caminho da pasta atual e configura o caminho relativo para a pasta 'exercicios'
    pasta_exercicios = os.path.join(os.path.dirname(__file__), 'exercicios')
    exercicios = listar_exercicios_com_primeira_linha(pasta_exercicios)
    
    mostrar_menu(exercicios)
    
    while True:
        try:
            escolha = int(input("Sua escolha: "))
            if escolha == 0:
                print("\nSaindo...\n")
                break
            elif 1 <= escolha <= len(exercicios):
                executar_exercicio(escolha, exercicios, pasta_exercicios)
            else:
                print("\nEscolha inválida, tente novamente.\n")
            
            # Perguntar ao usuário se ele deseja ver a lista novamente
            mostrar_novamente = input("\nDeseja ver a lista de exercícios novamente? (s/n): ").strip().lower()
            if mostrar_novamente == 's':
                mostrar_menu(exercicios)
                
        except ValueError:
            print("\nPor favor, digite um número válido.\n")
