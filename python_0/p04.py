#obtener datos de entrada
sueldo = float(input("Sueldo: "))
situacion = input("Situación (1/2/3): ")
num_hijos = int(input("Número de hijos: "))

#obtener exención
exencion = 0
if situacion == "1":
    if num_hijos <= 0:
        exencion = 0
    elif num_hijos == 1:
        exencion = 15947
    else:
        exencion = 17100
        
if situacion == "2":
    if num_hijos <= 0:
        exencion = 15546
    elif num_hijos == 1:
        exencion = 16481
    else:
        exencion = 17634
    
if situacion == "3":
    if num_hijos <= 0:
        exencion = 14000
    elif num_hijos == 1:
        exencion = 14516
    else:
        exencion = 15063
        
sueldo_retener = sueldo - exencion

#obtener retencion
if sueldo_retener <= 12450:
    porcentaje = 19
elif sueldo_retener <= 20200:
    porcentaje =24
elif sueldo_retener <= 35200:
    porcentaje = 30
elif sueldo_retener <= 60000:
    porcentaje = 37
elif sueldo_retener <= 300000:
    porcentaje = 45
else:
    porcentaje = 47
    
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
    















    
