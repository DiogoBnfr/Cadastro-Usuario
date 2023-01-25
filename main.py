from sys import exit
from colorama import Fore

usuarios = []
usuario = {"E-mail": '', "Senha": ''}
usuario_logado = {"Permissão": 'offline'}

# Funções
def header(txt):
    print(Fore.GREEN + ('=' * 65) + Fore.RESET)
    print(f'{txt:^65}')
    print(Fore.CYAN +  ('=' * 65) + Fore.RESET)

def erro(txt):
    print(Fore.RED + f'{str(txt)}' + Fore.RESET)

def menu_principal():
    header('MENU PRINCIPAL')
    print('''[ 1 ] Cadastro 
[ 2 ] Login
[ 3 ] Lista de Cadastros
[ 4 ] Excluir Cadastro
[ 0 ] Sair''')
    while True:
        nav_menu = int(input('Que aba deseja acessar? '))
        if nav_menu not in [1, 2, 3, 4, 0]:
            erro('Erro! O valor inserido é inválido para a operação atual.')
        else:
            break
    if nav_menu == 1:
        cadastro()
    elif nav_menu == 2:
        login()
    elif nav_menu == 3:
        if usuario_logado["Permissão"] == 'adm':
            lista_usuarios()
        else:
            if usuario_logado["Permissão"] == 'offline':
                erro('Nenhum usuário logado. Faça login e tente novamente.')
            else:
                erro('O usuário logado não possui a permissão necessária para acessar essa aba.')
            menu_principal()
    elif nav_menu == 4:
        excluir_usuario()
    elif nav_menu == 0:
        erro('Encerrando . . .')
        exit()

def cadastro():
    header('CADASTRO')
    usuario.clear()
    while True:
        usuario["E-mail"] = str(input('Insira seu e-mail: '))
        if '@' not in usuario["E-mail"]:
            erro('Erro! O endereço de e-mail inserido é inválido.')
        else:
            break
    usuario["Senha"] = str(input('Insira sua senha: '))

    while True:
        conf_cadastro = input('Confirma os dados inseridos [S/N]? ').upper()[0]
        if conf_cadastro not in 'SN':
           erro('O valor inserido é inválido para a operação atual.')
        else:
            break
    if conf_cadastro == 'S':
        usuarios.append(usuario.copy())
        print('Cadastro concluído!')
    else:
        cadastro()

    while True:
        cadastro_add = input('Deseja cadastrar mais usuários[S/N]? ').upper()[0]
        if cadastro_add not in 'SN':
            erro('Erro! O valor inserido é inválido para a operação atual.')
        else:
            break
    if cadastro_add == 'S':
        cadastro()
    else:
        menu_principal()

def login():
    header('LOGIN')
    login_email = str(input('Digite seu e-mail: '))
    login_senha = str(input('Digite sua senha: '))
    for user in usuarios:
        if login_email == user["E-mail"] and login_senha == user["Senha"]:
            usuario_logado.clear()
            usuario_logado["Permissão"] = 'adm'
            usuario_logado["E-mail"] = login_email
            usuario_logado["Senha"] = login_senha
            print('Você está logado!')
            menu_principal()
    else:
        erro('Erro! E-mail ou senha incorretos!')
        print('''[ 1 ] Tentar novamente
[ 0 ] Voltar''')
        nav_login = int(input('Que aba deseja acessar? '))
        while True:
            if nav_login not in [1, 0]:
                erro('Erro! O valor inserido é inválido.')
            else:
                break
        if nav_login == 1:
            login()
        else:
            menu_principal()


def lista_usuarios():
    header('USUÁRIOS CADASTRADOS')
    if len(usuarios) >= 1:
        print(f'{"N.":<5}', end='')
        for key in usuario.keys():
            print(f'{key:^30}', end='')
        print()
        print('-' * 65)
        for n, user in enumerate(usuarios):
            print(f'{n:<5}{user["E-mail"]:^30}{user["Senha"]:^30}')
        print('=' * 65)
    else:
        print()
        print()
        print()
        print(f'{"Nenhum cadastro encontrado.":^65}')
        print()
        print()
    print()
    menu_principal()

def excluir_usuario():
    header('EXCLUIR CADASTRO')
    if usuario_logado["Permissão"] == 'offline':
        erro('Você precisa fazer login com uma conta já cadastrada antes de excluir.')
        menu_principal()
    erro('Deseja realmente excluir seu cadastro? A ação não poderá ser desfeita.')
    usuario_conf = str(input('Digite sua senha para confirmar ou [N] para cancelar: '))
    if usuario_conf in 'Nn':
        menu_principal()
    for CADASTRO in usuarios:
        if CADASTRO["Senha"] == usuario_conf:
            if CADASTRO["E-mail"] == usuario_logado["E-mail"] and CADASTRO["Senha"] == usuario_logado["Senha"]:
                usuario_logado["Permissão"] = 'offline'
            del usuarios[usuarios.index(CADASTRO)]
            print('Cadastro excluído!')
            menu_principal()
        else:
            erro('A senha digitada não corresponde a nenhuma senha cadastrada.')
            excluir_usuario()

#Programa Principal
menu_principal()
