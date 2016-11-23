'''
Created on 23 nov. 2016

@author: najib
'''
from fibonacci_funcion.funcion_fibonacci import fibonacci
numero=int(input("Escribe un numero entero:"))
fibonacci=fibonacci(numero)
print("La funcion de fibonacci del numero %d"%numero,"es %d"%fibonacci)