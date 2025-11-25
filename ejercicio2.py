# Programa: término n-ésimo de una progresión geométrica

a1 = float(input("Ingresa el primer término (a1): "))
r = float(input("Ingresa la razón (r): "))
n = int(input("Ingresa el número de término que quieres (n): "))

an = a1 * (r ** (n - 1))

print("El término número", n, "de la progresión geométrica es:", an)
if r != 1:
    sn = a1 * (r**n - 1) / (r - 1)

else:
     a1 * n


print("La suma de los primeros", n, "términos de la progresión geométrica es:", sn)