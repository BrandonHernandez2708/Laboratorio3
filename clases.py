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
print(alumno1.Nombre,alumno1.edad,alumno1.Calificacion,resultado1)
print(alumno2.Nombre,alumno2.edad,alumno2.Calificacion,resultado2)