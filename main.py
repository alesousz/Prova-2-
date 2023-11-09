#Construa um subprograma que, recebendo como parâmetros quatro números inteiros, devolva ao módulo que o chamou a soma dos três maiores números dentre os quatro recebidos.
#O programa principal deverá ler tantos conjuntos de quatro valores quantos o usuário deseje e que acione o subprograma para cada conjunto de valores, apresentando a cada vez a soma produzida.
def lerconjuntosa(a,b,c,d):
    numeros = [a,b,c,d]
    numeros.sort(reverse=True)
    resultado = numeros[0] + numeros[1] + numeros[2]
    return resultado

while True:
    try:
        a = int(input('Digite o valor de A: '))
        b = int(input('Digite o valor de B: '))
        c = int(input('Digite o valor de C: '))
        d = int(input('Digite o valor de D: '))

        resultado = lerconjuntosa(a, b,c ,d)

        print(f'O resultado é {resultado}')

        continuar = str(input('Deseja continuar (S/N)? ')).upper()
        if continuar == 'N':
            break
    except ValueError:
        print('Insira numeros inteiros')
