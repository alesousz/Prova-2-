#Escreva um programa, em python, que atenda às seguintes funcionalidades:
#leia valores reais e armazene-os em uma matriz 6×6.
#calcule a média dos elementos da área assinalada em cinza (ver figura abaixo)
#determinar o maior elemento contido na matriz;
#verificar se um determinado valor (passado como parâmetro) está contido na matriz. Esse valor deve ser informado pelo usuário, via leitura;
#fazer a varredura da matriz e devolução dos elementos contidos em sua diagonal principal, copiados para um vetor.
def le_matriz():
    matriz = []
    for i in range(6):
        linha = []
        for y in range(6):
            valor = int(input(f'Digite o valor na posição [{i + 1}][{y + 1}]: '))
            linha.append(valor)
        matriz.append(linha)
    return matriz
#_______________________________________________________________________________________________________________________
def media_matriz(matriz):
    soma = 0
    count = 0
    for i in range(6):
        for y in range(6):
            if (i >= 1 and i <= 4) and (j >= 1 and j <= 4):
                soma += matriz[i][y]
                count += 1
    return soma/count
# ______________________________________________________________________________________________________________________
def maior_elemento():
# ______________________________________________________________________________________________________________________
def contido_matriz():
# ______________________________________________________________________________________________________________________
def varredura_matriz():
#_______________________________________________________________________________________________________________________
print("Digite os valores da matriz:")
M = le_matriz()

print(M)
#______________________________________________________________________________________________________________________
soma =
print(soma)