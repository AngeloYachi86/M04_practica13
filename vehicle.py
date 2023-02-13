class vehicle:
    def __init__(self, marca, modelo, año, peso, numPuertas, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.peso = peso
        self.numPuertas = numPuertas
        self.color = color

    # Getters
    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def getAño(self):
        return self.Año

    def getPeso(self):
        return self.peso

    def getNumPuertas(self):
        return self.numPuertas

    def getColor(self):
        return self.color

    # Setters
    def setMarca(self, marca):
        self.marca = marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def setAño(self, año):
        self.año = año

    def setPeso(self, peso):
        self.peso = peso

    def setNumPuertas(self, numPuertas):
        self.numPuertas = numPuertas

    def setColor(self, color):
        self.color = color

    # Método partes
    def partes(self):
        print("\nMarca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año:", self.año)
        print("Peso:", self.peso)
        print("Numero de puertas:", self.numPuertas)
        print("Color:", self.color)

