# HashCriptografico
## 1 - Autenticação

Desenvolva um programa que implemente uma aplicação que possui duas funcionalidades: cadastrar
e autenticar usuário.

Um usuário possui os seguintes atributos:
• Nome (string de 4 caracteres)
• Senha (string de 4 caracteres)

Além disso, o cadastro dos usuários deve ser armazenado em um arquivo (TXT, CSV ou JSON). A
aplicação deve utilizar o algoritmo SHA-256 para realizar como função hash para o armazenamento
da senha.

-------------------------------------------

## 2 - Quebra de hash criptográfico
Pesquise um algoritmo/código fonte de força bruta para SHA-256 e processe o arquivo que contém as
senhas armazenadas conforme implementado na Seção 1. Compute o tempo necessário para realizar
a quebra de hash de 4 usuários (tempo total e tempo por senha).

-------------------------------------------

## 3 Solução
Implemente uma solução para reduzir a possibilidade de sucesso de um ataque de força bruta no programa desenvolvido na Seção 1. Após a implementação, execute novamente o algoritmo/código-fonte de força bruta para quebra das senhas. Compute o tempo necessário para realizar a quebra de hash dos mesmos 4 usuários. O resultado esperado é que o tempo aumente muito ou que você não consiga quebrar as senhas.


