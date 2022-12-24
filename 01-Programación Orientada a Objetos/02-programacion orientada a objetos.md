<h2> Clases en Python</h2>

<p>Las clases proveen una estructura, o en otras palabras, nos dan un modelo con el cual podamos construir objetos mas especifico o generar nuevos tipos de datos. </p>

<h2> Instancias </h2>

<p>Mientras que las clases nos dan la estructura, las intancias son los objetos reales que creamos. Otra forma de verlo es que las clases son como un formulario y las intancias son las que pertenecen a dicha clase, pueden tener sus variaciones y cada instancia es distinta de la otra. </p>

<p> Para definir una clase, se utiliza el keyword class. Ejemplo:</p>

<pre><code>class Person:
    pass
</code></pre>

<p>Una vez que tenemos una clase, podemos generar la instancia llamando al constructor de la clase.</p>

<pre><code>tomas = Person() </code></pre>


<h2>Atributos de la instancia</h2>

<p>      
Las clases generan objetos y todas las clases clases tienen atributos.
</p>

<p>Para poder definir tales objetos, usamos el metodo especial __init__ (viene con doble guión bajo) para definir el estado inicial de nuestra instancia. Teniendo en cuenta que hay que usar el parametro obligatorio self (referencia a la instancia).</p>
<br/>
<pre><code>class Hotel:

    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0

hotel = Hotel(numero_maximo_de_huespedes = 50, lugares_de_estacionamiento = 20)
print(hotel.lugares_de_estacionamiento)
</code></pre>
<br/>
<h2>Método de instancias</h2>

<p>Los atributos describen a la clase, los metodos nos indican que podemos hacer con esa clase al ser instanciada. Pero comunmente los métodos son vistos como funciones.</p>

<br/>
<pre><code>class Hotel:

    ...

    def anadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes

    def checkout(self, cantidad_de_huespedes):
        self.huespedes -= cantidad_de_huespedes

    def ocupacion_total(self):
        return self.huespedes


hotel = Hotel(50, 20)
hotel.anadir_huespedes(3)
hotel.checkout(1)
hotel.ocupacion_total() 

</code></pre>


