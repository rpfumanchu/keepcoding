def voz_alta(texto):
    return texto.upper() + " !!!"

#chr(129323) codigo emoticono
def voz_baja(texto):
    return chr(129323) + texto.lower()

gritando = voz_alta
susurrando = voz_baja

# print(gritando ("Hola"))
# print(susurrando ("Adios"))

dialogo =[
    ("Hola ", gritando),
    ("Por favor, no chilles, me duele mucho la cabeza, ", None), 
    ("Perdona, ¿Quieres una aspirina, ", voz_baja)

]
for frase in dialogo:
    if frase[1] == None:
        print(frase[0])
    else:
        print(frase[1] (frase[0]))
