def crearMatrizF(matriz):
    num = 1
    j = len(matriz)-1
    for i in range(len(matriz)):
                            #importante impide que me salga del rango
        while j >= (len(matriz)-1-i):
            matriz[i][j] = num
            num += 1
            j -= 1
        j = len(matriz) - 1

    return matriz
    

def imprimirMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            print("%3d" %matriz[i][j], end = "")
        print()
        

n = int(input("ingrese el tamaño de la columna deseado: "))

matriz = []
#añado 0 a cada posicion
for i in range(n):
    matriz.append([])
    for j in range(n):
        matriz[i].append(0)
print()
print("Ejercicio F matriz: ")
print()
matriz6 = list(crearMatrizF(matriz))
imprimirMatriz(matriz)
print()
