ALFABETO = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

def cesar(caracter, clave):
    posicion =ALFABETO.index(caracter)
    nuevaposicion = posicion + clave
    # if nuevaposicion >= len(ALFABETO):
    #     nuevaposicion -= len(ALFABETO)
    # else:
    #     return ALFABETO[nuevaposicion]
    nuevaposicion = nuevaposicion % len(ALFABETO)
    return ALFABETO[nuevaposicion]

def cifrar(mensaje, clave):
    resultado = ""
    for caracter in mensaje:
        nuevo_caracter = cesar(caracter, clave)
        resultado += nuevo_caracter
        #resultado = resultado + nuevo_caracter
    return resultado

def creaEncriptador(clave):
    def encriptar(mensaje):
        resultado = ""
        for caracter in mensaje:
            nuevo_caracter = cesar(caracter, clave)
            resultado += nuevo_caracter
        return resultado
    return encriptar