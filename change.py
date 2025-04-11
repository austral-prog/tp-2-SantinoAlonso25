print("Ingresar gasto:")
gasto = float(input())

print("Dinero recibido")
pagado = float(input())

vuelto = pagado - gasto

pesos = int(vuelto)
centavos = int(round((vuelto - pesos) * 100))

print("\nVuelto\n")
print("Pesos:")
print(pesos)
print("Centavos:")
print(centavos)