class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    def __str__(self):
        return "El vehiculo es de color {}, tiene cantidad de ruedas {}, y cantidad de puertas {}".format(self.color, self.ruedas, self.puertas)
class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        Vehiculo.__init__(self,color,ruedas,puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada    
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} Velocidad y cilindrada de {}".format(self.velocidad, self.cilindrada)

mi_Vehiculo = Vehiculo('azul','4','5')
print(mi_Vehiculo)
mi_Coche = Coche('rojo','4','3','240','1600')
print(mi_Coche)