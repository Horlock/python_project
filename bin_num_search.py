vetor = [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, \
        17, 18, 19, 20, 21, 23, 25, 29, 31, 35, 37, 41, 48, 49, \
        50, 51, 53, 55, 58, 62, 64, 68, 69, 71, 72, 73, 74, 75, \
        78, 79, 81, 82, 84, 85, 87, 88, 89, 91, 92, 93, 94, 95, 100]

def binSearch(vetor, valor):
    inicio = 0
    fim = len(vetor) - 1
    while (inicio <= fim):
        meio = (inicio + fim) // 2
        if(vetor[meio] == valor):
            return print("Valor: %d\nIndice: %d" %(vetor[meio], meio))
        elif (vetor[meio] < valor):
            inicio = meio + 1
        elif (vetor[meio] > valor):
            fim = meio - 1
    else:
        return print('-1')

valor= int(input("Digite um valor (inteiro) a ser procurado: "))

binSearch(vetor, valor)