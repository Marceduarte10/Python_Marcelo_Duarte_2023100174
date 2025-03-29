'''
Crear un programa que pida dos numero y obtenga como resultado
cual de ellos es par o si ambos lo son
'''
n1=int(input("Ingrese primer numero: "))
n2=int(input("Ingrese segundo numero: "))

if((n1%2==0) and(n2%2==0)):
    print("los numeros ",n1 , "y", n2, " son pares")
elif ((n1%2==0) and (n2%2!=0)):
    print("El numero ",n1, "es par, y el numero ", n2, "es impar")
elif ((n1%2!=0) and (n2%2==0)):
    print("El numero ",n2, "es par, y el numero ", n1, "es impar")
else:
    print("los numeros ",n1 , "y", n2, " son impares")

