lista = [1,2,3]
tupla = (1,2,3)
print(lista)
print(tupla[1], 'de la tupla')
lista.append(5)
lista.pop(1)
lista.pop(1)
print(lista)
lista[0] = 'Texto'
print(lista)

for i in lista:
    if i == 3:
        print("Valor es:",i)

for i in range(6,(20+1)):
    print(i)