def suma_es_par(num1, num2):
    suma = num1 + num2
    return suma % 2 == 0
num1=int(input("ingrese un numero: "))
    
num2=int(input("ingrese otro numero: "))
    
resultado = suma_es_par(num1, num2)
print(resultado)


