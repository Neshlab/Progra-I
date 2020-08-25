import random

# genera una lista de 50 ints
def RandomListGenerator(lista = []):
    i = 0
    for i  in range(i,50):
        varTemp = random.randint(1,100)
        lista.append(varTemp)

    return(lista)

# controla si la lista tiene elementos duplicados
def checkDuplicatedValues(lista):
    boolean = False
    if len(lista) != len(set(lista)):
        boolean = True
    else:
        boolean = False    
    return(boolean)

# genera una nueva lista sin elementos repetidos 
# // No Ordena la Misma en caso de necesitar ordenar simplemente usar la funcion
#   set(myList) on en caso de necesitar que siga siendo una lista list(set(mylist))

def listOnlyWithOriginalValues(lista = [0,1]):
    list_dup = set()
    list_controled =  []
    for x in lista:
        if x not in list_dup:
            list_controled.append(x)
            list_dup.add(x)
    return(list_controled)

#test para la generacion de lista aleatoria
def GeneratorListTest(lista_for_test):
    ListTested = RandomListGenerator(lista_for_test)
    TestGeneratorFunc = len(ListTested)
    if TestGeneratorFunc == 50:
        test = True
    else:
        test = False
    print("la lista Testeada fue: ", ListTested)
    return(test)

#test para checkear si la lista tiene repetidos
def TestCheckerListDupl(x = 0):
    if  x == 0:
        x = list_with_dups = [0,0,0,0]
        print(list_with_dups)
        
    else:
        x = list_without_dups = [1,2,3,4]
        print(list_without_dups)
        
    funcListSender = checkDuplicatedValues(x)

    if funcListSender is True:
        test = True
    else:
        test = False
    return(test)

def main():
    print("ingrese 1 en caso de que desee realizar un test o 2 en caso de que desee realizar la carga manual")

    #   USER INPUT    
    FirstInput = int(input("ingrese su respuesta: "))
    
    if FirstInput == 1:
    #   TEST       
        lista_for_test = []

        GeneratorListTest_try = GeneratorListTest(lista_for_test)

        if GeneratorListTest_try == True:
           print("Test de Generacion de lista de 50 elementos pasada con EXITO")
        else:
           print("Test de Generacion de lista de 50 elementos FALLO")
        
        print("Test de Control de Elementos de una lista, si checkear una lista con repetidos digite 0, en caos contrario cualquier otro numero" )   
        
        TestDupInput = int(input("ingrese su respuesta: "))
        
        if TestDupInput == 0:
            TestCheckerListDupl_try = TestCheckerListDupl(TestDupInput)
            if TestCheckerListDupl_try == True:
                print("la lista ingresada contiene Elementos Repetidos, Test pasado con Exito")
            else:
                print("la lista ingresada contiene Elementos Repetidos, Test pasado con Exito")    
    else:
    #   PRODUCTION        
        lista = []
        x = RandomListGenerator(lista)
        y = checkDuplicatedValues(x)    
        z = listOnlyWithOriginalValues(x)
        print("la lista generada es ", x)
        if y ==True:
            print("la lista no CONTIENE elementos repetidos")
        else:    
            print("la lista CONTIENE elementos repetidos")
        print("la lista sin repetidos es", z)

main()

#corregir DONE

#test_bot DONE 

#list generator by input DONE

#document DONE
