#Estructuras condicionales TP3

#ejercicio 1

edad= int(input("Ingrese su edad: "))

if edad>= 18:
    print("Es mayor de edad!")
else :
    print("No es mayor de edad")

#ejercicio 2

nota= float(input("Ingrese su nota: "))

if nota>=6 :
    print("Aprobado!")
else:
    print("Desaprobado")

#ejercicio 3

par= int(input("Ingrese un numero par "))

if par%2==0 :
    print(f"El numero {par} es par!")
else:
    print("Porfavor ingrese un numero par")

#ejercicio 4

edad= int(input("Ingrese su edad: "))

if edad<12 :
    print("Su categoria es: Niño/a")
elif edad>=12 and edad<18 :
    print("Su categoria es: Adolecente")
elif edad>=18 and edad<30 :
    print("Su categoria es: Adulto/a Joven")
elif edad>=30 :
    print("Su categoria es: Adulto/a")
else:
    print("Numero incorrecto")

#ejercicio 5

contra= input("Ingrese una contraseña entre 8 y 14 caracteres: ")          
long= len(contra)

if long>=8 and long<=14:
    print("A ingresado una contraseña correcta")
else :
    print("Porfavor ingrese una contraseña entre 8 y 14 caracteres: ")

#ejercicio 6

import random 
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

print("Numeros aleatorios: ",numeros_aleatorios)

media= mean(numeros_aleatorios)
mediana= median(numeros_aleatorios)
moda= mode(numeros_aleatorios)

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media>mediana and mediana>moda:
    print("La distribucion tiene sesgo positivo (hacia la derecha)")
elif media<mediana and mediana<moda:
    print("La distribucion tiene sesgo negativo (hacia la izquierda)")
else :
    print("La distribucion no tiene sesgo (simetrica)")


#ejercicio 7


palabra= input("Escriba una palabra: ")
ultima= len(palabra) 


if   (palabra[ultima-1]) == "a":
    print(palabra," !!")
elif (palabra[ultima-1]) == "e":
    print(palabra," !!")
elif (palabra[ultima-1]) == "i":
    print(palabra," !!")
elif (palabra[ultima-1]) == "o":
    print(palabra," !!")
elif (palabra[ultima-1]) == "u":
    print(palabra," !!")            
else :
    print(palabra)


#ejercicio 8

nombre= input("ingrese su nombre: ")
numero= input("ingrese un numero: 1)para su nombre en mayscula, 2) su nombre en minuscula, 3) Con la primera letra en mayus: ")

if numero == "1":
    print(nombre.upper())
elif numero =="2":
    print(nombre.lower())    
elif numero== "3":
    print(nombre.capitalize())    
else:
    print("A ingresado un numero incorrecto") 

#ejercicio 9

mag= float=float(input("Ingrese magnitud del terremoto "))
if mag<3 :
    print("muy leve")
elif mag>=3 and mag<4 :
    print("levemente perceptible")
elif mag>=4 and mag<5 :
    print("moderado")
elif mag>=5 and mag<6 :
    print("puede causar daños en estructuras debiles")
elif mag>=6 and mag<7:
    print("muy fuerte")
elif mag>=7 and mag <=10 :
     print("extremo")
else :
    print("numero no valido")

#ejercicio 10

hemisferio= input("Ingrese en que hemisferio se encuentra(n/s): ")
mes= int(input("Ingrese el numero del mes (1-12): "))
dia= int(input("Ingrese dia (1-30/31): "))

if hemisferio=="n" :
    if (mes==12 and dia>=21) or(mes in[1,2]) or (mes==3 and dia<=20):
        print("invierno")
    elif (mes==3 and dia>=21) or (mes in[4,5]) or(mes==6 and dia<=20):
        print("primavera")
    elif (mes==6 and dia>=21) or (mes in[7,8]) or(mes==9 and dia<=20):
        print("verano")   
    elif (mes==9 and dia>=21) or (mes in[10,11]) or(mes==12 and dia<=20):
        print("otoño")    


elif hemisferio=="s" :
    if (mes==12 and dia>=21) or(mes in[1,2]) or (mes==3 and dia<=20):
        print("verano")
    elif (mes==3 and dia>=21) or (mes in[4,5]) or(mes==6 and dia<=20):
        print("otoño")
    elif (mes==6 and dia>=21) or (mes in[7,8]) or(mes==9 and dia<=20):
        print("invierno")   
    elif (mes==9 and dia>=21) or (mes in[10,11]) or(mes==12 and dia<=20):
        print("primavera")    

else:
    print("hemisferio no valido")