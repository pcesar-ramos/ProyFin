# Calculadora en Consola de python
# Nombre: Paulo Cesar Ramos Huarachi

sw = True



def suma():
    print(f'Suma de {a} y {b} es: ', a+b)

def resta():
    print(f'Resta de {a} y {b} es: ', a-b)

def producto():
    print(f'Producto de {a} y {b} es: ', a*b)

def division():
    print(f'Cociente de {a} y {b} es: ', a/b)

# Terminar el programa

def terminar_programa():
    print('Fin del programa')
    global sw
    sw = False

def opcion_no_disponible():
    print('Opcion no disponible')

# Interfaz del usuario en la consola
operaciones = ''' === Calculadora===
1. Suma
2. Resta
3. Producto
4. División 
5. Salir '''

while sw:
    print(operaciones)
    option = int(input('Ingrese la operación: '))
    a = int(input('Valor de a? '))
    b = int(input('Valor de b? '))
    if option ==1:
        suma()
    elif option ==2:
        resta()
    elif option is 3:
        producto()
    elif option == 4:
        division()
    elif option is 5:
        terminar_programa()
    else:
        opcion_no_disponible()

