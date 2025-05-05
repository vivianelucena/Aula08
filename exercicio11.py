'''Faça um código para ler 10 números e guardar num vetor. Após isto, ler mais um
número qualquer, calcular e escrever quantas vezes esse número aparece no vetor.'''

cont = 0
vetor = [0] * 10

for a in range(len(vetor)):
    vetor[a] = int(input('Digite um número para armazenar: '))

numero = int(input('Digite um número: '))

for b in range(len(vetor)):
    if numero == vetor[b]:
        cont = cont + 1

print(f'O número {numero} aparece {cont}x no vetor.')