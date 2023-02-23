Dis = float(input("Ingrese la distancia recorrida: "));
Consumo = float(input("Ingrese el consumo de combustible: "))/100;
CostA = float(input("Ingrese el costo promedio anual de combustible: "));
CostoTotal = Dis*Consumo*CostA;
print("Su costo anual del consumo de combustible es: ",CostoTotal);