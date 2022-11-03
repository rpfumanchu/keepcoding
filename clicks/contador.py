def creaContador(ini = 0):
    clicks = ini

# diciendole nom local python va a buscar en todos los ambitos superiores donde esta clicks y si le pusieramos global nos lo sacaria fuera de la función 
    def click():
        nonlocal clicks
        clicks = clicks + 1
        return clicks
    return click

def crea_Con_Reu(ini = 0):
    clicks = ini

    def contador(**kwargs):
        nonlocal clicks

        if len(kwargs) == 0:
            clicks = clicks +1
            return clicks
        if "consulta" in kwargs:
            return clicks

        if "reset" in kwargs:
            #aqui debe validarse si kwargs["reset"] es >= 0 y enetro
            clicks = kwargs["reset"]
            print("reseateado a ", clicks)
            return clicks

        #raise Exception("Función desconocida")
        

    return contador
