"""
Existen tres tipos de jubilaciones, 
por edad, 
por antigüedad joven y 
por antigüedad adulta. 

Las personas para la jubilación por edad deben tener 60 años o más y una antigüedad en su empleo de menos de 25 años.
Las personas para la jubilación por antigüedad joven deben tener menos de 60 años y una antigüedad en su empleo de 25 años o más.
Las personas para antigüedad adulta deben tener 60 años o más
y una antigüedad en su empleo de 25 años o más.
"""
import os



edad = int(input("Ingresa tu edad(en años) : "))
antiguedad = int(input("Ingresa tu antiguedad(en años) : "))
os.system("cls")
if edad >= 60 and antiguedad < 25:
    print("jubilación por edad")
elif edad < 60 and antiguedad >= 25:
    print("jubilación por antigüedad joven")
elif edad >= 60 and antiguedad >= 25: 
    print("jubilacion por antigüedad adulta")
else:
    print("no te puedes jubilar aún! ;( 😀")
os.system("mkdir resultados")
os.system("cd resultados")
os.system("touch archivo.txt")
res = str(edad) +" >> archivo.txt"
os.system(res)