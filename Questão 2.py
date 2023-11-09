#Faça um programa que leia quatro matrizes inteiras, 5 × 5 (A, B, C e D), com pelo menos dois subprogramas:
# um que carrega valores em uma matriz, a ser usado para a leitura das quatro matrizes, e um segundo que recebe duas matrizes 5 × 5 e calcula a matriz soma.
#Aplique esse último subprograma para obter A + B, C + D e A + C

#______________________________________________________________________________________________________________________
def le_matriz():
    matriz = []
    for i in range(2):
        linha = []
        for y in range(5):
            valor = int(input(f'Digite o valor na posição [{i + 1}][{y + 1}]: '))
            linha.append(valor)
        matriz.append(linha)
    return matriz
#______________________________________________________________________________________________________________________
def soma_matriz(matriz1,matriz2):
    resultado = []
    for i in range(2):
        linha = []
        for y in range(5):
            soma = matriz1[i][y] + matriz2[i][y]
            linha.append(soma)
        resultado.append(linha)
    return resultado
#______________________________________________________________________________________________________________________
print("Digite os valores da matriz A:")
A = le_matriz()

print("Digite os valores da matriz B:")
B = le_matriz()

print("Digite os valores da matriz C:")
C = le_matriz()

print("Digite os valores da matriz D:")
D = le_matriz()
#______________________________________________________________________________________________________________________
print(A)
print(B)
print(C)
print(D)
#______________________________________________________________________________________________________________________
resultado_AB = soma_matriz(A,B)
resultado_AC = soma_matriz(A,C)
resultado_CB = soma_matriz(C,B)
#______________________________________________________________________________________________________________________
print(A)
print(B)
print(C)
print(D)
#______________________________________________________________________________________________________________________
print("A + B:")
for linha in resultado_AB:
    print(linha)

print("C + B:")
for linha in resultado_CB:
    print(linha)

print("A + C:")
for linha in resultado_AC:
    print(linha)
#______________________________________________________________________________________________________________________