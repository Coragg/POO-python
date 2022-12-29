class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperature = "Caliente"):
        self._llenar_tanque_de_agua(temperature)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperature):
        print(f"Llenando el tanque con agua {temperature}")

    def _anadir_jabon(self):
        print("Añadiendo jabon")

    def _lavar(self):
        print("Lavando la ropa")

    def _centrifugar(self):
        print("Centrifugando la ropa")


if __name__ == "__main__":
    primera_lavadora = Lavadora()
    primera_lavadora.lavar()
