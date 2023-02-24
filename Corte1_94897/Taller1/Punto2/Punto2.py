#Realice un programa que calcule el indice 
#de masa corporal de una persona, donde le solicite
#al usuario la estatura en cm y el peso en Kg. 
#Despues imprima como resultado el indice de masa 
#corporal mediante un mensaje que diga Su IMC es 
#<valor> redondeado con dos decimales. p/m^2
Estatura = int(input("Ingrese su estatura en centrimetros: "));
Peso = int(input("Ingrese su peso en Kg: "));
IMC = Peso/((Estatura*0.01)**2);
print("Su IMC es de: ",IMC);