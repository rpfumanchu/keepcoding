

def voz_alta(texto):
    return texto.upper() + " !!!"

#chr(129323) codigo emoticono
def voz_baja(texto):
    return chr(129323) + texto.lower()

gritando = voz_alta
susurrando = voz_baja


# print(gritando ("Hola"))
# print(susurrando ("Adios"))

# def saludar(saludo):
#     print("*" * len(saludo))
#     print(saludo)
#     print("." * len(saludo))

# def saludar(saludo, modo):
#     print("*" * len(saludo))
#     print(modo (saludo))
#     print("." * len(saludo))

def saludar(saludo, modo):
    saludo_formateado = modo(saludo)
    linea = len(saludo_formateado)

    if modo == voz_baja:
        linea +=1

    print("*" * linea)
    print(saludo_formateado)
    print("." * linea)
    

    # print("*" * len(saludo_formateado +" "))
    # print(saludo_formateado)
    # print("." * len(saludo_formateado +" "))