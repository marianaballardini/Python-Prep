import datetime
x = datetime.datetime.now()
print("Ahora =",x)
x = datetime.datetime(2020, 5, 10)
print("Fecha fija =",x)

fecha_hora = '2022-05-10 12:30:00'
objeto_datetime = datetime.datetime.strptime(fecha_hora, '%Y-%m-%d %H:%M:%S')
print("objeto datetime =", objeto_datetime)
marca_de_tiempo = datetime.datetime.timestamp(objeto_datetime)
print("timestamp =", marca_de_tiempo)
fecha_hora2 = datetime.datetime.fromtimestamp(marca_de_tiempo)
print("fecha hora =", fecha_hora2)