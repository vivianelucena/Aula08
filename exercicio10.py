'''Faça um código para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois
vetores A e B (de tamanho N cada um) e depois armazenar em um terceiro vetor Soma a soma dos
elementos do vetor A com os do vetor B (respeitando as mesmas posições) e escrever o vetor Soma.'''

vetor = int(input('Digite o tamanho do vetor: '))

vetorA = [0] * vetor
vetorB = [0] * vetor
soma = [0] * vetor

for a in range(vetor):
    vetorA[a] = int(input(f'Digite o primeiro número: '))
    vetorB[a] = int(input(f'Digite o segundo número: '))
    soma[a] = vetorA[a] + vetorB[a]
    print(f'{vetorA[a]} + {vetorB[a]} = {soma[a]}')