# los decoradores se suelen usar en funciones de hight order
def funcion_decorado(funcion):
    def wrapper():
        print('Este es el ultimo mensaje ...')
        funcion()
        print('Este es el primer mensaje ...')
    return wrapper

@funcion_decorado
def cristo():
    print('viva cristo rey. ')

cristo()

""" 
def funcion_decoradora(funcion):
	def wrapper():
		print("Este es el último mensaje...")
		funcion()
		print("Este es el primer mensaje ;)")
	return wrapper

def zumbido():
	print("Buzzzzzz")

zumbido = funcion_decoradora(zumbido) """