class funciones_m7:
    def __init__(self,lista1):
        if type ( lista1) != list:
            self.lista=[]
            raise ValueError (f'El tipo de valor ingresado no es correcto ')
        else:
            self.lista = lista1
        
    def verifica_primo (self):
        listaverificados = []
        for i in self.lista:
            if  self.__verifica_primo(i):
                listaverificados.append(i)
            else:
                listaverificados.append(i)
                return listaverificados
            
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
        
        return moda, maximo    


    def conversor_grados (self,origen, destino):

        parametros_esperados = ['celsius', 'kelvin' , ' farenheit']

        lista_conversion = []

        try:
            for i in self.lista:
                lista_conversion.append(self.__conversor_grados(i,origen,destino))
                
           
        except:
            if origen not in parametros_esperados:
                print ( f'El valor origen debe ser alguno de los siguientes:{parametros_esperados} ')
              
            
            if destino not in parametros_esperados:
                 print( f'El valor destino debe ser alguno de los siguientes:{parametros_esperados} ')
        
        return lista_conversion

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
        resultado = []
        
        for i in self.lista:
            resultado.append(self.__factorial(i))
        return resultado

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