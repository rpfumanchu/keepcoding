from p04funciones_bis2 import obtener_exencion, obtener_retencion
#from p04funciones import * con el asterisco nos traemos todo lo que este en ese fichero



#obtener datos de entrada
sueldo = float(input("Sueldo: "))
situacion = input("Situación (1/2/3): ")
num_hijos = int(input("Número de hijos: "))


#recurda aqui usaremos las variables globales "sit y nhijos son variables locales que solo existen dentro de la función no fuera"
exencion = obtener_exencion(situacion, num_hijos)    
sueldo_retener = sueldo - exencion
porcentaje = obtener_retencion(sueldo_retener)


    
monto_anual = sueldo_retener * porcentaje / 100
monto_mensual = monto_anual / 12

#mostrar resultado
print(f"Sueldo anual: \t {sueldo}")
print(f"situación:\t {situacion}")
print(f"Base a retener: {sueldo_retener}")
print(f"Porcentaje:\t {porcentaje}")
print(f"monto anual:\t {monto_anual}")
print()
print(f"Retención mensual: {monto_mensual}")
    
def test():
    pass














    
