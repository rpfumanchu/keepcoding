#creamos dos variables globales y constantes y como no quiero que nadie las borre las pongo en mayusculas

#TABLA DENTRO DE OTRA TABLA  TABLA BIDIMENSIONAL                                                     float("inf") el número infinito mas grande que tu consola pueda representar
RETENCIONES = [[0, 0], [12450, 19], [20200, 24], [35200, 30], [60000, 37], [300000, 45], [float("inf"), 47]]

SITUACIONES = {
    "1": [0, 15947, 17100],
    "2": [15546, 16481, 17634],
    "3": [14000, 14516, 15063],
}
    
def obtener_exencion(sit, nhijos):
#obtener exención
    if nhijos > 2:
        nhijos = 2
    elif nhijos < 0:
        nhijos = 0
    return SITUACIONES[sit] [nhijos]
    
   

def obtener_retencion(base):
    for retencion in RETENCIONES:
        if base <= retencion[0]:
            return retencion[1]


def test():
    pass

   