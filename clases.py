class Alumno:
    def __init__(self, Nombre, edad, Calificacion):
        self.Nombre = Nombre
        self.edad = edad
        self.Calificacion = Calificacion
    
    def nota(self):
        return self.Calificacion >= 60

alumno1=Alumno("Juan",20,60)
alumno2=Alumno("Maria",20,30)
resultado1 = "Aprobado" if alumno1.nota() else "Reprobado"

resultado2 = "Aprobado" if alumno2.nota() else "Reprobado"
print("El alumno:", alumno1.Nombre, "de", alumno1.edad, "años con la nota de", alumno1.Calificacion, "está", resultado1)
print("El alumno:", alumno2.Nombre, "de", alumno2.edad, "años con la  nota de", alumno2.Calificacion, "está", resultado2)