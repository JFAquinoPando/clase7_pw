def imprimir(texto,val1, val2, res):
    print(texto, val1,val2, res)


def multiplicacion(n1,n2):
    imprimir("El restulado de multiplicar los primeros 2 valores, sera de:",n1,n2,n1*n2)
    return n1*n2

mult = multiplicacion(5,9)

print("mult es", mult)