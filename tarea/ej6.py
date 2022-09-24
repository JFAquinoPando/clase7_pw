frases = []
frase = input('Ingrese una frase: ')
hasta = 2

while frase != '0':
    frases.append(frase)
    frase = input('Ingrese una frase: ')
    
print("La cantidad de frases es: ", len(frases))