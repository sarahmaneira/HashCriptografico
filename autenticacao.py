# ENZO RICARDO E SARAH MANEIRA
# SEÇÃO 1

import json
import getpass
import hashlib


def cadastrar():
    print("\n- Cadastro de usuário")

    username = input("Nome de usuário (máx 4 caracteres): ") 
    if len(username) > 4:
        print("O nome usuário deve ter no máximo 4 caracteres!")
        return()
    
    password = input("Senha (máx 4 caracteres): ")
    if len(password) > 4:
        print("A senha deve ter no máximo 4 caracteres!")
        return
    
    password = hashlib.sha256(password.encode()).hexdigest() 
    
    
    with open("usuarios.json", "r") as file:
        usuarios = json.load(file)

    for usuario in usuarios:
        if usuario["username"] == username:
            print("Nome de usuário já existe!")
            return
        
        else:
            usuario = usuarios + [{
                "username": username,
                "password": password
            }]
            with open("usuarios.json", "w") as file:
                json.dump(usuario, file)
            

            print("Usuário cadastrado com sucesso!")
            break


def autenticar():
    print("\n- Autenticação de usuário")

    username = input("\nNome de usuário: ")
    password = input("Senha: ")
    password = hashlib.sha256(password.encode()).hexdigest() 
    

    with open("usuarios.json", "r") as file:
        usuarios = json.load(file)

    for usuario in usuarios:
        if usuario["username"] == username and usuario["password"] == password:
            print("\n** Usuário autenticado com sucesso! **\n ")
            return
    print("Usuário ou senha inválidos!")
    return



print("=-"*20)
print("Bem-vindo ao sistema de autenticação!")
print("=-"*20)

while True:
    opcao = input("1- Cadastrar\n2- Autenticar\n3- Sair\nEscolha uma opção: ")
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        autenticar()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
