'''Faça um código para ler 5 números e armazenar em um vetor. Após a leitura total dos 5 números,
o código deve escrever esses 5 números lidos na ordem inversa.'''

numeros = [0] * 5

for a in range(len(numeros)):
    numeros[a] = int(input(f'Digite um número para armazenar: '))

for b in range(len(numeros)-1,-1,-1):
    print(numeros[b])