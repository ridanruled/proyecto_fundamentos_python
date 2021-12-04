from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches, users_passwords_list

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
    
def mes():
    encabezado()
    print("""
    Consulta de resumen general por mes.
    Para realizar tu consulta, introduce con el teclado el mes y año de consulta
    en el siguiente formato: MM/YYYY, donde MM es el mes con dos digitos y YYYY es
    el año con cuatro dígitos. Por ejemplo, para consultar el mes de marzo del 2020,
    se introduce lo siguiente: 03/2020.
    """)



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
    
    if(opcion_menu == 1):
        mes()
    elif(opcion_menu == 2):
        # anual()
        pass
    elif(opcion_menu == 3):
        # search()
        pass
    else:
        print("Hasta pronto. 😊")





    

    





principal()