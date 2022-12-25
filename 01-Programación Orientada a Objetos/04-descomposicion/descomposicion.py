
class Automovil:
    
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = "en_reposo" # el guion bajo es una convencion para definir que es un atributo privado
        self._motor = Motor(cilindros=4)
    
    def aceleracion(self, tipo = 'despacio'):
        if tipo == 'rapido':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        self._estado = "en_movimiento"
        


class Motor:

    def __init__(self, cilindros, tipo = "gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass 