"""
 Ingresar dos valores en las variables “maximo” y “minimo” y
luego ingresar un valor en la variable “temperatura”. Imprime un
mensaje si el valor de temperatura no está dentro del rango de
marcado por minimo y maximo
"""
import os


maximo = float(input("Ingresa un valor para la varibale maximo: "))
minimo = float(input("Ingresa un valor para la varibale minimo: "))
temperatura = float(input("Ingresa un valor para la varibale temperatura: "))

os.system("cls")

if temperatura <= maximo and temperatura >= minimo:
    print("La temperatura",temperatura," está dentro del rango de marcado por minimo (",minimo,") y maximo (",maximo,")")
else:
    print("No está dentro del rango marcado. Temperatura: ", temperatura, "minimo:", minimo,"maximo:",maximo)
