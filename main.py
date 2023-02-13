from animal import animal
from vehicle import vehicle
ingresarAnimal = animal("Perro","canino","pequines",2,"50 kg","blanco")
ingresarAnimal.saludar()
ingresarAnimal.setRaza("chiguagua")
ingresarAnimal.saludar()

ingresarVehicle = vehicle("Toyota","Corolla", 2022,"2 toneladas",4,"Amarillo")
ingresarVehicle.partes()
ingresarVehicle.setAño(2020)
ingresarVehicle.partes()