#ejercicio1
"""obtener un numero por teclado y verificar si es divisible por 2 y por

#ejercicio2
obtener 3 numero por teclado y verificar cual es el mayor de los 3

obtener un numero por teclado y verificar si es par o impar

#ejercicio3
pepito perez fue a la tienda a comprar un kilo de carne donde su valor es de 25.000 el tendero le comento que si compraba
2 kilos o mas iba a tener el 35% de descuento, obtener el valor a pagar si pepito compro 2.5 kilos de carne

ejercicio4
si Andres fue a comprar 5 huevos a la tienda y en la tienda solo habian 3 huevos entoces Andres le toca a. ir a otra tienda
b. llevar los tres huevos a la casa c. comprar otra cosa determinar las respuesta de la mama para cada punto"""

#ejercicio1
numero = int(input("ingrese el numero"))
if numero != 0 and numero % 2 == 0 and numero % 3 == 0:
    print(f"el numero {numero} es divisble entre 2 y 3")
else:
    print(f"el{numero} no es divisble por 2 y 3")

#ejercicio 2
num1 = int(input("ingresa el numero 1:"))
num2 = int(input("ingresa el numero 2:"))
num3 = int(input("ingresa el numero 3:"))
if num1 >= num2 and num1 >= num3:
    print("el numero ", num1, "es el mayor de los tres")
if num2 >= num1 and num2 >= num3:
    print("el numero ", num2, "es el mayor de los tres")
else:
    print("el numero ", num3, "es el mayor de los tres")

#ejercicio3
numero = int(input("digite el numero"))
if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")

#ejercicio4
valor_carne = 25000 # xkg
cantidad_carne = 2.5 #kg
total_antes = valor_carne * cantidad_carne
total_despues = 0
if (cantidad_carne >= 2):
    total_despues = total_antes - (total_antes * 0.35)
print("el precio total a pagar pepito"
      f"por los 2.5 kg de carne es: ${total_despues}")

#ejercicio5
cantidad_de_huevos = 5
if cantidad_de_huevos <= 3:
    print("a. llevar los tres huevos a la casa ")
    print("b. ir a otra tienda")
    print("c. llevar otra cosa")
    opcion= input("que opcion tomo andres?:").lower()
    if opcion == "a":
        print("y los demas?")
    elif opcion == "b":
        print("por que te demoraste?")
    else:
        print("esto no fue lo que te pedi")

def calcular_imc(peso, altura):
 imc = (peso / altura ** 2)
peso=int(input("ingresa tu peso en kilogramos"))
altura=int(input("ingresa tu altura en metros"))
imc = calcular_imc(peso, altura)
print("tu indice de masa corporal (imc) es:", imc)


num1 = float(imput("introduce el primer numero"))

















