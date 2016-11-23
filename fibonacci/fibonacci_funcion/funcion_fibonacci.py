'''
Created on 23 nov. 2016

@author: najib
'''
def fibonacci(num):
    if num==0:
        return 0
    if num==1:
        return 1
    else:
        fibonacci1=fibonacci(num-1)
        fibonacci2=fibonacci(num-2)
        fibonacci_final=fibonacci1+fibonacci2
        return fibonacci_final
if __name__=="__main__":
    numero=int(input("Escribe un numero entero:"))
    print(fibonacci(numero))