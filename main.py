usuarios = []
usuario = {}

# Funções
def header(txt):
    print('=' * 65)
    print(f'{txt:^65}')
    print('=' * 65)

def menu_principal():
    header('MENU PRINCIPAL')
    print('''[ 1 ] Cadastro 
[ 2 ] Login
[ 0 ] Sair''')
    while True:
        nav_menu = int(input('Que aba deseja acessar? '))
        if nav_menu not in [1, 2, 0]:
            print('Erro! O valor inserido é inválido para a operação atual.')
        else:
            break
    if nav_menu == 1:
        cadastro()
    elif nav_menu == 2:
        login()
    elif nav_menu == 0:
        print('Encerrando . . .')

def menu_principal_logado():
    header('MENU PRINCIPAL')
    print('''[ 1 ] Cadastro 
[ 2 ] Login
[ 3 ] Lista de Cadastros
[ 0 ] Sair''')
    while True:
        nav_menu = int(input('Que aba deseja acessar? '))
        if nav_menu not in [1, 2, 3, 0]:
            print('Erro! O valor inserido é inválido para a operação atual.')
        else:
            break
    if nav_menu == 1:
        cadastro()
    elif nav_menu == 2:
        login()
    elif nav_menu == 3:
        lista_usuarios()
    elif nav_menu == 0:
        print('Encerrando . . .')

def cadastro():
    usuario.clear()
    while True:
        usuario["E-mail"] = str(input('Insira seu e-mail: '))
        if '@' not in usuario["E-mail"]:
            print('Erro! O endereço de e-mail inserido é inválido.')
        else:
            break
    usuario["Senha"] = str(input('Insira sua senha: '))

    while True:
        conf_cadastro = input('Confirma os dados inseridos [S/N]? ').upper()[0]
        if conf_cadastro not in 'SN':
            print('O valor inserido é inválido para a operação atual.')
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
            print('Erro! O valor inserido é inválido para a operação atual.')
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
            user["Permissão"] = True
            print('Você está logado!')
            menu_principal_logado()
        else:
            print('E-mail ou senha incorretos!')
            print('''[ 1 ] Tentar novamente
[ 0 ] Voltar''')
            nav_login = int(input('Que aba deseja acessar? '))
            while True:
                if nav_login not in [1, 0]:
                    print('Erro! O valor inserido é inválido.')
                else:
                    break
            if nav_login == 1:
                login()
            else:
                menu_principal()


def lista_usuarios():
    header('USUÁRIOS CADASTRADOS')
    if usuarios:
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

#Programa Principal
menu_principal()
