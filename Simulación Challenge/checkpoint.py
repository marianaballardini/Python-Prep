# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
    '''
    #Tu código aca:
    if type(numero) != int:
        return 'El numero debe ser un entero'
   
    if numero < 0:
        return 'El numero debe ser positivo'
    
    
    if numero <= 1:
        return 1
    
    resultado = 1
    for i in range(1,numero+1):
        resultado *= i
        return resultado
   

def EsPrimo(valor):
    '''
    Esta función devuelve el valor booleano True si el número reibido como parámetro es primo, de lo 
    contrario devuelve False..
    En caso de que el parámetro no sea de tipo entero debe retornar nulo.
    Recibe un argumento:
        valor: Será el número a evaluar
    Ej:
        EsPrimo(7) debe retornar True
        EsPrimo(8) debe retornar False
    '''
    #Tu código aca:
    esprimo= True
    if type(valor) != int:
        None
    else:
        for i in range (2,valor):
            if valor % i == 0:
                    esprimo = False
            else:
                esprimo = True
            return esprimo

    
def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''
    class Animal:
        def __init__(self,edad,especie,color):
            self.especie = especie
            self.color = color
            self.edad  = 0
        

        def CumpliAnios(self):
            self.edad +=1
            return self.edad
    
    return Animal(especie , color)
a1=ClaseAnimal("perro","negro")
a1.CumpliAnios()
a1.CumpliAnios()
a1.CumpliAnios()
