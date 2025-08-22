import json
import os

def nome_do_programa():
    os.system('cls')
    print("""  █▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀█   █▀▀▄ █▀▀█   █▀▀▄ █░█
  █▀▀▄ █▄▄█ █░░█ █░░ █░░█   █░░█ █░░█   █░▒█ █▀▄
  █▄▄█ ▀░░▀ ▀░░▀ ▀▀▀ ▀▀▀▀   ▀▀▀░ ▀▀▀▀   █▄▄▀ ▀░▀\n""")

def funcoes_do_programa():
    print('1.Login')
    print('2.Listar Usuários')
    print('3.Cadastrar Usuário.')
    print('4.Ativar Usuário.')
    print('5.Depositar Dinheiro.')
    print('6.Retirar Dinheiro.')
    print('7.Denúncias.')
    print('8.Sair\n')

def voltar_ao_menu_principal():
    str(input('\nAperte ENTER para voltar ao Menu Principal: '))
    main()

def login():
    token = input('\nPara fazer seu login, digite seu Nome de Usuário: ')
    senha = input('\nAgora digite sua senha para fazer login: ')
    for usuario in usuarios:
        if token.lower() == usuario['nome'].lower() and senha.lower() == usuario['senha'].lower():
            print('Login feito com sucesso.')
            voltar_ao_menu_principal()
    print('Usuário ou senha incorreto, tente novamente.')
    voltar_ao_menu_principal()

def ativar_usuario_ativado():
    ativar_cadastro = input(str('Digite o nome do cliente que deseja ativar: '))
    usuarioencontrado = False
    for cliente in usuarios:
        if ativar_cadastro == cliente['nome']:
            usuarioencontrado = True
            cliente['ativado'] = True
            print('Usuário ativado com sucesso! Fique a vontade para usar sua conta bancária.')
            salvar_usuarios()
    if not usuarioencontrado:
        print('Usuário não encontrado')
    voltar_ao_menu_principal()

def carregar_users():
    if os.path.exists('usuarios.json'):
        with open('usuarios.json', 'r', encoding='utf-8',) as users:
            return json.load(users)
    else:
        return []

usuarios = carregar_users()

def salvar_usuarios():
    with open('usuarios.json', 'w', encoding='utf-8') as users:
        json.dump(usuarios, users, ensure_ascii=False, indent=4)

def cadastrar_usuario():
    os.system('cls')
    usuario_ativado = input('Coloque o Nome de Usuário que você deseja cadastrar: ')
    usuario_senha = input('Insira uma senha para o Usuário que você deseja cadastrar: ')
    usuario_categoria = input('Insira a categoria do Usuário que você deseja cadastrar: ')
    usuario_esta_ativo = False
    print('Usuário ativado com sucesso!')
    usuarios.append({
        'nome': usuario_ativado,
        'categoria': usuario_categoria,
        'ativado': usuario_esta_ativo,
        'senha': usuario_senha
        })
    salvar_usuarios()
    voltar_ao_menu_principal()

def listar_usuario():
    os.system('cls')
    print('Usuários cadastrados:\n')
    for pessoa in usuarios:
        nome_cliente = pessoa['nome']
        categoria_client = pessoa['categoria']
        esta_ativado = 'Conta Ativada!' if pessoa['ativado'] else 'A conta ainda não está ativada.'
        print(f'|{nome_cliente}\n|{categoria_client}\n|Estado da conta: {esta_ativado}\n')
    voltar_ao_menu_principal()
    
def depositar():
    str(input('Quanto você deseja depositar? '))
    print('Depositado com sucesso!')

def retirar():
    str(input('Quanto você deseja retirar? '))
    print('Dinheiro retirado com sucesso!')

def denunciar():
    print('Para fazer uma Denúncia, preencha o formulário a seguir: https://dk/banco/report.com')

def opcao_invalida():
    print('\nOpção invalida!')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        global sair
        desejo = int(input('Oque deseja fazer? '))
        if desejo == 1:
            login()
        elif desejo == 3:
            cadastrar_usuario()
        elif desejo == 2:
            listar_usuario()
        elif desejo == 5:
            depositar()
        elif desejo == 6:
            retirar()
        elif desejo == 7:
            denunciar()
        elif desejo == 8:
            sair = True
        elif desejo == 4:
            ativar_usuario_ativado()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

sair = False

def main():
    while True:
        nome_do_programa()
        funcoes_do_programa()
        escolher_opcao()
        if sair:
            print('\n' * 100)
            break

if __name__ == '__main__':
    main()
