from triangulos import superficieEquilatero, alturaEquilatero

lado = ""
while not lado.isdigit():
    lado = input("Lado: ")

l = int(lado)
print("Triangulo equilatero de lado", l)
print("---")
print("Perímetro:", l * 3)
print("Superficie:", superficieEquilatero(l))
print("Altura:", alturaEquilatero(l))