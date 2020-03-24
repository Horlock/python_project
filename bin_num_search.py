vector = [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, \
        17, 18, 19, 20, 21, 23, 25, 29, 31, 35, 37, 41, 48, 49, \
        50, 51, 53, 55, 58, 62, 64, 68, 69, 71, 72, 73, 74, 75, \
        78, 79, 81, 82, 84, 85, 87, 88, 89, 91, 92, 93, 94, 95, 100]

def binSearch(vector, value):
    start = 0
    end = len(vector) - 1
    while (start <= end):
        mid = (start + end) // 2
        if(vector[mid] == value):
            return print("Valor: %d\nÍndice: %d" %(vector[mid], mid))
        elif (vector[mid] < value):
            start = mid + 1
        elif (vector[mid] > value):
            end = mid - 1
    else:
        return print('-1')

value = int(input("Digite um valor (inteiro) a ser procurado: "))

binSearch(vector, value)