
class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = "reposo"
        self._motor = Motor(cilindros = 4)

    def aceleracion(self, velocidad):
        if velocidad > 120:
            return "we can't do that"
        else:
            gasolina = 0.08 * (velocidad ** 2)
            self._motor.inyecta_gasolina(gasolina)
        self._estado = "en movimiento"



class Motor:
    def __init__(self, cilindros, tipo = 'gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatua = 0
        self._cantidad_gasolina = 0

    def inyecta_gasolina(self, cantidad):
        return _cantidad_gasolina - cantidad


