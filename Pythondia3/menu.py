print("MENU")
def menu():

  print ("Selecciona una opción")
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
  if opcionMenu==8:
      print:("Pulsa enter")
      return

opciones=int(input("selecciona una opcion"))
while opciones==1:

	  menu()
	  opciones=int(input("¿Quieres hacer otra operacion?"))
