from CL22006UNO import GaussianElimination

# Define un sistema de ecuaciones lineales
matriz = [
    [5, -1],
    [2, 7],
]
resultados = [1, -1]

# Crea una instancia de GaussianElimination
solucionador = GaussianElimination(matriz, resultados)

# Resuelve el sistema usando eliminación de Gauss
try:
    soluciones = solucionador.Gauss()
    print("Soluciones usando eliminación de Gauss:", soluciones)
except ValueError as e:
    print("Error:", e)

# Resuelve el sistema usando eliminación de Gauss-Jordan
try:
    soluciones = solucionador.gauss_jordan()
    print("Soluciones usando eliminación de Gauss-Jordan:", soluciones)
except ValueError as e:
    print("Error:", e)

# Resuelve el sistema usando la regla de Cramer
try:
    soluciones = solucionador.cramer()
    print("Soluciones usando la regla de Cramer:", soluciones)
except ValueError as e:
    print("Error:", e)

# Resuelve el sistema usando descomposición LU
try:
    soluciones = solucionador.lu_decomposition()
    print("Soluciones usando descomposición LU:", soluciones)
except ValueError as e:
    print("Error:", e)

# Resuelve el sistema usando el método de Jacobi
try:
    soluciones = solucionador.jacobi()
    print("Soluciones usando el método de Jacobi:", soluciones)
except ValueError as e:
    print("Error:", e)

# Resuelve el sistema usando el método de Gauss-Seidel
try:
    soluciones = solucionador.gauss_seidel()
    print("Soluciones usando el método de Gauss-Seidel:", soluciones)
except ValueError as e:
    print("Error:", e)

# Ejemplo para el método de bisección
def funcion_de_prueba(x):
    return x**4 + 7*x**3 - 7  # Función con raíces en x = -2 y x = 2

# Usa el método de bisección para encontrar la raíz en el intervalo [0, 1]
try:
    raiz = solucionador.bisection(funcion_de_prueba, 0, 1)  # Intervalo [0, 1]
    print("Raíz encontrada usando el método de bisección:", raiz)
except ValueError as e:
    print("Error:", e)
