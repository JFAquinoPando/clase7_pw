cantidad = 0

def esMultiplo3(n):
    if n % 3 == 0 and n > 0:
        return True
    return False

for i in range(0, 21):
    if esMultiplo3(i):
        print(i)
        cantidad = cantidad + 1

print("Cantidad de multiplos de 3:", cantidad)