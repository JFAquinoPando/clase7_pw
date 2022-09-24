"""
Un vendedor recibe un sueldo base más un 10% extra por
comisión de sus ventas, 


el vendedor desea saber cuánto dinero
obtendrá por concepto de comisiones por las tres ventas que
realiza en el mes y 

el total que recibirá en el mes tomando en
cuenta su sueldo base más comisiones.
"""
import os


sueldoBase = int(input("Ingresa tu sueldo base: "))
venta1 = int(input("ingresa el valor de la venta1: "))
venta2 = int(input("ingresa el valor de la venta2: "))
venta3 = int(input("ingresa el valor de la venta3: "))

comision = (venta1 + venta2 + venta3) * (10/100)
os.system("cls")
print("La comision por ventas es de:",comision)
print("Sueldo base más comisiones es de:",comision+sueldoBase)

