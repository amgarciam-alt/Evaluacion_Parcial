def leer_opcion():
    while True:
        try:
            opcion = int(input('Ingrese una opcion 1-4: '))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print('Debe seleccionar una opción válida!!')
        except ValueError:
            print('Debe seleccionar una opción válida!!')

def stock_marca(marca,stock,productos):
    totalstock = 0
    for codigo, datos in productos.items():
        if datos[0].lower() ==marca.lower():
            totalstock +=stock[codigo][1]
    print(f'Los stocks encontrados son: {totalstock}')


def busqueda_precio(precio_min,precio_max,productos,stock):
    resultados = []
    for marca, datos_producto in stock.items():
        precio = datos_producto[0]
        stocks = datos_producto[1]
        if precio_min <=precio<= precio_max and stocks !=0:
            Modelo = productos[marca][0]
            resultados.append(f'{Modelo}--{marca}')

    if len(resultados) == 0:
        print('No hay notebooks en ese rango de precio')
    else:
        resultadofinal = sorted(resultados)
        print(f'Los notebooks entre los precios son: {resultadofinal}')

def validar_codigo(codigo,stock):
    return codigo in stock

def actualizar_precio(codigo,stock,nuevoprecio):
    if validar_codigo(codigo,stock):
        stock[codigo][0] == nuevoprecio
        return True
    return False

def validacion_entero(validacion):
    try:
        valor = int(validacion)
        return valor>=0
    except ValueError:
        return False

def validar_texto(texto):
    if texto.strip() !='':
        return texto

def validar_repetir(respuesta):
    return respuesta in ('s','n')

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
}

stock = {'8475HD': [387990,10], 
         '2175HD': [327990,4], 
         'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21],
        '123FHD': [290890,32], 
        '342FHD': [444990,7],
        'GF75HD': [749990,2], 
        'UWU131HD': [349990,1], 
        'FS1230HD': [249990,0], }


def mostrarmenu():
    print('***MENU***')
    print('1.Stock Marca')
    print('2.Busqueda por precio')
    print('3.Actualizar precio')
    print('4.Salir')


while True:
    mostrarmenu()
    op = leer_opcion()

    if op == 1:
        marca = input('Ingrese marca a consultar: ')
        if not validar_texto(marca):
            print('La categoria no puede estar vacia')
        else:
            stock_marca(marca,stock,productos)
    
    elif op == 2:
        precio_min = None
        precio_max = None
        while precio_min is None or precio_max is None:
            try:
                precio_min = int(input('Ingrese un precio minimo para la busqueda: '))
                precio_max = int(input('Ingrese un precio maximo para la busqueda: '))
            except ValueError:
                print('Debe ingresar valores entero!!!')
                precio_min = None
                precio_max = None
            busqueda_precio(precio_min,precio_max,productos,stock)
    
    elif op == 3:
        repetir = 's'
        while repetir == 's':
            codigo = input('Ingrese el modelo del precio a actualizar: ').upper()
            precionuevo = False
            while not precionuevo:
                precionuevotexto = input(f'Ingrese el nuevo precio de {codigo}:  ')
                if validacion_entero(precionuevotexto):
                    nuevoprecio = int(precionuevotexto)
                    precionuevo = True
                else:
                    print('el precio debe ser un numero entero positivo!!')
            
            if actualizar_precio(codigo,stock,nuevoprecio):
                print(f'El Precio de {codigo} fue actualizado!!!')
            else:
                print('El modelo no existe')
            repetir = input('Desea cambiar el precio de otro notebook? s/n: ').lower()

    elif op == 4:
        print('Programa Finalizado')
        break
