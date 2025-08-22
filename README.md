# Sistema Bancário em Python

Um projeto simples de sistema bancário feito em **Python**, com funcionalidades de login, cadastro, ativação de usuário e transações simuladas.

---

## Funcionalidades

O programa oferece as seguintes opções:

1. **Login**: Permite que o usuário faça login com nome de usuário e senha.  
2. **Listar Usuários**: Exibe todos os usuários cadastrados, suas categorias e estado da conta (ativada ou não).  
3. **Cadastrar Usuário**: Permite criar um novo usuário com nome, senha e categoria.  
4. **Ativar Usuário**: Ativa a conta de um usuário cadastrado.  
5. **Depositar Dinheiro**: Simula depósito em conta (não há armazenamento real do valor).  
6. **Retirar Dinheiro**: Simula retirada de dinheiro.  
7. **Denúncias**: Disponibiliza link para formulário de denúncias.  
8. **Sair**: Fecha o programa.

---

## Estrutura do Código

- `usuarios.json`: Arquivo usado para armazenar os usuários cadastrados.  
- `main.py`: Script principal que contém toda a lógica do sistema.

Principais funções do código:

- `nome_do_programa()`: Exibe o título estilizado do programa.  
- `funcoes_do_programa()`: Mostra o menu de opções.  
- `carregar_users()`: Carrega os usuários salvos no arquivo JSON.  
- `salvar_usuarios()`: Salva os usuários no arquivo JSON.  
- `cadastrar_usuario()`, `login()`, `listar_usuario()`, `ativar_usuario_ativado()`, `depositar()`, `retirar()`, `denunciar()`: Funções principais para as operações do sistema.

---

## Como Rodar

1. Certifique-se de ter o **Python 3** e o editor de código **Visual Studio Code** instalado.  
2. Baixe o arquivo "main.py" na sua maquina.
3. Abra o arquivo no editor de código e execute.
