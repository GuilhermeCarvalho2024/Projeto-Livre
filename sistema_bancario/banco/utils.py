import json
import os

def ler_json(caminho):
    if os.path.exists(caminho):
        with open(caminho, 'r') as arquivo:
            return json.load(arquivo)
    return None

def escrever_json(caminho, dados):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    
    with open(caminho, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def limpar_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')