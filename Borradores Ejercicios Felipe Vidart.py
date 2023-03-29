# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 21:55:02 2023

@author: vidar
"""

#%%

#EJERCICIO 174

def gcd(a, b):
    if b == 0:
        return a 
    if b > a:
        return print("error: A debe ser mayor que B")
    else: 
        c = a%b
        return gcd(b, c)

prueba = gcd(5454246,684446)
print(prueba)

#%%

#EJERCICIO 175

def binario(numero):
    """
    Esta función recibe un número (Int > 1) y lo traduce a binario. Para esto se utilizan 0 y 1 como casos base y se va agregando recursivamente
    los dígitos del binario a partir de la división entera y el resto de la división al número introducido.

    Parameters
    ----------
    numero : Int
        Numero que se quiere traducir a binario.

    Returns
    -------
    Str
        String que tiene como valor el numero introducido al inicio pero en binario.

    """
    if numero == 0:
        return 0
    if numero == 1:
        return 1
    if numero < 0:
        print("ERROR: Debe introducir un numero positivo")
        numeroinput = int(input("Ingrese un numero entero positivo: "))
        binario(numeroinput)
    else:
        return str(binario(numero//2)) + str(numero%2)

numeroinput = int(input("Ingrese un numero entero positivo: "))
print(binario(numeroinput))

#%%

#EJERCICIO 177 con caso base 1 
#Hice el ejercicio con caso base 1 y caso base 0 porque al hacerlo no me di cuenta que el libro pedia hacerlo con caso base 0. La funcion
#está explicada mas adelante

valores = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

def romanoabinario(romano):
    total = 0
    if len(romano) == 1:
        total += valores[romano]
    elif len(romano) > 1:
        if romano[0] in valores:
            if valores[romano[0]] >= valores[romano[1]]:
                total += valores[romano[0]] + romanoabinario(romano[1:])
            elif valores[romano[0]] < valores[romano[1]]:
                if len(romano) > 2:
                    total += valores[romano[1]] - valores[romano[0]] + romanoabinario(romano[2:])
                elif len(romano) <= 2:
                    total += valores[romano[1]] - valores[romano[0]]
    return total

numeroromano = input("Ingrese un numero romano: ")
print(romanoabinario(numeroromano))

#%%

#EJERCICIO 177 con caso base 0

def romano2(romano):
    """
    Esta función recibe un número romano y lo devuelve en decimal. El número es procesado recursivamente utilizando un diccionario de vlaores
    para los números y muchos condicionales para sumar y restar correctamente estos valores.

    Parameters
    ----------
    romano : Str
        String que contiene el número romano que se quiere pasar a decimal.

    Returns
    -------
    total : Int
        Valor decimal del número romano.

    """
    valores = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    total = 0
    if len(romano) == 0:
        return 0
    elif len(romano) >= 1:
        if romano[0] in valores:
            if len(romano) == 1:
                return valores(romano[0])
            elif valores[romano[0]] >= valores[romano[1]]:
                total += valores[romano[0]] + romano2(romano[1:])
            elif valores[romano[0]] < valores[romano[1]]:
                if len(romano) > 2:
                    total += valores[romano[1]] - valores[romano[0]] + romano2(romano[2:])
                elif len(romano) <= 2:
                    total += valores[romano[1]] - valores[romano[0]]
        return total

numeroromano = input("Ingrese un numero romano: ")
print(romano2(numeroromano))

#%%

#EJERCICIO 183

elementosquimicos = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon','Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel','Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine','Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium','Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Cesium', 'Barium', 'Lanthanum','Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium','Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium','Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium','Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine','Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium','Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium','Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium','Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium', 'Roentgenium', 'Copernicium', 'Nihonium','Flerovium', 'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson']

diccionarioelementos = {elemento[:2].lower(): elemento for elemento in elementosquimicos}

def proximoselementos(elemento, elementosusados):
    proximos_elementos = []
    ultimaletra = elemento[-1]
    for acorte, nombre in diccionarioelementos.items():
        if acorte not in elementosusados and nombre[0].lower() == ultimaletra:
            proximos_elementos.append(nombre)
    return proximos_elementos

def secuenciafinal(elemento, elementosusados):
    proximos_elementos = proximoselementos(elemento, elementosusados)
    if not proximos_elementos:
        return elemento
    secuenciamaslarga = []
    for posibleelemento in proximos_elementos:
        secuenciaactual = secuenciafinal(posibleelemento, elementosusados + [elemento])
        if len(secuenciaactual) > len(secuenciamaslarga):
            secuenciamaslarga = secuenciaactual
            if len(secuenciamaslarga) == elementosquimicos:
                break
    return elemento + secuenciamaslarga

elementoinput = input("Introduzca el nombre de un elemento químico para encontrar su secuencia mas larga. Debido a la naturaleza del juego, se requiere que el mismo se introduzca en inglés: ").capitalize()
if elementoinput not in elementosquimicos:
    print("El elemento que ha introducido no es válido. Por favor, vuelva a correr el programa e introduzca uno válido")
else:
    secuencia = secuenciafinal(elementoinput, [])
    print("Has elegido el elemento", elementoinput)
    print("La secuencia mas larga que se puede formar con ese elemento es: ", secuencia)


#%%

#Ejercicio adicional MCD no recursiva

def mcd(a, b):
    """
    Esta función calcula el MCD de dos números. La función llama a factoresprimos() para obtener los factores primos de ambos números y para 
    cada factor y exponente que coincidan entre los números multiplica el factor por el exponente y eso se va acumulando en la variable MCD.

    Parameters
    ----------
    a : Int
        Primer número del cual se quiere buscar MCD.
    b : Int
        Segundo número del cual se quiere buscar MCD.

    Returns
    -------
    mcd : Int
        MCD entre A y B.

    """
    factoresa = factoresprimos(a)
    factoresb = factoresprimos(b)
    mcd = 1 
    for factor, exponente in factoresa.items():
        if factor in factoresb:
            exponenteb = factoresb[factor]
            exponentecomun = min(exponente, exponenteb)
            mcd *= factor ** exponentecomun
    return mcd

def factoresprimos(numero):
    """
    Esta función busca los factores primos de un número. Estos son almacenados en un diccionario que muestra los factores primos en si y sus
    exponentes.

    Parameters
    ----------
    numero : Int
        Número del cual se desea buscar los factores primos.

    Returns
    -------
    factores : Dic
        Diccionario que indica los factores primos del número y sus respectivos exponentes.

    """
    factores = {}
    #pruebo con los numeros pares
    while numero % 2 == 0:
        if 2 not in factores:
            factores[2] = 0
        factores[2] += 1
        numero //= 2
    #pruebo con los numeros impares
    factor = 3
    while factor * factor <= numero:
        while numero % factor == 0:
            if factor not in factores:
                factores[factor] = 0
            factores[factor] += 1
            numero //= factor
        factor += 2
    if numero > 2:
        if numero not in factores:
            factores[numero] = 0
        factores[numero] += 1
    return factores

a = int(input("introduzca el primer numero: "))
b = int(input("introduzca el segundo numero: "))
mcdalmacenado = mcd(a, b)
print("El MCD entre", a,"y", b,"es: ", mcdalmacenado)

#%%

# Crear una funcion recursiva que calcule el valor presente de una lista de flujos:

def valorpresente(TIR, flujos):
    """Esta función recibe una TIR periódica y una lista. Esta lista representa los flujos de fondos de un proyecto.
    Lo que hace la función es actualizar el valor del proyecto a valor presente. Comenzando desde el último flujo
    y actualizando cada flujo hasta el presente""" 
    if len(flujos) == 1: 
        VP = flujos[0]
    else:
        VP = flujos[0] + (1/(1+TIR)) * valorpresente(TIR, flujos[1:])
    return VP

valor = valorpresente(0.1, [-4000, 2000, 3000, 1000, 500, 500, 1000, 4000])
print('El valor presente del proyecto es de: ', valor)

#%%

#EJERCICIO 183 planteado como un problema de grafos:

import numpy as np

"""
Todo el código debajo que no es parte de una función fue utilizado para crear un grafo con todos los elementos 
químicos en forma de matriz. 
"""

elementosquimicos = ['Actinium', 'Aluminum', 'Americium', 'Antimony', 'Argon', 'Arsenic', 'Astatine', 'Barium', 'Berkelium', 'Beryllium', 'Bismuth', 'Bohrium', 'Boron', 'Bromine', 'Cadmium', 'Calcium', 'Californium', 'Carbon', 'Cerium', 'Cesium', 'Chlorine', 'Chromium', 'Cobalt', 'Copernicium', 'Copper', 'Curium', 'Darmstadtium', 'Dubnium', 'Dysprosium', 'Einsteinium', 'Erbium', 'Europium', 'Fermium', 'Flerovium', 'Fluorine', 'Francium', 'Gadolinium', 'Gallium', 'Germanium', 'Gold', 'Hafnium', 'Hassium', 'Helium', 'Holmium', 'Hydrogen', 'Indium', 'Iodine', 'Iridium', 'Iron', 'Krypton', 'Lanthanum', 'Lawrencium', 'Lead', 'Lithium', 'Livermorium', 'Lutetium', 'Magnesium', 'Manganese', 'Meitnerium', 'Mendelevium', 'Mercury', 'Molybdenum', 'Moscovium', 'Neodymium', 'Neon', 'Neptunium', 'Nickel', 'Nihonium', 'Niobium', 'Nitrogen', 'Nobelium', 'Oganesson', 'Osmium', 'Oxygen', 'Palladium', 'Phosphorus', 'Platinum', 'Plutonium', 'Polonium', 'Potassium', 'Praseodymium', 'Promethium', 'Protactinium', 'Radium', 'Radon', 'Rhenium', 'Rhodium', 'Roentgenium', 'Rubidium', 'Ruthenium', 'Rutherfordium', 'Samarium', 'Scandium', 'Seaborgium', 'Selenium', 'Silicon', 'Silver', 'Sodium', 'Strontium', 'Sulfur', 'Tantalum', 'Technetium', 'Tellurium', 'Tennessine', 'Terbium', 'Thallium', 'Thorium', 'Thulium', 'Tin', 'Titanium', 'Tungsten', 'Uranium', 'Vanadium', 'Xenon', 'Ytterbium', 'Yttrium', 'Zinc', 'Zirconium']

matrizgrafo = np.zeros((len(elementosquimicos), len(elementosquimicos)))
elementosnumerados = {}
contador = 0

for elemento in elementosquimicos:
    minusc = elemento.lower()
    elementosnumerados[minusc] = contador
    contador += 1

elementositems = elementosnumerados.items()
for elemento, numero in elementositems:
    letrafinal = elemento[-1]
    contador2 = 0
    for i, numero2 in elementositems:
        if i == elemento:
            continue
        if i[0] == letrafinal:
           matrizgrafo[numero][contador2] = elementosnumerados[i]
           contador2 += 1

def traduccion(secuencia):
    """
    Esta función recibe el resultado de la secuencia mas larga (que estan en forma de numeros debido al sistema de grafos)
    utilizado y devuelve esa misma secuencia pero traducida al elemento químico que cada número representa

    Parameters
    ----------
    secuencia : lista
        lista de números que representan a los diferentes elementos químicos en el grafo

    Returns
    -------
    secuenciafinal : string
        secuencia de elementos traducida por la función que son representados por los números introducidos

    """
    secuenciafinal = elementoinput + ", "
    for i, numero1 in enumerate(secuencia):
        for elemento, numero2 in elementositems:
            if i == len(secuencia)-1:
                if float(numero2) == float(numero1):
                    secuenciafinal += elemento.title()
            else:
                if float(numero2) == float(numero1):
                    secuenciafinal += elemento.title() + ", "
    return secuenciafinal

def secuencialarga(elemento, elementosusados, secuencia, matrizgrafo):
    """

    Parameters
    ----------
    elemento : string
        elemento químico desde el cual se comienza el juego
    elementosusados : lista
        lista de elementos que ya han sido usados en el juego, no es necesario introducir una en la primera llamada a la función
    secuencia : lista
        secuencia de palabras con la que trabaja la función, está formada por los números del grafo que representan a cada elemento

    Returns
    -------
    secuencia : TYPE
        DESCRIPTION.

    """
    eleminusc = elemento.lower()
    elementosusados.append((elementosnumerados[elemento]))
    for i in matrizgrafo[elementosnumerados[eleminusc]]:
        if i == 0:
            break
        if i in elementosusados:
            continue
        else:
            for elem, numero in elementositems:
                if i == numero:
                    secuenciaactual = [i] + secuencialarga(elem, elementosusados, secuencia, matrizgrafo)
                    if len(secuenciaactual) > len(secuencia):
                        secuencia = secuenciaactual    
                    return secuenciaactual
    return secuencia

secuencia = []
elementoinput = input("Introduzca el nombre de un elemento químico para encontrar su secuencia mas larga. Debido a la naturaleza del juego, se requiere que el mismo se introduzca en inglés: ").title()
if elementoinput not in elementosquimicos:
    print("El elemento que ha introducido no es válido. Por favor, vuelva a correr el programa e introduzca uno válido")
else:
    respuesta = secuencialarga(elementoinput.lower(), [], secuencia, matrizgrafo)
    print("Has elegido el elemento", elementoinput)
    print("La secuencia mas larga que se puede formar con ese elemento es: ", traduccion(respuesta))
    
#%%

#EJERCICIO TORRE DE HANOI 

def torrehanoi(n, i, a, f):
    """
    Esta funcion recibe un numero de discos, vara incial y vara final y da los pasos
    para mover esa cantidad de discos de una vara a la otra según la torre de hanoi.
    La vara de ayuda es la vara hacia la que se hacen movimiento para que sea posible 
    trasnferir todos los discos hacia la vara objetivo en orden. 

    Parameters
    ----------
    n : Int
        Número de discos 
    i : Int
        Vara inicial
    j : Int
        Vara final
    a : Int
        Vara de ayuda

    Returns
    -------
    None.
    """
    if n == 1:
        print(f"Mover el disco 1 desde la vara {i} hasta la vara {f}")
        return
    torrehanoi(n - 1, i, f, a)
    print(f"Mover el disco {n} desde la vara {i} hasta la vara {f}")
    torrehanoi(n - 1, a, i, f)

discos = int(input("Cuantos discos quiere mover? "))
vara1 = int(input("Cual es la vara inicial? "))
vara2 = int(input("Cual es la vara final? "))
ayuda = 6-(vara1+vara2)
torrehanoi(discos, vara1, ayuda, vara2)

#%%

class FF:

    def _init_(self,flujos,tir):
        
        self.flujos = flujos
        self.tir = tir
        self.p = int(input("Periodos a futuro: "))
        self.resultadova = []
        self.resultadovf = []
        
    
    def VA(self, n = 0):
        if n == len(self.flujos):  
            return None
        
        else: 
            self.resultadova.append(round(self.flujos[n]/((1+self.tir)**(n)),2))
            return self.VA(n+1)
        
    def VF(self, n = 0):
        if n == len(self.flujos):
            return None
        else:
            self.resultadovf.append(round(self.resultadova[n]((1+self.tir)*(self.p)),2))
            return self.VF(n+1)
        
def elija():
    e = input("elija si quiere el VA o VF de los flujos:")
    
    if e == "VA":
        print(ff.resultadova)
    elif e == "VF":
        print(ff.resultadovf)
    else:
        return None
    
ff = FF([7300, 2000, 8000, 3000, 5000], 0.1)
ff.VA()
ff.VF()
elija()


