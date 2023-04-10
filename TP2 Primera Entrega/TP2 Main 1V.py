# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 10:53:58 2023

@author: vidar
"""

import math
import numpy as np #numpy solo lo uso para linspace no para operaciones algebraicas
import matplotlib.pyplot as plt

class Poly:
    """La clase "Poly" permite almacenar y realizar operaciones algebraicas sobre 
    polinomios de diferente grado. En un principio, poly almacena el grado del 
    polinomio como "grado" y los coeficientes como "coefs", donde coefs[0] corresponde
    al coeficiente de grado 0, coefs[1] al de grado 1 y así sucesivamente"""
    def __init__(self, n = 0, coefs = [0]):
        if n+1 == len(coefs):
            self.n = n
            self.coefs = coefs
        else:
            print('Error: La lista de coeficientes no coincide con el grado del polinomio')
            
    def get_expression(self):
        """get_expression es un metodo de la clase Poly que devuelve un string que representa
        al polinomio en la forma: p(x) =  ax^0 + bx^1 + cx^2"""
        string = "p(x) = "
        for n in range(len(self.coefs)):
            if self.coefs[n] < math.exp(-5): #aca la idea es que si es menos a e^-5 no se imprima nada
                continue
            if len(self.coefs) == n+1:
                string += f"{self.coefs[n]}x^{n}"
            else:                
                string += f"{self.coefs[n]}x^{n} + "
        return string

    def graf_data(self, a, b):
        """graf_data es una funcion utilizada para crear los datos necesarios para graficar diferentes
        polinomios. Devuelve una listax y una listay con los respectivos valores de X e Y necesarios para
        graficar en el intervalo [a,b], que debe ser introducido en los parámetros"""
        xlist, ylist = [], []
        for i in np.linspace(a, b, 1000):
            xlist.append(i)
            ylist.append(self(i)) #aprovecho que lo hice "callable" para ahorrarme lineas
        return xlist, ylist    
            
    def poly_plt(self, a, b, **kwargs):
        """poly_plt es un método de la clase poly que sirve para graficar un polinomio en un intervalo deseado. 
        Como parámetros tiene a:
            - a y b: dos enteros que indican el intervalo en el cual se desea graficar el polinomio
            - ***kwargs: diferentes paramaetros de graficacion, estos son los parametros posibles:
                {titulo: titulo del grafico, xlabel: titulacion del eje x, ylabel: titulacion del eje y, grid: color del grid}"""
        xlist, ylist= self.graf_data(a,b)
        plt.figure()
        plt.plot(xlist, ylist)
        plt.title(kwargs['titulo'])
        plt.xlabel(kwargs['xlabel'])
        plt.ylabel(kwargs['ylabel'])
        plt.grid(kwargs['grid'])
        
    def __call__(self, x):
        """Call es una funcion que hace que Poly sea callable y evalúa el polinomio en el número
        que se introduzca en los parámetros"""
        return sum(list(map(lambda degree: self.coefs[degree]*(x**degree), range(len(self.coefs)))))
        #hace la suma de una lista. Esta lista es cada coeficiente multiplicado por el nuemro elevado a su grado.
        
    def extend(self, N):
        """Extend sirve para extender un polinomio de grado menor a n hasta que sea un polinoimo de 
        grado n. Esto se hace agregando 0s a la lista de coeficientes. Devuelve un nuevo objeto que es
        el mismo polinomio pero extendido a grado n"""
        coefs = self.coefs
        coefs.extend(0 for i in range(N-self.n))
        return self.__class__(N, coefs)
        
    def __add__(self, other):
        """add es un método de la clase Poly que permite sumar un escalar u otro polinomio a un polinomio
        ya existente. Si se suma un escalar c se tomará el escalar como un polinomio de grado 0 de la forma:
            p(x) = c"""
        if isinstance(other, int) or isinstance(other, float):
            aux_poly = self.__class__(0, [other])
            end = self + aux_poly
        if isinstance(other, type(self)):
            if self.n > other.n:
                list1, list2 = self.coefs, other.extend(self.n).coefs
            elif self.n < other.n:
                list1, list2 = self.extend(other.n).coefs, other.coefs
            else:
                list1, list2 = self.coefs, other.coefs
            end = list(map(lambda pair: pair[0] + pair[1], zip(list1,list2)))
        return end

    def __radd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self + other

    def __sub__(self, other):
        """sub es un método de la clase Poly que permite restar un escalar u otro polinomio a un polinomio
        ya existente. Si se resta un escalar c se tomará el escalar como un polinomio de grado 0 de la forma:
            p(x) = c"""
        if isinstance(other, int) or isinstance(other, float):
            end = self + (-other)
        if isinstance(other, type(self)):
            aux = self.__class__(other.n, [-elem for elem in other.coefs])
            end = self + aux
        return end

    def __rsub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            aux = self.__class__(self.n, [-elem for elem in self.coefs])
            end = aux + other
        if isinstance(other, type(self)):
            aux = self.__class__(self.n, [-elem for elem in self.coefs])
            return aux + other 
        return end

    def __mul__(self, other):
        """add es un método de la clase Poly que permite multiplicar un escalar u otro polinomio a un polinomio
        ya existente. Si se multiplica un escalar c se tomará el escalar como un polinomio de grado 0 de la forma:
            p(x) = c"""
        if isinstance(other, int):
            aux = self.__class__(0, [other])
            end = self * aux
        if isinstance(other, type(self)):
            list1, list2 = self.coefs, other.coefs
            new_list = [0 for i in range((self.n + other.n)+1)] #creo una lista con el maximo orden posible
            for indice1, i in enumerate(list1): #pongo el enumerate para saber en que orden almacenar la multiplicacion
                for indice2, a in enumerate(list2): #pongo el enumerate para saber en que orden almacenar la multiplicacion
                    new_list[indice1+indice2] += i*a
            end = new_list
        return end

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            end = self * other
        return end 
    
    def __floordiv__(self, other):
        #100% seguro que esto esta mal
        if isinstance(other, int) or isinstance(other, float):
            aux = self.__class__(0, [other])
            end = self // aux
        if isinstance(other, type(self)):
            mod_instance = self.__class__(other.n, [1/int(x) for x in other.coefs])
            end = self * mod_instance
        return end

    def __rfloordiv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            aux = self.__class__(0, [other])
            end = aux // self
        return end
    
# =============================================================================
#     def __mod__(self, other):
#         if isinstance(other, int) or isinstance(other, float):
#             aux = self.__class__(0, [other])
#             end = self % aux
#         if isinstance(other, type(self)): 
#         return end
#     # def __rmod__(self, other):
# =============================================================================
    
    def rootfind(self, interval = [-100, 100]):
        """rootfind es un metodo de Poly que permite encontrar raices de un polinomio.
        rootfind usa la bisección como método para encontrar las raices de la función.
        Tiene como parámetro intervalo, que debe ser una lista de dos elementos que indique
        donde inicia y termina el intervalo en el cual se quiere buscar una raiz. Si no se 
        introduce un intervalo el predeterminado es [-100, 100]
        En caso de que ambos numeros tengan el mismo signo la funcion retornará error (por
        teorema de Bolzano).
        rootfind tiene como tolerancia de error 0.05"""    
        #por ahora solo funciona con algunos valores, no se bien porque
        a, b = interval[0], interval[1]
        tol = 0.05
        #root = [] #esto lo hago por si los dos numeros del intervalo son raices, por ejemplo [-1, 0] en la funcion 3x^2 + 3x^3
        if self(a) == 0:
            root = a
        if self(b) == 0:
            root = b
        elif self(a)*self(b) < 0: #si uno es positivo y el otro negativo su multiplicacion da negativo
            midpoint = a + (b-a)/2 #busco punto medio
            if -tol < self(midpoint) < tol:
                root = midpoint
            elif self(midpoint)*self(b) < 0: #si el punto medio y b tienen signo distinto hay una raiz en el medio
                self.rootfind([midpoint, b])
            elif self(midpoint)*self(a) < 0: #si a y el punto medio tienen signo distinto hay una raiz en el medio
                self.rootfind([a, midpoint])
        elif (self(a) != 0) and (self(b) != 0) and (self(a)*self(b) < 0):
            print('ERROR: No existe una raiz en ese intervalo')
            root = None
        return root
        
#%%

if __name__ == "__main__":   
    polinomio_test = Poly(4, [1,3,2,4,6])
    
    #print(polinomio_test.get_expression())
    
    #print(polinomio_test.poly_plt(-20, 20, titulo="Grafico del polinomio", xlabel='Eje X', ylabel='Eje Y', grid='k'))
    
    #print(polinomio_test(3))
    
    #polinomio_suma = Poly(2, [3,5,6])
    #print(66 + polinomio_test)
    #print(polinomio_test + polinomio_suma)
    
    #polinomio_resta = Poly(2, [3,5,6])
    #print(66 - polinomio_test)
    #print(polinomio_resta - polinomio_test)
    
    #polinomio_mult = Poly (2, [2,4,3])
    #print(4 * polinomio_test)
    #print(polinomio_test*polinomio_mult)
    #print(polinomio_mult * polinomio_test)
    
    #polinomio_div = Poly (2, [2,4,3])
    #print(polinomio_test//2)
    #print(polinomio_test//polinomio_div)
    #print(polinomio_div//polinomio_test)
    
    polinomio_rootsimple = Poly(2, [0, 3, 3])
    print(polinomio_rootsimple.rootfind([-0.5, 0.75]))    
    
          