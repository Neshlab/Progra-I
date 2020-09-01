def crear_matriz():
    matriz = []
    filas = int(input("ingrese el numero de filas "))
    columnas = int(input("ingrese el numero de columnas "))
    for i in range(filas):
        matriz.append([0] * columnas)
    
    return matriz

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
	    for j in range(len(matriz[i])):
		    print("%3d" %matriz[i][j], end="")
	    print()

def hacer_una_cruz(matriz):
    filas = int(input("ingrese el numero de filas a elegir "))
    columnas = int(input("ingrese el numero de filas a columnas "))
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][columnas] = 1
            matriz[filas][j] = 1
            
    return matriz        


def seleccionar_butaca(matriz):

    filas = int(input("ingrese el numero de filas a elegir "))
    columnas = int(input("ingrese el numero de filas a columnas ")) 
    for i in range(len(matriz)):
        if filas == i:
            for j in range(len(matriz[i])):
                if columnas == j and matriz[i][j] != 1:
                    matriz[i][j] = 1 
                elif columnas == j and matriz[i][j] == 1:
                    print("butaca reservada")    
    return matriz
        
matriz = crear_matriz()

def main(c):
    while c != -1:
        c = int(input("desea reservar una butaca? "))
        if c == -1:
            break # ESTA MAL LO SE PERO LO TERMINE EN CLASES
        b = seleccionar_butaca(matriz)
        imprimir_matriz(b)

if __name__ == '__main__':
    main(0)
    


