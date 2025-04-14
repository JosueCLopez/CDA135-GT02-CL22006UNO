# GaussianElimination

Este proyecto implementa múltiples métodos numéricos para resolver sistemas de ecuaciones lineales y encontrar raíces de funciones.

Incluye algoritmos clásicos como Eliminación de Gauss, Gauss-Jordan, Regla de Cramer, Descomposición LU, así como métodos iterativos como Jacobi y Gauss-Seidel. También incluye el método de Bisección para la búsqueda de raíces.

## Características

-   ✅ Eliminación de Gauss
-   ✅ Gauss-Jordan
-   ✅ Regla de Cramer
-   ✅ Descomposición LU
-   ✅ Método de Jacobi
-   ✅ Método de Gauss-Seidel
-   ✅ Método de Bisección para encontrar raíces de funciones
-   ✅ Cálculo del determinante de matrices

## Estructura del Proyecto

El proyecto se basa en una clase principal:

```python
class GaussianElimination:
    def __init__(self, matrix, results):
        self.matrix = matrix
        self.results = results
```
# GaussianElimination

Este proyecto proporciona una clase de Python (`GaussianElimination`) que implementa varios métodos numéricos para resolver sistemas de ecuaciones lineales y encontrar raíces de funciones.

## Métodos Disponibles

Cada método está implementado como una función dentro de esta clase.

-   `determinant(matrix)`: Calcula el determinante de una matriz cuadrada.
-   `Gauss()`: Resuelve el sistema mediante eliminación de Gauss.
-   `gauss_jordan()`: Resuelve el sistema utilizando el método de Gauss-Jordan.
-   `cramer()`: Aplica la Regla de Cramer para resolver el sistema.
-   `lu_decomposition()`: Utiliza la descomposición LU para encontrar la solución.
-   `jacobi(max_iterations=100, tolerance=1e-10)`: Resuelve el sistema utilizando el método iterativo de Jacobi.
-   `gauss_seidel(max_iterations=1000, tolerance=1e-10)`: Resuelve el sistema mediante el método de Gauss-Seidel.
-   `bisection(func, lower, upper, max_iterations=100, tolerance=1e-10)`: Encuentra raíces de funciones con el método de bisección.

## Requisitos

-   Este proyecto no requiere librerías externas. Está desarrollado solo con Python puro.
-   Compatible con Python 3.x.

## Instalación

-   Para instalar este proyecto solamente tendras que digitar en tu consola Python
 ```
 pip install CL22006UNO
```
  


## Ejemplos de Uso
 ```python

    from CL22006UNO.GaussianElimination import GaussianElimination

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
    ```

