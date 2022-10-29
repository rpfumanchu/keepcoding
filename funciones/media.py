#con pass simplemente pasaa la siguiente lo 
from mis_funciones import nota_numerica
def media(*notas):
    suma_notas = 0
    for nota in notas:
        valor_nota = nota_numerica(nota)
        suma_notas += valor_nota
#si en vez de == ponemos > 0 al no cumplirse nos devuelve none por defecto y nos ahorramos el else
    if len(notas) > 0:
        return suma_notas / len(notas)

    """para que sea una lista de valores indeterminada ponemos un * delante"""
def multientrada(*valores):
    for valor in valores:
        print(valor*2) 

def boletin(**asignaturas):
    #notas =[]
    for asignatura, nota in asignaturas.items():
        print(f"{asignatura} - {nota}")
     #   notas.append(nota)
#o bien lo hacemos manualmente "esta comentado" o utilizo asignaturas que es un diccionario lo paso a list y hacedo co .values
    notas = list(asignaturas.values())
    nota_media = media(*notas)
    print(f"Media: {nota_media}")
    
#para poder utilizar clave valor lo hacemos co doble **
def multientrada_1(**pares_clave_valor):
    print(pares_clave_valor)
    for clave, valor in pares_clave_valor.items():
        print(clave, "-", valor)

def control():
    pass