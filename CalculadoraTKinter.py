#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Proyecto final Python
# Calculadora en interfaz gráfica (TKINTER)
# Nombre: Paulo Cesar Ramps Huarachi

# Importación de la librería tkinter
import tkinter as tk
##################
root = tk.Tk()



sw = False

# Definición de las funciones básicas
def sumar():
    a = int(caja_a.get())
    b = int(caja_b.get())
    print(f'La suma de {a} y {b} es: ', a + b)
    mensaje.set(a+b)
    

def restar():
    a = int(caja_a.get())
    b = int(caja_b.get())
    print(f'La Resta de {a} y {b} es: ', a - b)
    mensaje.set(a - b)

def producto():
    a = int(caja_a.get())
    b = int(caja_b.get())
    print(f'El producto de {a} y {b} es: ', a * b)
    mensaje.set(a * b)

def division():
    a = int(caja_a.get())
    b = int(caja_b.get())
    print(f'El cociente de {a} y {b} es: ', a / b)
    mensaje.set(a/b)

# Configuraciones de la pantalle emergente
# Color del fondo
root.geometry('450x250')
root.title('Calculadora básica')
root.configure(bg="#2D8BFA")

#######
mensaje = tk.StringVar()

tk.Label(root, text='Calculadora', bg="#2D8BFA", fg='white', font=('', 20)).place(x=250, y=30)

# Variables de entrada etiquetas
tk.Label(root, text='Ingrese variable a:', bg="#312098", fg='white', font=('', 10)).place(x=20, y=20)
tk.Label(root, text='Ingrese variable b:', bg="#312098", fg='white', font=('', 10)).place(x=20, y=60)

ventana = tk.Tk()
ventana.config(width=400, height=300)
ventana.title("Proyecto Final Programación en Python")

# Entrada de las variables
caja_a = tk.Entry()
caja_a.place(x=140, y=20, width=50, height=25)


caja_b = tk.Entry()
caja_b.place(x=140, y=60, width=50, height=25)

# Botones de Sumar
boton1 = tk.Button(text="Sumar", command=sumar)
boton1.place(x=20, y=100)



# Botones de Restar
boton2 = tk.Button(text="Restar", command=restar)
boton2.place(x=80, y=100)

# Botones de producto
boton3 = tk.Button(text="Multiplicar", command=producto)
boton3.place(x=140, y=100)

# Botones de division
boton4 = tk.Button(text="Dividir", command=division)
boton4.place(x=220, y=100)

# Resultado
tk.Label(root, text='Resultados: ', bg="#2D8BFA", fg='white', font=('', 15)).place(x=100, y=160)
tk.Label(root, textvariable=mensaje, bg="#2D8BFA", fg='white', font=('', 15)).place(x=220, y=160)

# Salir
tk.Button(root, text='Salir', bd=0, command=root.destroy).place(x=220, y=200)

root.mainloop
ventana.mainloop()


def terminar_programa():
    print('Fin del programa')
    global sw
    sw = False


while sw:
    print(menu)
    opcion = int(input('Ingrese la opcion: '))
    if opcion == 1:
        listar_frutas()
    elif opcion == 2:
        agregar_fruta()
    elif opcion == 3:
        buscar_fruta()
    elif opcion is 4:
        eliminar_fruta()
    elif opcion is 5:
        terminar_programa()
    else:
        opcion_no_disponible()
