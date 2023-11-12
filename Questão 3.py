#Escreva um programa, em python, que atenda às seguintes funcionalidades:
#leia valores reais e armazene-os em uma matriz 6×6.
#calcule a média dos elementos da área assinalada em cinza (ver figura abaixo)
#determinar o maior elemento contido na matriz;
#verificar se um determinado valor (passado como parâmetro) está contido na matriz. Esse valor deve ser informado pelo usuário, via leitura;
#fazer a varredura da matriz e devolução dos elementos contidos em sua diagonal principal, copiados para um vetor.
def ler_matriz():
    matriz = []
    for i in range(6):
        linha = []
        for j in range(6):
            valor = float(input(f"Informe o valor para a posição ({i + 1},{j + 1}): "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def media_area_cinza(matriz):
    soma = 0
    count = 0
    for i in range(1, 5):
        for j in range(1, 5):
            soma += matriz[i][j]
            count += 1
    return soma / count

def maior_elemento(matriz):
    maior = matriz[0][0]
    for linha in matriz:
        for elemento in linha:
            if elemento > maior:
                maior = elemento
    return maior

def verificar_valor(matriz, valor):
    for linha in matriz:
        if valor in linha:
            return True
    return False

def diagonal_principal(matriz):
    diagonal = []
    for i in range(6):
        diagonal.append(matriz[i][i])
    return diagonal

# Leitura da matriz
minha_matriz = ler_matriz()

# Cálculo da média da área assinalada em cinza
media = media_area_cinza(minha_matriz)
print(f"Média da área assinalada em cinza: {media}")

# Determinar o maior elemento contido na matriz
maior = maior_elemento(minha_matriz)
print(f"Maior elemento na matriz: {maior}")

# Verificar se um determinado valor está contido na matriz
valor_usuario = float(input("Informe um valor para verificar se está na matriz: "))
if verificar_valor(minha_matriz, valor_usuario):
    print(f"O valor {valor_usuario} está na matriz.")
else:
    print(f"O valor {valor_usuario} não está na matriz.")

# Varredura da matriz e devolução dos elementos contidos na diagonal principal
diagonal = diagonal_principal(minha_matriz)
print(f"Elementos na diagonal principal: {diagonal}")
