import sys
if len(sys.argv) == 4:
    parametros = (sys.argv[1] , sys.argv[2] , sys.argv[3])
    for i in parametros:
        print(parametros)
else:
    print('Parametros incorrectos, debes ingresar 3 parametros')
    