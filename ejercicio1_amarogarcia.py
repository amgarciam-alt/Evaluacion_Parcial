def leer_opcion():
    while True:
        try:
            opcion = int(input('Ingrese una opcion 1-6: '))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print('Opcion en un rango no valido')
        except ValueError:
            print('Solo caracteres no numericos')