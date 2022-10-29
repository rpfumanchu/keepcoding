#creamos dos variables globales y constantes y como no quiero que nadie las borre las pongo en mayusculas

#TABLA DENTRO DE OTRA TABLA  TABLA BIDIMENSIONAL                                                     float("inf") el número infinito mas grande que tu consola pueda representar
RETENCIONES = [[0, 0], [12450, 19], [20200, 24], [35200, 30], [60000, 37], [300000, 45], [float("inf"), 47]]

SIT1 = [0, 15947, 17100]
SIT2 = [15546, 16481, 17634]
SIT3 = [14000, 14516, 15063]


def obtener_exencion(sit, nhijos):
#obtener exención
    if nhijos > 2:
        nhijos = 2
    elif nhijos < 0:
        nhijos = 0
    if sit == "1":
        return SIT1[nhijos]
    if sit == "2":
        return SIT2[nhijos]
    if sit == "3":
        return SIT2[nhijos]
    return 0

def obtener_retencion_for(base):
    for retencion in RETENCIONES:
        if base <= retencion[0]:
            return retencion[1]


def test():
    pass

   