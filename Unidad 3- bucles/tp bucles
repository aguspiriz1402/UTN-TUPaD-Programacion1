#ejercicio 1

for i in range(1,101):
    print(i)

#ejercicio 2

numero= input("Ingrese un numero entero ")

if numero[0]=="-":
    numero= numero[1:] # va a tomar al digito en si posicion 1 , ya q en la 0 estaria el "-"

contador=0
i=0
while i<len(numero):
    contador+=1
    i+=1

print(f"el numero tiene", contador,"digitos")

#ejercicio 3

valor_1: int=int(input("ingrese el primer valor "))
valor_2: int=int(input("ingrese el segundo valor "))

if valor_1<valor_2:
    suma=0
    for i in range(valor_1+1,valor_2):
        suma+=i
print (f"la suma de los numeros entre {valor_1} y {valor_2} es: {suma}")

#ejercicio 4

suma=0
while True:
    num: int=int(input("ingrese un num entero o (0) para terminar: "))
    if num==0:
        break
    suma+=num

print(f"la suma de los numeros es ",suma)

#ejercicio 5

import random
aleatorio=random.randint(0,9)

intentos=0
bandera= False
print("adivina el numero entre 0 y 9! ")

while not bandera:
    num= int(input("ingrese su numero: "))
    intentos +=1

    if num==aleatorio:
        bandera= True

print(f"Adivinaste!! el numero secreto era : ",aleatorio)
print(f"Lo intentaste ",intentos," veces ")

#ejercicio 6 

print("numeros pares entre 0 y 100 en orden decreciente")

for i in range(100,-1,-2):
    print(i)

#ejercicio 7

numero= int(input("Ingrese un numero positivo: "))

if numero>=0:
    suma=0
    for i in range(0,numero+1):
        suma+=i

print(f"la suma de los numeros entre ",0," y ",numero," es : ",suma)

#ejercicio 8

numero:int=int(input("Ingrese un numero positivo: "))

if numero >= 0:
    suma=0
    for i in range(0,numero+1):
        suma+=i

print(f"la suma de los numeros entre ",0," y ",numero," es : ", suma )

#ejercicio 9

cant=100
pares=0
impares=0
positivos=0
negativos=0

for i in range(cant):
    num= int(input(f"ingrese el numero {i+1}: "))

    if num%2==0 : #para saber si es par
        pares+=1
    else:
        impares+=1
    if num>0:
        positivos+=1
    else:
        negativos+=1

print("RESULTADOS")
print("Cantidad de pares: ",pares)
print("Cantidad de impares: ",impares) 
print("Cantidad de positivos: ",positivos)    
print("Cantidad de negativos: ",negativos)

#ejercicio 10

num= input("Ingrese un numero entero: ")
invertido=""

if num[0]=="-":
    for i in range(len(num)-1,0,-1): #recorremos desde el ultimo hasta el indice 1 sin incluir el-
        invertido+=num[i]
    invertido="-"+ invertido #se agrega el signo una sola ves
else:
    for i in range(len(num)-1,-1,-1): #recorre todo en orden inverso
        invertido+=num[i]

print("Numero invertido: ",invertido)
