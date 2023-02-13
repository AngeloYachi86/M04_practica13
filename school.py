class school:
    def __init__(self, nombre, direccion, turno, profesores, estudiantes, cursos):
        self.nombre = nombre
        self.direccion = direccion
        self.turno = turno
        self.profesores = profesores
        self.estudiantes = estudiantes
        self.cursos = cursos

    # Getters
    def getNombre(self):
        return self.nombre

    def getDireccion(self):
        return self.direccion

    def getTurno(self):
        return self.turno

    def getProfesores(self):
        return self.profesores

    def getEstudiantes(self):
        return self.estudiantes

    def getCursos(self):
        return self.cursos

    # Setters
    def setNombre(self, nombre):
        self.nombre = nombre

    def setDireccion(self, direccion):
        self.direccion = direccion

    def setTurno(self, turno):
        self.turno = turno

    def setProfesores(self, Profesores):
        self.profesores = Profesores

    def setEstudiantes(self, estudiantes):
        self.estudiantes = estudiantes

    def setCursos(self, cursos):
        self.cursos = cursos

    #Metodo informacion
    def info(self):
        print("\nNombre de la escuela:", self.nombre)
        print("Direccion de la escuela:", self.direccion)
        print("Turno :", self.turno)
        print("Nombre de los profesores:", self.profesores)
        print("Nombre de los alumnos:", self.estudiantes)
        print("Lista de los cursos:", self.cursos)
