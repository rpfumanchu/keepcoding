strNumRepeticiones = input("¿Cuantos asteriscos quieres? ")
if strNumRepeticiones.isdigit():
  numRepeticiones = int(strNumRepeticiones)
else:
  numRepeticiones = 5
  print ("Pues imprimo 5")

#Ahora el bucle
for veces in range(1,numRepeticiones): #Aquí cambiar el 1 por otros valores nos permite ver que hace range
  print(veces)