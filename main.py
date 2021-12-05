from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches, users_passwords_list
import re

def encabezado():
    # Encabezado

    # Imprime el nombre de la organización y su logo.
    encabezado = """
    ||    |||||||| ||||||| ||||||||   ||||||| |||||||| ||||||| ||||||| |||||||   __
    ||       ||    ||      ||         ||         ||    ||   || ||   || ||          \_________
    ||       ||    |||||   |||||      |||||||    ||    ||   || ||||||| |||||        \       /
    ||       ||    ||      ||              ||    ||    ||   || || ||   ||            \_____/
    ||||| |||||||| ||      |||||||    |||||||    ||    ||||||| ||   || |||||||        °   °
    """
    print(encabezado)

def login(intentos):
    
    # Verifica que el número de intentos no se haya agotado.
    if(intentos < 1):
        print("Número de intentos de inicio de sesión agotados")
        quit()

    encabezado()
    print("Sistema de gestión de ventas de Life Store, inicia sesión para continuar.")
    print(f'Intentos de inicio de sesión restantes: {intentos}')

    # Solicita el usuario y contraseña.
    # Por defecto: 
    # Usuario: Admin
    # 12345

    user_login = input("Usuario: ")
    password_login = input("Contraseña: ")

    for user_list in users_passwords_list:
        if(user_login == user_list[0] and password_login == user_list[1]):
            return True
    
    print("Usuario o contraseña incorrectos")
    return False

def menu():
    print("""
    Bienvenida/o, teclea el número de la consulta que deseas hacer y pulsa enter para continuar:
        1. Consultar resumen general por mes de ventas.
        2. Consultar resumen general anual de ventas.
        3. Consultar resumen general de búsquedas.
        4. Salir
    """)

    try:
        entrada_menu = int(input("Selecciona un número: "))
        if(entrada_menu == 4):
            print("Hasta pronto. 😊")
        elif(entrada_menu > 0 and entrada_menu <5):  
            return entrada_menu
        else:
            print("Entrada no válida, hasta pronto. 😊")
    except:
        print("Entrada no válida, hasta pronto. 😊")

def verificacion_formato_fecha(fecha):
    #Verifica que la fecha este en formato apropiado con una expresión regular que verifica el mes y solo el año 2020.
    # por la información disponible.
    check = re.search(r"^([0][1-9][/]2020$)|(^[1][0-2][/]2020$)", fecha)
    if check:
        return True
    else:
        return False

def conversion_numero_letra_fecha(fecha):
    month = 'Mes'
    # Verifica las dos primeras posiciones del string que son los digitos del mes y asigna el mes de acuerdo a los valores.
    if(fecha[:2] == '01'):
        month = 'enero'
    elif(fecha[:2] == '02'):
        month = 'febrero'
    elif(fecha[:2] == '03'):
        month = 'marzo'
    elif(fecha[:2] == '04'):
        month = 'abril'
    elif(fecha[:2] == '05'):
        month = 'mayo'
    elif(fecha[:2] == '06'):
        month = 'junio'
    elif(fecha[:2] == '07'):
        month = 'julio'
    elif(fecha[:2] == '08'):
        month = 'agosto'
    elif(fecha[:2] == '09'):
        month = 'septiembre'
    elif(fecha[:2] == '10'):
        month = 'octubre'
    elif(fecha[:2] == '11'):
        month = 'noviembre'
    elif(fecha[:2] == '12'):
        month = 'diciembre'

    # Divide el string en elementos de una lista a partir del caracter "/".
    year = fecha.split('/')

    # Regresa el mes en letra y el año.
    return month,year[1]
 
def clasificacion_ventas_por_mes(fecha):
    month = fecha.split('/')[0]
    year = fecha.split('/')[1]
    ventas_mes = []

    for sale in lifestore_sales:
        if(sale[3][3:5] == month and sale[3][-4:] == year):
            ventas_mes.append(sale)
    
    return ventas_mes


def mejores_ventas_mes(ventas_mes):
    product_sales = []
    
    if(len(ventas_mes) == 0):
        return product_sales
    
    for product in lifestore_products:
        contador = 0
        for sale in ventas_mes:
            if(product[0] == sale[1] and sale[4] == 0):
                contador += 1
        if(contador != 0):
            product_sales.append([contador, product[0], product[1]])

    product_sales.sort(reverse=True)

    if len(product_sales) >= 5:
        return product_sales[:5]
    else:
        return product_sales 

def peores_ventas_mes(ventas_mes):
    if(len(ventas_mes) == 0):
        return []

    # Listas donde se agruparan las ventas de los productos de acuerdo con su categoría.
    procesadores = []
    tarjetas_video = []
    tarjetas_madre = []
    discos_duros = []
    pantallas = []
    memorias_usb = []
    bocinas = []
    audifonos = []

    # Clasificación de los productos por su categoria
    for product in lifestore_products:
        if(product[3] == 'procesadores'):
            procesadores.append(product)

    for product in lifestore_products:
        if(product[3] == 'tarjetas de video'):
            tarjetas_video.append(product)
    
    for product in lifestore_products:
        if(product[3] == 'tarjetas madre'):
            tarjetas_madre.append(product)
    
    for product in lifestore_products:
        if(product[3] == 'discos duros'):
            discos_duros.append(product)
    
    for product in lifestore_products:
        if(product[3] == 'memorias usb'):
            memorias_usb.append(product)

    for product in lifestore_products:
        if(product[3] == 'pantallas'):
            pantallas.append(product)
    
    for product in lifestore_products:
        if(product[3] == 'bocinas'):
            bocinas.append(product)
    
    for product in lifestore_products:
        if(product[3] == 'audifonos'):
            audifonos.append(product)

    ventas_procesadores = []
    for producto in procesadores:
        contador = 0
        for venta in ventas_mes:
            if(producto[0] == venta[1] and venta[4] == 0):
                contador += 1
        ventas_procesadores.append([contador, producto[0], producto[1], producto[3]])
    
    ventas_procesadores.sort()

    ventas_tarjetas_video = []
    for producto in tarjetas_video:
        contador = 0
        for venta in ventas_mes:
            if(producto[0] == venta[1] and venta[4] == 0):
                contador += 1
        ventas_tarjetas_video.append([contador, producto[0], producto[1], producto[3]])
    
    ventas_tarjetas_video.sort()

    ventas_tarjetas_madre = []
    for producto in tarjetas_madre:
        contador = 0
        for venta in ventas_mes:
            if(producto[0] == venta[1] and venta[4] == 0):
                contador += 1
        ventas_tarjetas_madre.append([contador, producto[0], producto[1], producto[3]])
    
    ventas_tarjetas_madre.sort()

    ventas_discos_duros = []
    for producto in discos_duros:
        contador = 0
        for venta in ventas_mes:
            if(producto[0] == venta[1] and venta[4] == 0):
                contador += 1
        ventas_discos_duros.append([contador, producto[0], producto[1], producto[3]])
    
    ventas_discos_duros.sort()

    ventas_memorias_usb = []
    for producto in memorias_usb:
        contador = 0
        for venta in ventas_mes:
            if(producto[0] == venta[1] and venta[4] == 0):
                contador += 1
        ventas_memorias_usb.append([contador, producto[0], producto[1], producto[3]])
    
    ventas_memorias_usb.sort()

    ventas_pantallas = []
    for producto in pantallas:
        contador = 0
        for venta in ventas_mes:
            if(producto[0] == venta[1] and venta[4] == 0):
                contador += 1
        ventas_pantallas.append([contador, producto[0], producto[1], producto[3]])
    
    ventas_pantallas.sort()

    ventas_bocinas = []
    for producto in bocinas:
        contador = 0
        for venta in ventas_mes:
            if(producto[0] == venta[1] and venta[4] == 0):
                contador += 1
        ventas_bocinas.append([contador, producto[0], producto[1], producto[3]])
    
    ventas_bocinas.sort()

    ventas_audifonos = []
    for producto in audifonos:
        contador = 0
        for venta in ventas_mes:
            if(producto[0] == venta[1] and venta[4] == 0):
                contador += 1
        ventas_audifonos.append([contador, producto[0], producto[1], producto[3]])
    
    ventas_audifonos.sort()

    lista_menos_vendidos_categorias = [ventas_procesadores[:5], ventas_tarjetas_video[:5], ventas_tarjetas_madre[:5], ventas_discos_duros[:5], ventas_memorias_usb[:5], ventas_pantallas[:5], ventas_bocinas[:5], ventas_audifonos[:5]]

    return lista_menos_vendidos_categorias


def peores_resenas_mes(ventas_mes):
    productos_puntuaciones = []

    for product in lifestore_products:
        contador = 0
        suma_score = 0
        promedio_score = 0
        for sale in ventas_mes:
            if(product[0] == sale[1]):
                contador += 1
                suma_score += sale[2]
        if(contador != 0):
            promedio_score = suma_score / contador
            productos_puntuaciones.append([round(promedio_score, 3), product[0], product[1]])

        #Asignación de valor de 1000 a productos que no tienen reseña para identificar los peores valorados.
        else:
            promedio_score = 1000
            productos_puntuaciones.append([promedio_score, product[0], product[1]])
    
    productos_puntuaciones.sort()
    return productos_puntuaciones[:5]

def mejores_resenas_mes(ventas_mes):
    mejores_puntuaciones = []

    for product in lifestore_products:
        contador = 0
        suma_score = 0
        promedio_score = 0
        for sale in ventas_mes:
            if(product[0] == sale[1]):
                contador += 1
                suma_score += sale[2]
        if(contador != 0):
            promedio_score = suma_score / contador
            mejores_puntuaciones.append([round(promedio_score, 3), product[0], product[1]])

        #Asignación de valor de -1 a productos sin reseña para identificar los mejores valorados.
        else:
            promedio_score = -1
            mejores_puntuaciones.append([promedio_score, product[0], product[1]])
    
    mejores_puntuaciones.sort(reverse=True)

    return mejores_puntuaciones[:5]

def mensual():
    x = False
    while(x is False):
        encabezado()
        print("""
        Consulta de resumen general por mes.

        Para realizar tu consulta, introduce con el teclado el mes y año de consulta
        en el siguiente formato: MM/YYYY, donde MM es el mes con dos digitos y YYYY es
        el año con cuatro dígitos. Por ejemplo, para consultar el mes de marzo del 2020,
        se introduce lo siguiente: 03/2020. 
        Información disponible solo de enero 2020 a diciembre 2020.

        """)
        fecha_consulta = input('Introduce la fecha en el formato indicado: ')
        es_formato_correcto = verificacion_formato_fecha(fecha_consulta)
        if(es_formato_correcto is True):
            x= True
        else:
            print("Formato de fecha incorrecto, por favor sigue las instrucciones.")
        
    ventas_del_mes = clasificacion_ventas_por_mes(fecha_consulta)

    productos_mas_ventas_mes = mejores_ventas_mes(ventas_del_mes)

    productos_categoria_menos_ventas_mes = peores_ventas_mes(ventas_del_mes)
    
    productos_categorias_mejores_resenas = mejores_resenas_mes(ventas_del_mes)

    productos_categorias_peores_resenas = peores_resenas_mes(ventas_del_mes)



    month, year  = conversion_numero_letra_fecha(fecha_consulta)
        
    print(f'Resumen general de ventas del mes de {month} del {year}')
    print('________________________________________________________________________________________________________________________')
    if(ventas_del_mes != 0):
        print(f'Productos más vendidos en {month} del {year}')
        for i,producto in enumerate(productos_mas_ventas_mes):
            print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_vendida: {producto[0]}.')
        print('________________________________________________________________________________________________________________________')
        print(f'Productos menos vendidos por categoria en {month} del {year}')
        print("Procesadores")
        for i,producto in enumerate(productos_categoria_menos_ventas_mes[0]):
            print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_vendida: {producto[0]}.')
        print("Tarjetas de video")
        for i,producto in enumerate(productos_categoria_menos_ventas_mes[1]):
            print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_vendida: {producto[0]}.')
        print("Tarjetas madre")
        for i,producto in enumerate(productos_categoria_menos_ventas_mes[2]):
            print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_vendida: {producto[0]}.')
        print("Discos duros")
        for i,producto in enumerate(productos_categoria_menos_ventas_mes[3]):
            print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_vendida: {producto[0]}.')
        print("Memorias USB")
        for i,producto in enumerate(productos_categoria_menos_ventas_mes[4]):
            print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_vendida: {producto[0]}.')
        print("Pantallas")
        for i,producto in enumerate(productos_categoria_menos_ventas_mes[5]):
            print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_vendida: {producto[0]}.')
        print("Bocinas")
        for i,producto in enumerate(productos_categoria_menos_ventas_mes[6]):
            print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_vendida: {producto[0]}.')
        print("Audifonos")
        for i,producto in enumerate(productos_categoria_menos_ventas_mes[7]):
            print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_vendida: {producto[0]}.')
        print('________________________________________________________________________________________________________________________')
        print(f'Productos con mejores reseñas en {month} del {year}')
        for i,producto in enumerate(productos_categorias_mejores_resenas):
            print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, Puntuación: {producto[0]}.')
        print('________________________________________________________________________________________________________________________')
        print(f'Productos con peores reseñas en {month} del {year}')
        for i,producto in enumerate(productos_categorias_peores_resenas):
            print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, Puntuación: {producto[0]}.')
    else:
        print("Sin ventas registradas en este mes")



def principal():
    # Variable de control del while
    x = False

    # Varible de conteo de intentos de inicio de sesión
    intentos = 4 

    #Control de flujo while para el inicio de sesión, se termina hasta que se ingresa usuario y contraseña correctos.
    while(x is False):
        intentos -= 1
        x = login(intentos)

    #Al introducir usuario y contraseñas correctos, imprime menú principal.
    encabezado()
    opcion_menu = menu()
    
    # Condicional if para iniciar el tipo de consulta de acuerdo al número introducido.
    if(opcion_menu == 1):
        # Ejecuta la función mes.
        mensual()
    elif(opcion_menu == 2):
        # anual()
        pass
    elif(opcion_menu == 3):
        # search()
        pass
    else:
        print("Hasta pronto. 😊")

principal()