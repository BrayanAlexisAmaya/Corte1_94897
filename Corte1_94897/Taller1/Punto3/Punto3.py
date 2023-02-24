#Realice un programa donde se solicite
#al usuario escribir el precio final de 
#un articulo o producto, con el que despues 
#calculara e imprimira en pantalla el valor del
#IVA y el valor bruto (precio antes de IVA) del
#articulo o producto.
Precio = float(input("Ingrese el precio final de su producto: "));
iva = Precio*0.19;
print("El valor del iva es: ",iva," y el precio de su producto sin iva es: ",Precio-iva);