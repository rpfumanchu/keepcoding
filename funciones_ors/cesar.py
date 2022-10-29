ALFABETO = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

def cesar(caracter, clave):
    posicion =ALFABETO.index(caracter)
    nuevaposicion = posicion + clave
    return ALFABETO[nuevaposicion]
