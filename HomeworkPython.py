#!/usr/bin/env python
# coding: utf-8

# # Tarea Python
# Nombre: Cesar Ramos
# 02 de mayo 2020

# In[109]:


class Presupuesto:
    tipo_gasto = ""
    tipo_ingreso = ""
    ingreso = 0
    gasto = 0
    #saldo = 0
    
    def __init__(self, tipo_gasto,  gasto, tipo_ingreso, ingreso):
        self.tipo_gasto = tipo_gasto
        self.gasto = gasto
        self.tipo_ingreso = tipo_ingreso
        self.ingreso = ingreso
    
    def __str__(self):
        return "Tipo de gasto: {} \nGasto: {} Bs. \n"                "Tipo de ingreso: {} \nIngreso: {} Bs. \n"                "".format(self.tipo_gasto, self.gasto, self.tipo_ingreso, self.ingreso)
    
    def saldo(self):
        saldo_presupuestario = self.ingreso - self.gasto
        return saldo_presupuestario
        
    def donacion(self):
        saldo = self.ingreso - self.gasto
        if saldo < 0:
            #return saldo
            print("Deuda", saldo)
        else:
            #return self.saldo
            print("Superávit", saldo)
            
    
pres = Presupuesto("Sueldos y salarios", 2000, "Impuestos", 2100)
print(pres)
print("Saldo presupuestario:",int(pres.saldo()), "Bs.")
print(pres.donacion())


# In[ ]:


#Definición de la Clase:
class Biblioteca:

    def __init__(self, area, editorial, year, edition):
        self.area = area
        self.editorial = editorial
        self.year = year
        self.edition = edition

    def __str__(self):
        return "Title : {} \n Editorial : {} \nYear : {} \n Edition: {}".format(self.area, self.editorial, self.year, self.edition)
        

    def nueva_edicion(self):
        edition = self.edition + 1
        return edition
    
    def año_actualizado(self):
        newyear = self.year + 3
        return newyear
        
Sel_lib = Biblioteca("Python Pandas", "Springer", 2017, 2)
print("===== Biblioteca =====")
print(Sel_lib)
print("Updated edition:", Sel_lib.nueva_edicion())
print("New publication:", Sel_lib.año_actualizado())
print("======= ====== =======")

