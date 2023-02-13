class Llibre:
    def __init__(self, titol, autor, any, editorial, pagines, preu):
        self.titol = titol
        self.autor = autor
        self.any = any
        self.editorial = editorial
        self.pagines = pagines
        self.preu = preu

    #Aquests son el Getters
    def getTitol(self):
        return self.titol

    def getAutor(self):
        return self.autor

    def getAny(self):
        return self.any

    def getEditorial(self):
        return self.editorial

    def getPagines(self):
        return self.pagines

    def getPreu(self):
        return self.preu


    # Aquests son el Setters
    def setTitol(self, titol):
        self.titol = titol

    def setAutor(self, autor):
        self.autor = autor

    def setAny(self, any):
        self.any = any

    def setEditorial(self, editorial):
        self.editorial = editorial

    def setPagines(self, pagines):
        self.pagines = pagines

    def setPreu(self, preu):
        self.preu = preu


    def titolLlibre(self):
        print("El titol del llibre es: " + self.titol)





