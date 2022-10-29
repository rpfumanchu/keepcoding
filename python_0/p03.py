#quien eres

nombre = input("¿Como te llamas? ")
print(f"Hola, {nombre}")

#toma de datos
edad = int(input("¿Cuantos años tienes? "))
año_actual = int(input("¿En que año estamos?"))
has_cumplido = input("¿Has cumplido años ya (S/N)? ")

#calculo de año
if has_cumplido == "S":
    año_nacimiento = año_actual - edad
else:
    año_nacimiento = año_actual - edad
    
    año_nacimiento = año_nacimiento - 1


#presentación del resultado
print(f"{nombre}, naciste en, {año_nacimiento}")