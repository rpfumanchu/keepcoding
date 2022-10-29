#creamos dos variables globales y constantes y como no quiero que nadie las borre las pongo en mayusculas
RANGOS = [12450, 20200, 35200, 60000, 300000]
PORCENTAJES = [19, 24, 30, 37, 45, 47]


def obtener_exencion(sit, nhijos):
#obtener exención
    exencion = 0
    if sit == "1":
        if nhijos <= 0:
            exencion = 0
        elif nhijos == 1:
            exencion = 15947
        else:
            exencion = 17100
            
    if sit == "2":
        if nhijos <= 0:
            exencion = 15546
        elif nhijos == 1:
            exencion = 16481
        else:
            exencion = 17634
        
    if sit == "3":
        if nhijos <= 0:
            exencion = 14000
        elif nhijos == 1:
            exencion = 14516
        else:
            exencion = 15063
    return exencion

def obtener_retencion(base):
    #obtener retencion
    # este if no hace falta si le añadimos 0 y 0, 0 en las tablas de arriba
    # if base<= 0:
    #     return 0
    i = 0
    while i < len(RANGOS):
        if base <= RANGOS[i]:
            #con break rompemos el bucle y se sale
            break
        #incrementamos y avanzamos una posicion
        i += 1
    return PORCENTAJES [i]
  

def obtener_retencion_for(base):
    i = 0
    for rango in [RANGOS]:
        if base <= RANGOS[i]:
            break
        i += 1
    return PORCENTAJES[i]


def test():
    pass

   