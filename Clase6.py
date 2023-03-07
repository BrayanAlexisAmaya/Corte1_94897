import random as r
import math 
print("Escoja el ejercicio que desea realizar: ");
print("1. Ejercicio aleatorio.")
print("2. seno, coseno, tangente.")
punto = int(input("Ingrese el numero del ejercicio a realizar: "));
def Aleatorio():
   p = r.randint(100,120);
   if p == 110 or p == 115 or p == 119:
      p = p-1;
   return p

def calcu(n,funcion):
    
    if funcion == "seno":
        seno = math.sin(n);
        return seno;
    elif funcion == "coseno":
        coseno = math.cos(n);
        return coseno;
    elif funcion == "tangente":
        tangente = math.tan(n);
        return tangente;
    elif funcion == "exponencial":
        expo = math.exp(n);
        return expo;
    elif funcion == "logaritmo":
        log = math.log(n);
        return log;



if punto == 1:

    i = 0;
    while i < 10:
        print(Aleatorio());
        i += 1;

elif punto == 2:

    funcion = input("Ingrese la funcion que quiere realizar: tangente, exponencial, logaritmo, seno o coseno: ").lower();
    n = float(input("Ingrese un numero: "));
    print(calcu(n,funcion));

   
