N = int(input("Ingrese un numero entero: "));
i = 0;
print("Los numeros impares son: ");
while i <= N:
    if i%2 != 0:
        print(f"{i}, ", end="");
    i += 1;

N = int(input("Ingrese un numero entero: "));
i = 2;
p = True;
while i < N:
    if N%i == 0:
        print("El numero no es primo");
        p = False;
        break;
    i += 1;
if p != False:
  print("El numero es primo");
print("Los numeros primos son: \n1");
l = 1;
p = True;
while l < N:
    p = True;
    i = 2;
    while i < l:
        if l%i == 0:
            p = False;
            break;
        i += 1;
        if p != False:
            print(l);
            break;
    l += 1;
    
   

    