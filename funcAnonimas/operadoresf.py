
from funciones1.funciones_01bis import voz_alta

frutas = ["platano", "platano", "fresa", "naranja", "uva", "uva", "fresa", "platano"]

lfConAsteriscos = list(map(lambda p: "*" + p + "*", frutas))
lMayusculas = list(map(voz_alta, frutas))

print(lfConAsteriscos)
print(lMayusculas)