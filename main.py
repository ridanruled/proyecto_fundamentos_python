from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches, users_passwords_list
import re

#Función que imprime el nombre de la organización y su logo.
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


# Función que lleva a cabo el registro del usuario
def login(intentos):
    
    # Verifica que el número de intentos no se haya agotado.
    if(intentos < 1):
        print("Número de intentos de inicio de sesión agotados")
        quit()

    # Imprime logo de la empresa
    encabezado()
    print("Sistema de gestión de ventas de Life Store, inicia sesión para continuar.")
    print(f'Intentos de inicio de sesión restantes: {intentos}')

    # Solicita el usuario y contraseña.
    # Por defecto: 
    # Usuario: Admin
    # 12345

    user_login = input("Usuario: ")
    password_login = input("Contraseña: ")

    #Verifica si existe un usuario y contraseña en la lista de users_passwords_list en lifestore_file.py que sea igual a el usuario y contraseña introducidos por el usuario
    for user_list in users_passwords_list:
        if(user_login == user_list[0] and password_login == user_list[1]):
            return True
    
    print("Usuario o contraseña incorrectos")
    return False

# Función del menú principal.
def menu():
    print("""
    Bienvenida/o, teclea el número de la consulta que deseas hacer y pulsa enter para continuar:
        1. Consultar resumen general por mes de ventas.
        2. Consultar resumen general anual de ventas.
        3. Consultar resumen general de búsquedas.
        4. Salir
    """)

    # Vefica que una de las entradas del usuario sea una opción del menu
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


# Función que convierte la fecha introducida por el usuario en formato MM/YYYY en palabras.
def conversion_numero_letra_fecha(fecha):
    # Variable que se le asignará el mes
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
 
# Función que permite identificar las ventas de cada mes.
def clasificacion_ventas_por_mes(fecha):
    #Divide el texto a partir del caracter /
    month = fecha.split('/')[0]
    year = fecha.split('/')[1]
    ventas_mes = []

    # For que permite recorrer la lista lifestore_sales e identificar las ventas del mes y año indicados.
    for sale in lifestore_sales:
        if(sale[3][3:5] == month and sale[3][-4:] == year):
            ventas_mes.append(sale)
    
    return ventas_mes


# Función que permite identificar los productos con mayores ventas.
def mejores_ventas_mes(ventas_mes):
    product_sales = []
    
    if(len(ventas_mes) == 0):
        return product_sales
    
    # Recorre las listas de lifestore_rpdocuts y ventas_mes para identificar los productos que se encuentran en ventas_mes a partir del id e ir sumando cada vez que aparecen en ventas_mes.
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

# Función que permite obtener la categoría de productos con peores ventas por categoria.
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

    # Identificación de las ventas de cada producto con base en su categoria y con el sort se ordena de menor a mayor por defecto (sin argumento reverse definido).
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

# Función que permite identificar los productos con las peores reseñas cada mes.
def peores_resenas_mes(ventas_mes):
    productos_puntuaciones = []
    
    # Controles de flujo for que permite recorrer la lista de productos y la lista de ventas para identificar el score de cada venta e irla sumando para posteriormente promediarla
    # e incluirla en la lista productos_puntuaciones

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
    # Se ordenan los productos de menor a mayor con base en su score.
    productos_puntuaciones.sort()
    return productos_puntuaciones[:5]

# Función que permite identificar los productos con las mejores reseñas
def mejores_resenas_mes(ventas_mes):
    mejores_puntuaciones = []

    # Controles de flujo for que permite recorrer la lista de productos y la lista de ventas para identificar el score de cada venta e irla sumando para posteriormente promediarla
    # e incluirla en la lista productos_puntuaciones
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
    
    # Ordena de mayor a menor con base en el score.
    mejores_puntuaciones.sort(reverse=True)

    return mejores_puntuaciones[:5]

# Función que permite verificar que la fecha introducida por el usuario sea correcta a partir del uso de expresiones regulares.
def verificacion_formato_fecha(fecha):
    #Verifica que la fecha este en formato apropiado con una expresión regular que verifica el mes y solo el año 2020.
    # por la información disponible.
    check = re.search(r"^([0][1-9][/]2020$)|(^[1][0-2][/]2020$)", fecha)
    if check:
        return True
    else:
        return False

# Función que permite realizar el resumen general de ventas por mes por lo cual imprime el reporte mensual del mes y año indicados de 
# productos más vendidos y mejor valorados y  productos menos vendidos y peor valorados por categoría.
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
        
    encabezado()
    if(len(ventas_del_mes) != 0):
        print(f'Resumen general de ventas del mes de {month} del {year}')
        print('________________________________________________________________________________________________________________________')
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

# Función que permite verifcar que el año es introducido en el formato apropiado YYYY.
def year_verification(year):
    check = re.search(r'^\d{4}$', year)
    if(check):
        return True
    else:
        return False

# Función que permite imprimir el resumen general de ventas e ingresos anuales que incluye el registro de ventas e ingresos de cada mes, el total anual y la identificación de los meses
# con mayores ventas.
def anual():
    # Verifica si el año ingresado es en el formato en números YYYY.
    es_formato_correcto = False
    while(es_formato_correcto is False):
        year = input("""Ingresa el año en el formato YYYY, por ejemplo Año 2020 = 2020: """)
        es_formato_correcto = year_verification(year)

    ventas_enero = []
    ventas_febrero = []
    ventas_marzo = []
    ventas_abril =[]
    ventas_mayo = []
    ventas_junio = []
    ventas_julio = []
    ventas_agosto = []
    ventas_septiembre = []
    ventas_octubre = []
    ventas_noviembre = []
    ventas_diciembre = []

    # Controles de flujo for que agrupan por mes cada una de las ventas por mes.
    for sale in lifestore_sales:
        if(sale[3][3:5] == '01' and sale[3][6:10] == year and sale[-1] != 1):
            for product in lifestore_products:
                if(sale[1] == product[0]):
                    ventas_enero.append([sale[3], product[0], product[2]])


    for sale in lifestore_sales:
        if(sale[3][3:5] == '02' and sale[3][6:10] == year and sale[-1] != 1):
            for product in lifestore_products:
                if(sale[1] == product[0]):
                    ventas_febrero.append([sale[3], product[0], product[2]])

    
    for sale in lifestore_sales:
        if(sale[3][3:5] == '03' and sale[3][6:10] == year and sale[-1] != 1):
            for product in lifestore_products:
                if(sale[1] == product[0]):
                    ventas_marzo.append([sale[3], product[0], product[2]])

    for sale in lifestore_sales:
        if(sale[3][3:5] == '04' and sale[3][6:10] == year and sale[-1] != 1):
            for product in lifestore_products:
                if(sale[1] == product[0]):
                    ventas_abril.append([sale[3], product[0], product[2]])
    
    for sale in lifestore_sales:
        if(sale[3][3:5] == '05' and sale[3][6:10] == year and sale[-1] != 1):
            for product in lifestore_products:
                if(sale[1] == product[0]):
                    ventas_mayo.append([sale[3], product[0], product[2]])

    for sale in lifestore_sales:
        if(sale[3][3:5] == '06' and sale[3][6:10] == year and sale[-1] != 1):
            for product in lifestore_products:
                if(sale[1] == product[0]):
                    ventas_junio.append([sale[3], product[0], product[2]])

    for sale in lifestore_sales:
        if(sale[3][3:5] == '07' and sale[3][6:10] == year and sale[-1] != 1):
            for product in lifestore_products:
                if(sale[1] == product[0]):
                    ventas_julio.append([sale[3], product[0], product[2]])

    for sale in lifestore_sales:
        if(sale[3][3:5] == '08' and sale[3][6:10] == year and sale[-1] != 1):
            for product in lifestore_products:
                if(sale[1] == product[0]):
                    ventas_agosto.append([sale[3], product[0], product[2]])

    for sale in lifestore_sales:
        if(sale[3][3:5] == '09'and sale[3][6:10] == year and sale[-1] != 1):
            for product in lifestore_products:
                if(sale[1] == product[0]):
                    ventas_septiembre.append([sale[3], product[0], product[2]])
    
    for sale in lifestore_sales:
        if(sale[3][3:5] == '10' and sale[3][6:10] == year and sale[-1] != 1):
            for product in lifestore_products:
                if(sale[1] == product[0]):
                    ventas_octubre.append([sale[3], product[0], product[2]])
    
    for sale in lifestore_sales:
        if(sale[3][3:5] == '11'and sale[3][6:10] == year and sale[-1] != 1):
            for product in lifestore_products:
                if(sale[1] == product[0]):
                    ventas_noviembre.append([sale[3], product[0], product[2]])

    for sale in lifestore_sales:
        if(sale[3][3:5] == '12' and sale[3][6:10] == year  and sale[-1] != 1):
            for product in lifestore_products:
                if(sale[1] == product[0]):
                    ventas_diciembre.append([sale[3], product[0], product[2]])

    # Controles de flujo for que permiten sumar los ingresos y ventas de cada mes.
    ingresos_ventas_enero =[]
    suma_ingresos = 0

    for venta in ventas_enero:
        suma_ingresos += venta[2]
    
    ingresos_ventas_enero = ['Enero 2020', len(ventas_enero), suma_ingresos]


    ingresos_ventas_febrero =[]
    suma_ingresos = 0

    for venta in ventas_febrero:
        suma_ingresos += venta[2]
    
    ingresos_ventas_febrero = ['Febrero 2020', len(ventas_febrero), suma_ingresos]

    ingresos_ventas_marzo =[]
    suma_ingresos = 0

    for venta in ventas_marzo:
        suma_ingresos += venta[2]
    
    ingresos_ventas_marzo = ['Marzo 2020', len(ventas_marzo), suma_ingresos] 

    ingresos_ventas_abril =[]
    suma_ingresos = 0

    for venta in ventas_abril:
        suma_ingresos += venta[2]
    
    ingresos_ventas_abril = ['Abril 2020', len(ventas_abril), suma_ingresos]

    ingresos_ventas_mayo =[]
    suma_ingresos = 0

    for venta in ventas_mayo:
        suma_ingresos += venta[2]
    
    ingresos_ventas_mayo = ['Mayo 2020', len(ventas_mayo), suma_ingresos]

    ingresos_ventas_junio =[]
    suma_ingresos = 0


    for venta in ventas_junio:
        suma_ingresos += venta[2]
    
    ingresos_ventas_junio = ['Junio 2020', len(ventas_junio), suma_ingresos]

    ingresos_ventas_julio =[]
    suma_ingresos = 0


    for venta in ventas_julio:
        suma_ingresos += venta[2]
    
    ingresos_ventas_julio = ['Julio 2020', len(ventas_julio), suma_ingresos]

    ingresos_ventas_agosto =[]
    suma_ingresos = 0


    for venta in ventas_agosto:
        suma_ingresos += venta[2]
    
    ingresos_ventas_agosto = ['Agosto 2020', len(ventas_agosto), suma_ingresos]

    ingresos_ventas_septiembre =[]
    suma_ingresos = 0


    for venta in ventas_septiembre:
        suma_ingresos += venta[2]
    
    ingresos_ventas_septiembre = ['Septiembre 2020', len(ventas_septiembre), suma_ingresos]

    ingresos_ventas_octubre =[]
    suma_ingresos = 0

    for venta in ventas_octubre:
        suma_ingresos += venta[2]
    
    ingresos_ventas_octubre = ['Octubre 2020', len(ventas_octubre), suma_ingresos]

    ingresos_ventas_noviembre =[]
    suma_ingresos = 0


    for venta in ventas_noviembre:
        suma_ingresos += venta[2]
    
    ingresos_ventas_noviembre = ['Noviembre 2020', len(ventas_noviembre), suma_ingresos] 

    ingresos_ventas_diciembre =[]
    suma_ingresos = 0

    for venta in ventas_diciembre:
        suma_ingresos += venta[2]

    ingresos_ventas_diciembre = ['Diciembre 2020', len(ventas_diciembre), suma_ingresos]


    ingresos_ventas_por_mes = [ingresos_ventas_enero, ingresos_ventas_febrero, ingresos_ventas_marzo, ingresos_ventas_abril, ingresos_ventas_mayo, ingresos_ventas_junio, ingresos_ventas_julio, ingresos_ventas_agosto, ingresos_ventas_septiembre,ingresos_ventas_octubre, ingresos_ventas_noviembre, ingresos_ventas_diciembre]


    # Generación de reporte de ingresos y ventas anuales
    ingresos_total_anual = 0
    ventas_total_anual = 0
    for l in ingresos_ventas_por_mes:
        ingresos_total_anual += l[2]
        ventas_total_anual += l[1]

    encabezado()
    print("""
    Total de ventas e ingresos por mes
    """)

    for mes in ingresos_ventas_por_mes:
        print(f'Mes/Año: {mes[0]}, Ventas: {mes[1]}, Ingresos: ${mes[2]}')
    print(f'Total de ventas anuales: {ventas_total_anual}, Total de ingresos anuales: ${ingresos_total_anual}')

    ingresos_ventas_por_mes.sort(key = lambda mes: mes[1], reverse = True)

    print("""
    Meses con mejores ventas en el año
    """)

    for i,mes in enumerate(ingresos_ventas_por_mes[:5]):
            print(f'Posición: {i+1}, Mes/Año: {mes[0]}, Ventas: {mes[1]}')

# Función que identifica los productos con más busquedas
def mejores_busquedas_productos():

    # Control de flujo que cuenta la cantidad de ventas de cada producto en la lista de ventas.
    product_search = []
    for product in lifestore_products:
        contador = 0
        for search in lifestore_searches:
            if(product[0] == search[1]):
                contador += 1
        product_search.append([contador, product[0]])
        
    product_search.sort(reverse=True)

    ten_most_searched_products = []
     
    for ps in product_search[:10]:
        for product in lifestore_products:
            if(ps[1] == product[0]):
                # Se agrega al final de la lista como [cantidad, id_producto, nombre_producto]
                ten_most_searched_products.append([ps[0], ps[1], product[1]])
    
    return ten_most_searched_products

# Función que permite indentificar los productos con menos busquedas por categoría.
def menos_busquedas_productos():
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

    # Controles de flujo for que permiten contar el número de búsquedas por producto en cada una de las listas de productos que están clasificados por su categoría.
    busquedas_procesadores = []
    for producto in procesadores:
        contador = 0
        for search in lifestore_searches:
            if(producto[0] == search[1]):
                contador += 1
        busquedas_procesadores.append([contador, producto[0], producto[1]])
    
    busquedas_procesadores.sort()

    busquedas_tarjetas_video = []
    for producto in tarjetas_video:
        contador = 0
        for search in lifestore_searches:
            if(producto[0] == search[1]):
                contador += 1
        busquedas_tarjetas_video.append([contador, producto[0], producto[1]])
    
    busquedas_tarjetas_video.sort()

    busquedas_tarjetas_madre = []
    for producto in tarjetas_madre:
        contador = 0
        for search in lifestore_searches:
            if(producto[0] == search[1]):
                contador += 1
        busquedas_tarjetas_madre.append([contador, producto[0], producto[1]])
    
    busquedas_tarjetas_madre.sort()

    busquedas_discos_duros = []
    for producto in discos_duros:
        contador = 0
        for search in lifestore_searches:
            if(producto[0] == search[1]):
                contador += 1
        busquedas_discos_duros.append([contador, producto[0], producto[1]])
    
    busquedas_discos_duros.sort()

    busquedas_pantallas = []
    for producto in pantallas:
        contador = 0
        for search in lifestore_searches:
            if(producto[0] == search[1]):
                contador += 1
        busquedas_pantallas.append([contador, producto[0], producto[1]])
    
    busquedas_pantallas.sort()

    busquedas_memorias_usb = []
    for producto in memorias_usb:
        contador = 0
        for search in lifestore_searches:
            if(producto[0] == search[1]):
                contador += 1
        busquedas_memorias_usb.append([contador, producto[0], producto[1]])
    
    busquedas_memorias_usb.sort()

    

    busquedas_bocinas = []
    for producto in bocinas:
        contador = 0
        for search in lifestore_searches:
            if(producto[0] == search[1]):
                contador += 1
        busquedas_bocinas.append([contador, producto[0], producto[1]])
    
    busquedas_bocinas.sort()

    busquedas_audifonos = []
    for producto in audifonos:
        contador = 0
        for search in lifestore_searches:
            if(producto[0] == search[1]):
                contador += 1
        busquedas_audifonos.append([contador, producto[0], producto[1]])
    
    busquedas_audifonos.sort()

    busquedas_por_categoria = [busquedas_procesadores, busquedas_tarjetas_video, busquedas_tarjetas_madre, busquedas_discos_duros, busquedas_memorias_usb, busquedas_pantallas, busquedas_bocinas, busquedas_audifonos]

    productos_menos_buscados = []

    for i in busquedas_por_categoria:
        if(len(i) < 5):
            productos_menos_buscados.append(i)
        else:
            productos_menos_buscados.append(i[:10])
    
    print(productos_menos_buscados[5])
    return productos_menos_buscados

# Función que permite llevar a cabo la impresión del resumen general de búsquedas.
def search():
    productos_mas_buscados = mejores_busquedas_productos()

    productos_menos_buscados_categoria = menos_busquedas_productos()

    encabezado()
    print("""Productos con mayor número de búsquedas.""")
    for i, producto in enumerate(productos_mas_buscados):
        print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_búsquedas: {producto[0]}')
    print('_____________________________________________________________________________________')
    print("""Productos con menor número de búsquedas por categoría""")
    print("Procesadores")
    for i, producto in enumerate(productos_menos_buscados_categoria[0]):
        print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_búsquedas: {producto[0]}')
    print("Tarjetas de video")
    for i, producto in enumerate(productos_menos_buscados_categoria[1]):
        print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_búsquedas: {producto[0]}')
    print("Tarjetas madre")
    for i, producto in enumerate(productos_menos_buscados_categoria[2]):
        print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_búsquedas: {producto[0]}')
    print("Discos duros")
    for i, producto in enumerate(productos_menos_buscados_categoria[3]):
        print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_búsquedas: {producto[0]}')
    print("Memorias USB")
    for i, producto in enumerate(productos_menos_buscados_categoria[4]):
        print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_búsquedas: {producto[0]}')
    print("Pantallas")
    for i, producto in enumerate(productos_menos_buscados_categoria[5]):
        print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_búsquedas: {producto[0]}')
    print("Bocinas")
    for i, producto in enumerate(productos_menos_buscados_categoria[6]):
        print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_búsquedas: {producto[0]}')
    print("Audifonos")
    for i, producto in enumerate(productos_menos_buscados_categoria[7]):
        print(f'Posición: {i+1}, id_producto: {producto[1]}, nombre_producto: {producto[2]}, cantidad_búsquedas: {producto[0]}')
    




# Función principal que concentra todas las funciones del programa.
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
        anual()
    elif(opcion_menu == 3):
        search()
    else:
        print("Hasta pronto. 😊")

# Ejecución de la función principal.
principal()