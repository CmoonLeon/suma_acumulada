# Implementación en Python de la suma acumulada usando recursividad

def suma_acumulada(n):
    # Caso base: si n es 0, la suma es 0
    if n == 0:
        return 0
    # Caso recursivo: n + suma_acumulada(n - 1)
    else:
        return n + suma_acumulada(n - 1)

# Probar la función con el número 10
resultado = suma_acumulada(10)

# Mostrar el resultado en pantalla
print(f"La suma acumulada de 10 es: {resultado}")
