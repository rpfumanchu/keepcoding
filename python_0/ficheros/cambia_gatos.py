perro = open("perro_perra.txt", "r")

lineas = perro.readlines()
perro.close()
nuevas_lineas = []
for linea in lineas:
    nuevas_lineas.append(linea.replace("perr", "gat"))

gato = open("gato_gata.txt", "w")
gato.writelines(nuevas_lineas)
gato.close()
