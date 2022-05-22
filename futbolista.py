from deportista import Deportista
from persona import Persona

class Futbolista(Persona, Deportista): # Clase.
    listaFutbolistas = []
    
    # Atributos.
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil, deporte = "Futbol"):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, deporte, añosPracticando,)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)
        
    # Getters and Setters.
    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados
        
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas
        
    def getPiernaHabil(self):
        return self._piernaHabil
    def setPierHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil
        
    # Metodos.
    def __str__(self):
        return f"Mi nombre es {self._getNombre()} soy profesional en el deporte {self._getDeporte()} Tengo {self._getEdad()} años de edad y llevo {self._getAñosPracticando()} años en el deporte"