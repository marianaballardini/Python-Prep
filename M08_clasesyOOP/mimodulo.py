class funciones_m7:
    def __init__(self, lista7):
        self.lista7 = lista7

    def verifica_primo(self):
        for i in self.lista7:
            if i < 2:
                print('El elemento', i, 'no es primo')
            elif i == 2:
                print('El elemento', i, 'es primo')
            elif self.__verifica_primo(i):
                print('El elemento', i, 'es primo')
            else:
                print('El elemento', i, 'NO es primo')

    def __verifica_primo(self, num):
        es_primo = True
        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                break
        return es_primo

    def modal(self):
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista7) == 0:
            return None
        for elemento in self.lista7:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return f"El numero modal es {moda} y se repite {maximo} veces."

    def conversion_grados(self, origen, destino):
        for i in self.lista7:
            print(f'{i} grados en {origen} equivalen a {self.__conversion_grados(i, origen, destino)} grados {destino}')

    def __conversion_grados(self, valor, origen, destino):
        if origen == 'celsius' and destino == 'celsius':
            valor_destino = valor
        elif origen == 'celsius' and destino == 'farenheit':
            valor_destino = (valor * 9 / 5) + 32
        elif origen == 'celsius' and destino == 'kelvin':
            valor_destino = valor + 273.15
        elif origen == 'farenheit' and destino == 'celsius':
            valor_destino = (valor - 32) * 5 / 9
        elif origen == 'farenheit' and destino == 'farenheit':
            valor_destino = valor
        elif origen == 'farenheit' and destino == 'kelvin':
            valor_destino = ((valor - 32) * 5 / 9) + 273.15
        elif origen == 'kelvin' and destino == 'celsius':
            valor_destino = valor - 273.15
        elif origen == 'kelvin' and destino == 'farenheit':
            valor_destino = ((valor - 273.15) * 9 / 5) + 32
        elif origen == 'kelvin' and destino == 'kelvin':
            valor_destino = valor
        else:
            print('Parámetros de Origen y/o Destino incorrectos')
            return None

        return valor_destino


    def factorial(self):
        for i in self.lista7:
            resultado = self.__factorial(i)
            print(f'El factorial de {i} es: {resultado}')
     

    def __factorial(self, elemento):
        if type(elemento) != int or elemento < 0:
            return None
        if elemento == 0 or elemento == 1:
            return 1

        resultado = elemento
        resultado *= self.__factorial(elemento - 1)

        return resultado


