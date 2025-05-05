'''Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada
lista em um array diferente, após completar a digitação, imprimir , nome, senha e posição
dos dados no array'''

nomes = [''] * 5
senhas = [''] * 5

for a in range(len(nomes)):
    nomes[a] = input(f'Digite o nome: ')
    senhas[a] = input(f'Digite a senha: ')

for b in range(len(nomes)):
    print(f'Posição: {b}. Nome: {nomes[b]}. Senha: {senhas[b]}')