# Codigo UML en POO 

from datetime import date

class Persona:
    def __init__(self, nombre: str, nif: str, fechaNac: date):
        self.nombre = nombre
        self.nif = nif
        self.fechaNac = fechaNac

    def __str__(self):
        return f"{self.nombre}, NIF: {self.nif}, Fecha de Nac: {self.fechaNac}"

class Jugador(Persona):
    def __init__(self, nombre: str, nif: str, fechaNac: date, numFed: int):
        super().__init__(nombre, nif, fechaNac)
        self.numFed = numFed

    def __str__(self):
        return f"{super().__str__()}, Número Federación: {self.numFed}"

jugador = Jugador("Daniel Medina", "12345678X", date(2007, 2, 5), 2025)
print(jugador)
