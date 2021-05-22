

nombre = input("Ingrese su nombre: ")
saludo = 'Hola '+nombre+'. Bienvenido a tu equipo! El numero de caracteres de este texto es:'
tamanio_saludo = len(saludo)
tamanio_num = len(str(tamanio_saludo))

print(saludo, tamanio_saludo+tamanio_num)
