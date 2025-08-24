# UTN-TUPaD-Programacion1
Subo practica unidad 1

#TPN 1
#ejercicio 1

print("hola mundo!")

#ejercicio 2

nombre = input("Ingrese su nombre ")
print("Hola",nombre,"!") 

#ejercicio 3

nombre=input("ingrese su nombre:")
apellido=input("ingrese su apellido:")
edad=input("ingrese su edad:")
edad=int(edad)
residencia=input("ingrese su lugar de residencia:")
print(f"Soy",nombre,apellido,"tengo",edad,"años y vivo en",residencia)

#ejercicio 4

radio: float=float(input("ingrese el valor del radio: "))
PI: float=3.14
area: float=PI*radio**2
perimetro: float=2*PI*radio
print(f"Area: ",area,", Perimetro:",perimetro)

#ejercicio 5

segundos: float=float(input("Ingrese una cantidad de segundos:"))
horas=segundos/3600
print(segundos, "equivale a :",horas,"horas")

#ejercicio 6

num: int=int(input("Ingrese el numero del que desee ver su tabla "))
print(num,"x 1=",num*1)
print(num,"x 2=",num*2)
print(num,"x 3=",num*3)
print(num,"x 4=",num*4)
print(num,"x 5=",num*5)
print(num,"x 6=",num*6)
print(num,"x 7=",num*7)
print(num,"x 8=",num*8)
print(num,"x 9=",num*9)
print(num,"x 10=",num*10)

#ejercicio 7

num_1: int=int(input("ingrese el primer numero entero: "))
num_2: int=int(input("ingrese el segundo numero entero: "))
print(num_1,"+",num_2,"=",num_1+num_2)
print(num_1,"-",num_2,"=",num_1-num_2)
print(num_1,"/",num_2,"=",num_1/num_2)
print(num_1,"x",num_2,"=",num_1*num_2)

#ejercicio 8

altura: float=float(input("ingrese su altura en metros: "))
peso: float=float(input("ingrese su peso en kg: "))
imc= peso/altura**2
print("su indice de masa corporal es:", imc)

#ejercicio 9

celsius: float=float(input("ingrese temperatura en °C : "))
fahrenheit= (celsius*(9/5))+32
print(celsius,"°C equivale a ",fahrenheit,"Fahrenheit")

#ejercicio 10

num_1: float=float(input("ingrese primer numero "))
num_2: float=float(input("ingrese segundo numero "))
num_3: float=float(input("ingrese tercer numero "))
promedio= (num_1+num_2+num_3)/3
print("el promedio de los numeros ingresados es:",promedio)
