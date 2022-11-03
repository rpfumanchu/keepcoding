class Asignatura():
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel
        self.hora = 0
     #con :.2f redondeamos a dos decimales
    def __str__(self):
        return (f"Asignaturas:  {self.nombre} {self.nivel}  - ({self.precio_h*4:.2f} euros/mes)")

    def __repr__(self):
        return self.__str__()

class Alumno():  
    def __init__(self, n, ap):
        self.nombre = n
        self.apellido = ap
        self.movil = ""
        self.correo_e = ""

        self.asignaturas = []

    def alta_asignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura):
            raise Exception(f"debe ser del tipo Asignatura {asignatura}")

        self.asignaturas.append(asignatura) 

    def __str__(self):
        #return "Alumno:  {} {} -{}".format(self.nombre, self.apellido, self.correo_e)
        return (f"Alumno : {self.nombre} python- {self.apellido}  - {self.correo_e}")

    def __repr__(self):
        return self.__str__()

class Profesor():
    def __init__(self, n, ap, nif, correo_e, sueldo_base=200):
        self.nombre = n
        self.apellidos = ap
        self.nif = nif
        self.movil = ""
        self.sueldo_base = sueldo_base
        self.correo_e = correo_e

        self.asignaturas = []

    def alta_asignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura):
            raise Exception(f"debe ser del tipo Asignatura {asignatura}")

        self.asignaturas.append(asignatura) 

    def __str__(self):
        #return "Alumno:  {} {} -{}".format(self.nombre, self.apellido, self.correo_e)
        return (f"Profesor : {self.nif} - {self.nombre} - {self.apellidos} - {self.correo_e}")

    def __repr__(self):
        return self.__str__()

    #@property convierte sueldo en un objeto con el decorador property , ya no haria falata poner sueldo () con parentesis
    def sueldo(self):
        return self.sueldo_base + len(self.asignaturas) * 300


    

