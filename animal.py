class animal:
    def __init__(self, nombre, especies, raza, edad, peso, color):
        self.nombre = nombre
        self.especies = especies
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setEspecies(self, especies):
        self.especies = especies

    def getEspecies(self):
        return self.species

    def setRaza(self, raza):
        self.raza = raza

    def getRaza(self):
        return self.raza

    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad

    def setPeso(self, peso):
        self.peso = peso

    def getPeso(self):
        return self.peso

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def saludar(self):
        print("\nDades de l'animal:")
        print("Nombre:", self.nombre)
        print("Especie:", self.especies)
        print("Raza:", self.raza)
        print("Edad:", self.edad)
        print("Peso:", self.peso)
        print("Color:", self.color)

