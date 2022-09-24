cantidad = 0
for i in range(0,21):
    if i % 3 == 0 and i > 0:
        print(i)
        cantidad = cantidad + 1
print("Cantidad de multiplos de 3:", cantidad)