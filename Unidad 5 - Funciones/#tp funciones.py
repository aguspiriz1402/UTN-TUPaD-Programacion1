#tp funciones

                 #ejercicio 1
#funcion
def imprimir_hola_mundo():
    print("hola mundo")
#principal    
imprimir_hola_mundo()

                 #ejercicio 2
#funcion
def saludar_usuario(nombre):
    saludo=f"Hola {nombre} bienvenido/a !"
    return saludo

#principal    
nombre=input("ingrese su nombre: ")
mensaje=saludar_usuario(nombre)
print(mensaje)

                 #ejercicio 3  
#funcion
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#principal    
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido:" )
edad=input("Ingrese su edad: ")
residencia=input("Ingrese su lugar de residencia: ")

informacion_personal(nombre,apellido,edad,residencia)
 
                 #ejercicio 4
#funcion
def calcular_area_circulo(radio):
    return 3.14159*(radio*radio)
    

def calcular_perimetro_circulo(radio):
    return 2*3.14159 * radio
  
#principal    
radio:float=float(input("Ingrese el radio de un circulo(cm): "))
area=calcular_area_circulo(round(radio,2))
perimetro=calcular_perimetro_circulo(round(radio,2))

print(f"El area del circulo es de {area} cm2 y el perimetro es de {perimetro} cm.")

                 #ejercicio 5
#funcion
def segundos_a_horas(seg):
    return seg / 60 /60
  

#principal    
segundos:int=int(input("Ingrese la cantidad de segundos, para tranformarlos a horas: "))
horas=segundos_a_horas(segundos)

print(f"{segundos} segundos, equivale a {horas} horas.")

                 #ejercicio 6
#funcion
def tabla_de_multiflicar(num):
    for i in range(1,11):
            print(f"{num} x {i} : {num*i} ")
  
#principal    
numero:int=int(input("Ingrese el numero del que desea ver su tabla de multiplicar: "))

tabla_de_multiflicar(numero)

                 #ejercicio 7
#funcion
def operaciones_basicas(a,b):
    suma=a+b
    resta=a-b
    multi= a*b
    if b != 0:
        divi= a/b
    else:
        print("No se puede dividir por 0")

    return (suma,resta,multi,divi)
  

#principal    
num1:float=float(input("Ingrese primer numero: "))
num2:float=float(input("Ingrese segundo numero: "))

resultado=operaciones_basicas(round(num1,num2),2)

print(f"Suma= {resultado[0]}")
print(f"Resta= {resultado[1]}")
print(f"Multiplicacion= {resultado[2]}")
print(f"Divicion= {resultado[3]}")

                 #ejercicio 8
#funcion
def calcular_imc(peso,altura): #IMC= peso/(altura)2
    IMC= peso/ (altura)**2 
    return round(IMC,2)
  

#principal    
peso:float=float(input("Ingrese su peso (kg): "))
altura:float=float(input("Ingrese su altura (mt): "))
print(f"Su Indice de masa corporal(IMC) es de: {calcular_imc(peso,altura)}")

                 #ejercicio 9
#funcion
def celsius_a_fahrenheit(celsius): #F= (Celsius * 9/5) + 32
    F= (celsius * 9/5)+32
    return round(F,2)#redondea con dos decimales
    

#principal    
celsius:float=float(input("Ingrese temperatura °C : "))
print(f"{celsius} °C equivale a {celsius_a_fahrenheit(celsius)} °F ")

                 #ejercicio 10
#funcion
def calcular_promedio(a,b,c):# P= a+b+c /3(o la cantidad de elementos)
    P= (a+b+c)/3
    return round(P,1)

#principal    
n1:float=float(input("Ingrese primer nota: "))
n2:float=float(input("Ingrese segunda nota: "))
n3:float=float(input("Ingrese tercer nota: "))
print(f"El promedio es: {calcular_promedio(n1,n2,n3)}")