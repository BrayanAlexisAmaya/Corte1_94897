import numpy as nump
print("\nEjercicios: \n\n1. Numero mayor o menor a 10. \n2. Dia de sabado a domingo.");
print("3. Mayor o menor de edad. \n4. Resolver una funcion cuadratica sin imaginarios.");
print("5. iniciando con bucles. ");
print("\n\nO ingrese 0 para salir.")
ejercicio = int(input("\nIngrese el numero de el ejercicio que quiere realizar: "));

if ejercicio == 0:
    print("Gracias por ejecutar");

elif ejercicio == 1:
    num = int(input("Ingrese un numero: "));
    if num < 10:
        print("El numero es menor que 10");
    elif num == 10:
        print("El numero es igual a 10");
    else:
        print("El numero es mayor que 10");
    print("final del proceso");

elif ejercicio == 2:
    dia = input("Ingrese el dia").lower();
    print(dia);
    if dia == hola:
        print("El numero es menor que 10");

elif ejercicio == 3:
    edad = int(input("Ingrese su edad: "));
    if edad < 18:
        print("Usted es menor de edad");
    elif edad >= 18:
        print("Usted es mayor de edad");

elif ejercicio == 4:
    a = int(input("\nIngrese un valor para a: "));
    b = int(input("\nIngrese un valor para b: "));
    c = int(input("\nIngrese un valor para c: "));
    t = (b**2)-(4*a*c);
    if t > 0:
        v1 = (-b + nump.sqrt(t))/(2*a)
        v2 = (-b - nump.sqrt(t))/(2*a)
        print("\nEl primer valor es: ",v1);
        print("\nEl segundo valor es: ",v2);
    elif t < 0:
        print("\nEl resultado es imaginario");

elif ejercicio == 5:
    print("\nEjercicios: \n\n1. while con brake. \n2. while con continue.");
    print("\n\nO ingrese 0 para salir.")
    ejercicio = int(input("\nIngrese el numero de el ejercicio que quiere realizar: "));
    if ejercicio == 0:
        print("Gracias por ejecutar");
    elif ejercicio == 1:
        n = 0;
        while n < 10:
            n +=1;
            print(n);
            if n>6:
                break
        print("Fin del proceso");
    elif ejercicio == 2:
        n = 0;
        while n < 10:
            n +=1;
            print(n);
            if n>6:
                print(n);
                n +=1;
                continue;
             
        print("Fin del proceso");
else:
    print("No se ha encontrado el ejercicio");
