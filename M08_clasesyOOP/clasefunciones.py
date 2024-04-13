class funciones_m7:
    def __init__(self,lista1):
        self.lista = lista1
        
    def verifica_primo (self):
        for i in self.lista:
            if  self.__verifica_primo(i):
                print(f'El valor {i} es primo')
            else:
                print(f'El valor{i} no es primo')
            
    def __verifica_primo(self,nro):
        es_primo = True  
        for i in range(2, nro):  
            if nro % i == 0:  
                es_primo = False  
                break  
        return es_primo

    def modal (self):
        lista_repetidos = []
        lista_unicos =[]
        
        for numero in self.lista:
            if numero in lista_unicos:
                i = lista_unicos.index(numero)
                lista_repetidos[i] += 1
            else:            
                lista_unicos.append(numero)
                lista_repetidos.append(1)

            moda = lista_unicos [0]
            maximo = lista_repetidos [0]

            for i, numero in enumerate(lista_unicos):
                if lista_repetidos [i] > maximo:
                    moda=lista_unicos[i]
                    maximo= lista_repetidos[i]
        
        return "El valor modal es: " + str(moda) + ', se repite '+ str(maximo)+  ' veces'        
    def conversor_grados (self,origen, destino):
        for i in self.lista:
            print(f'El valor {i} de {origen} convertido a {destino} es: {self.__conversor_grados(i,origen,destino)}')

    def __conversor_grados(self, grados,origen,destino):

        if origen == 'celsius':
            if destino == 'celsius':
                resultado= grados
            elif destino == 'farenheit':
                resultado= (grados*9/5)+32
            elif destino == 'kelvin':
                resultado= grados+273.15

        elif  origen == 'farenheit':
            if destino == 'celsius':
                resultado= (grados-32)* 5/9
            elif destino == 'kelvin':
                resultado= ((grados-32)* 5/9)+273.15
            elif destino=='farenheit':
                resultado=grados

        elif origen == 'kelvin':
            if destino == 'celsius':
                resultado= grados - 273.15
            elif destino == 'farenheit':
                resultado= ((grados-273.15)*9/5)+32
            elif destino == 'kelvin':
                resultado = grados 
        return resultado
    def factorial (self):
        for i in self.lista:
            print(f'El factorial de{i} es {self.__factorial(i)}')

    def __factorial(self,numero):

        if type(numero) != int:
            return 'El numero debe ser un entero'
    
        if numero < 0:
            return 'El numero debe ser positivo'
        
        
        if numero <= 1:
            return 1
        
        else: 
            numero = numero*self.__factorial(numero-1)
            return numero