# ENZO RICARDO E SARAH MANEIRA
# SEÇÃO 2

import json
import hashlib
import time
import itertools

def decifrar_hash():
    print("Quebra de senha\n")
    
    caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z']
    
    with open("usuarios.json", "r") as file:
        usuarios = json.load(file)
        
    tempo_inicial = time.time()
    
    for usuario in usuarios[:4]:  # só os 4 primeiros
        senha_hash = usuario["password"]
        senha_encontrada = ""
        
        inicio = time.time()
        
        for tentativa in itertools.product(caracteres, repeat=4):
            senha_tentativa = ''.join(tentativa)
            tentativa_hash = hashlib.sha256(senha_tentativa.encode()).hexdigest()
            
            if tentativa_hash == senha_hash:
                senha_encontrada = senha_tentativa
                break
        
        fim = time.time()
        
        if senha_encontrada:
            print(f"Senha encontrada: {senha_encontrada} para o usuário {usuario['username']} em {fim - inicio:.3f} segundos")
        else:
            print(f"Senha não encontrada para o usuário {usuario['username']}")
    
    tempo_final = time.time()
    print(f"\nTempo total de execução: {tempo_final - tempo_inicial:.2f} segundos")
    

if __name__ == "__main__":
    decifrar_hash()
