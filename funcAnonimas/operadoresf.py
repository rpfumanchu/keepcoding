

from funciones_01bis import voz_alta



frutas = ["platano", "platano", "fresa", "naranja", "uva", "uva", "fresa", "platano", ""]

lfConAsteriscos = list(map(lambda p: "*" + p + "*", frutas))
lMayusculas = list(map(voz_alta, frutas))

print(lfConAsteriscos)
print(lMayusculas)


# este bloque de aqui seria equivalente a lMayusculas = list(map(voz_alta, frutas))

# lMayuscukasIterando = []
# for fruta in frutas:
#     frutasMyu = voz_alta(fruta)
#     lMayuscukasIterando.append(frutasMyu)
# print(lMayuscukasIterando)

# si en frutas metemos "" nos va a dar error porque posicion[2] no puede hacerlo al no tener,si le decimos len(p) > 2 and 
# al ser la primera F ya no pasa porque con and o son los do T o los dos F
lp3aLetraA = list(filter(lambda p: len(p) > 2 and p [2] == "a", frutas))



#otra forma

def es3A(p):
    return len(p) > 2 and p [2] == "a"
lp3LetraF = list(filter(es3A, frutas))

# haciendolo con un if
def es3a(p):
    if len(p) > 2 and p [2] == "a":
        return True
    return 
lp3 = list(filter(es3a, frutas))

#asi seria hacer un filter sin usar filter
l3aIterando = []
for fruta in frutas:
    fru3a = es3A(fruta)
    if fru3a is True:
        l3aIterando.append(fruta) 
  
print(l3aIterando)
print(lp3aLetraA)
print(lp3LetraF)
print(lp3)