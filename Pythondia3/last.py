print("¿Que desea hacer?")

print ("Sumar dos cantidades:1")
print ("Restar dos cantidades:2")
print ("Multiplicar dos cantidades:3")
print ("Dividir:4")
print ("Comprar dos cantidades:5")
print ("Calcular IVA :6")
print ("Multiplicacion:7")
print ("Salir:8")

opcionMenu = int(input("Inserta un numero valor :  "))

if opcionMenu==1:
    print ("Suma")
   #input("Has pulsado la opción 1...\npulsa una tecla para continuar")
    var1=int(input("Dame a"))
    var2=int(input("Dame b"))
    resultado=var1+var2
    print(resultado)
if opcionMenu==2:
    print ("Resta")
    #input("Has pulsado la opción 2...\npulsa una tecla para continuar")
    var1=int(input("Dame a"))
    var2=int(input("Dame b"))
    resultado=var1-var2
    print(resultado)
if opcionMenu==3:
    print ("Producto")
    #input("Has pulsado la opción 3...\npulsa una tecla para continuar")

if opcionMenu==4:
    print ("Division")
    #input("Has pulsado la opción 4...\npulsa una tecla para continuar")
if opcionMenu==5:
    print ("Comparacion de numeros")
    #input("Has pulsado la opción 5...\npulsa una tecla para continuar")
if opcionMenu==6:
    print ("Calcular IVA")
    #input("Has pulsado la opción 6...\npulsa una tecla para continuar")
    print("Calculo del IVA de una cantidad")
    print("1.Digita el IVA")
    print("2.Digita la cantidad")
    IVA=float(input("Dame el valor del IVA:"))
    cantidad= float( input("Dame la cantidad:$"))
    resultado=IVA*cantidad
    print("El IVA es:",resultado)
    input("presiona para continuar....")
if opcionMenu==7:
    print ("Multiplicion")
    a = int(input("¿Que tabla quieres?: "))
    var=int(input("Ingresa numero"))
    for var in range(1,var+1):
     print(var,"x",a,"=",var*a)

    #input("Has pulsado la opción 7...\npulsa una tecla para continuar")

input(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
