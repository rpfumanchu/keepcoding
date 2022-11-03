                                                    #EJEMPLO DE HERENCIA

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

class Persona():
    def __init__(self, n, ap):
        self.nombre = n
        self.apellido = ap
        self.movil = ""
        self.correo_e = ""
        self.domicilio = ""

        self.asignaturas = []

    def alta_asignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura):
            raise Exception(f"debe ser del tipo Asignatura {asignatura}")

        self.asignaturas.append(asignatura) 


    # usamos type(self).__name__ para no tener que usar def __str__(self) con cada clase las otras lo cojeran de Persona 
    # y en su lugar ponemos {} para que lo rellene ya se Alumno, o Profesor 
    # y __repr__ podremos eliminarlo por que son exactamente iguales
    def __str__(self):
        #return "Alumno:  {} {} -{}".format(self.nombre, self.apellido, self.correo_e)
        #return (f"Persona : {self.nombre} - {self.apellido}  - {self.correo_e}")
        return (f"{type(self).__name__} - {self.nombre} - {self.apellido}  - {self.correo_e}")

    def __repr__(self):
        return self.__str__()

    
      #ponemos pass para que lo ignore y nos pase
class Alumno(Persona):  
   pass

#para heredar los atributos comunes le pedimos que nos ejecute Persona.__init__(self, n, ap) hay que comunicarle la instancia
class Profesor(Persona):
    def __init__(self, n, ap, nif, correo_e, sueldo_base=200):
        #Persona.__init__(self, n, ap)  esta es la manera antigua, es equivalente
        #  con esta otra se usa super().__init__(n, ap) no hace falta paserle el self
        #esto se llama sobreescritura
        super().__init__(n, ap)

        self.nif = nif
        self.sueldo_base = sueldo_base
        
    def alta_asignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura):
            raise Exception(f"debe ser del tipo Asignatura {asignatura}")

        self.asignaturas.append(asignatura) 

    

    #@property convierte sueldo en un objeto con el decorador property , ya no haria falata poner sueldo () con parentesis
    def sueldo(self):
        return self.sueldo_base + len(self.asignaturas) * 300


    

