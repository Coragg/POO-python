
class Coordenadas: 
    
    def __init__(self, x, y):
        # atributos
        self.x = x
        self.y = y

    #metodo
    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x) **  2
        y_diff = (self.y - otra_coordenada.y) ** 2

        return (x_diff + y_diff) ** 0.5



if __name__ == '__main__':
    coor_1 = Coordenadas(3, 30)
    coor_2 = Coordenadas(4, 8)

    print(coor_1.distancia(coor_2))
    print(isinstance(coor_1, Coordenadas)) # isinstance(obj, class) nos sirve para verificar si un objeto esta instanciado con una clase