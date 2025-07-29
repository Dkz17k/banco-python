
import os

usuarios = [{'nome':'Dhuan','categoria':'cliente','ativado':True},{'nome':'Ilenir','categoria':'cliente','ativado':False},{'nome':'Ivonir','categoria':'cliente','ativado':True},{'nome':'Arthur','categoria':'cliente','ativado':False}]

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
    str(input('\nPara fazer seu login, digite seu Nome de Usuário: '))
    print('Logado com sucesso!')

def ativar_usuario_ativado():
    ativar_cadastro = input(str('Digite o nome do cliente que deseja ativar: '))
    usuarioencontrado = False
    for cliente in usuarios:
        if ativar_cadastro == cliente['nome']:
            usuarioencontrado = True
            cliente['ativado'] = True
            print('Usuário ativado com sucesso! Fique a vontade para usar sua conta bancária.')
    if not usuarioencontrado:
        print('Usuário não encontrado')
    voltar_ao_menu_principal()
    main()

def cadastrar_usuario():
    os.system('cls')
    usuario_ativado = input('Coloque o Nome de Usuário que você deseja cadastrar: ')
    usuario_categoria = input('Insira a categoria do Usuário que você deseja cadastrar: ')
    usuario_esta_ativo = False
    print('Usuário ativado com sucesso!')
    usuarios.append({'nome': usuario_ativado,'categoria': usuario_categoria,'ativado': usuario_esta_ativo})
    voltar_ao_menu_principal()
    main()

def listar_usuario():
    os.system('cls')
    print('Usuários cadastrados:\n')
    for pessoa in usuarios:
        nome_cliente = pessoa['nome']
        categoria_client = pessoa['categoria']
        esta_ativado = 'Conta Ativada!' if pessoa['ativado'] else 'A conta ainda não está ativada.'
        print(f'|{nome_cliente}\n|{categoria_client}\n|Estado da conta: {esta_ativado}\n')
    voltar_ao_menu_principal()
    main()
    '''
    Função que exibe uma lista de todos os usuários com base no seu cadastro: Nome; Categoria; 
    '''
        
def depositar():
    str(input('Quanto você deseja depositar? '))
    print('Depositado com sucesso!')
    '''
    Função que pergunta ao usuário a quantia de dinheiro que ele deseja depositar com base no valor inserido pelo usuário. ( sem validações por ser um projeto simples )
    '''

def retirar():
    str(input('Quanto você deseja retirar? '))
    print('Dinheiro retirado com sucesso!')
    '''
    Função que pergunta ao usuário a quantia de dinheiro que ele deseja retirar com base no valor inserido pelo usuário. ( sem validações por ser um projeto simples )
    '''

def denunciar():
    print('Para fazer uma Denúncia, preencha o formulário a seguir: https://dk/banco/report.com')
    '''
    Função que exibe uma mensagem indicando um caminho para o usuário registrar uma denuncia.
    '''

def sair():
    os.system('cls')
    print('Saindo do app...\n')
    '''
    Função que fecha a aplicação e encerra sua execução.
    '''

def opcao_invalida():
    print('\nOpção invalida!')
    voltar_ao_menu_principal()
    main()
    '''
    Função que trata um erro do usuário ao escolher uma função inválida.
    '''

def escolher_opcao():
    try:
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
            sair()
        elif desejo == 4:
            ativar_usuario_ativado()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    '''
    Função que pergunta ao usuário o que ele deseja fazer na plataforma e executando uma determinada ação conforme seu desejo.
    ''' 

def main():
    nome_do_programa()
    funcoes_do_programa()
    escolher_opcao()
    '''
    Função principal, a raíz do projeto que executa organizadamente cada bloco de codigo.
    '''

if __name__ == '__main__':
    main()
