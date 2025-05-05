'''Altere o sistema anterior e faça um sistema de login, pedindo a senha do usuário e
mostrando seu nome e a mensagem, login efetuado com sucesso.'''

usuario = input('Digite o login: ')
senha = input('Digite a senha: ')

nomes = ['ana', 'beto', 'clara', 'danilo', 'ellie']
senhaCorreta = ['123', '345', '567', '789', '901']

loginEfetuado = False

for a in range(len(nomes)):
    if usuario == nomes[a] and senha == senhaCorreta[a]:
        print(f'Login efetuado com sucesso. Bem-vindo(a) {nomes[a]}!')
        loginEfetuado = True
    else:
        loginEfetuado = False