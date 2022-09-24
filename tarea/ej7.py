"""
Hacer un programa que imprima y cuente los
múltiplos de 3 que hay entre el 0 y el 20.
"""

def esMultiploDe3(numero):
    if numero % 3 == 0 and numero > 0:
        return True
    return False

def recorrerNumeros():
    multiplos = []
    for i in range(0, 21):
        if esMultiploDe3(i):
            multiplos.append(i)
    imprimirResultados(multiplos)

def imprimirResultados(mult):
    print("Los multiplos de 3 son:", mult)
    print("Los multiplos de 3 son (cantidad) son:", len(mult))

recorrerNumeros()