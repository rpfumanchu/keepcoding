from academia02 import Alumno,Asignatura
from academia02 import Profesor


roberto = Alumno("Roberto", "Rodriguez")
susana = Alumno("Susana", "Martin")

print(roberto.nombre, roberto.apellido, roberto) #roberto rodriguez
print(susana.nombre, susana.apellido, susana) #susana martin

print(roberto.correo_e, roberto.movil, roberto, susana) # vacio

ingles = Asignatura("Ingles", "A2")
ingles.precio_h = 7.5
aleman = Asignatura("Alemán", "A2")
aleman.precio_h = 8
chino = Asignatura("Chino Cantones", "A1")
chino.precio_h = 10

print(ingles) #Asignatura:Ingles - A2 - (30.00 eueros/mes)

roberto.alta_asignatura(ingles)
roberto.alta_asignatura(chino)

#susana.alta_asignatura(ingles)
#susana.alta_asignatura("ingles") # asi me daria 

print(roberto.asignaturas) #Asignatura:Ingles - A2 - (30.00 eueros/mes), Asignatura: Chino.....
print(susana.asignaturas) # 

roberto.asignaturas = None
print(roberto.asignaturas)

donJose = Profesor("Jose", "Martin Fustas", "0w", "jf@email.com")
print(donJose) #Profesor: 0w - Jose Martin Fusta - jf@email.com

#sueldo tiene que ir con () por que es un metodo que hay que calcularlo es una funcion
print(donJose.sueldo()) #200
donJose.alta_asignatura(ingles)

print(donJose.asignaturas) #[asignatura: Ingles - A2 -(30.00 euros/mes)]
print(donJose.sueldo()) #500
