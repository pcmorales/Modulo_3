# Importar las librerías necesarias para el proyecto de Máquina de Galton.
import numpy as np  # Biblioteca que ofrece soporte para arrays multidimensionales y funciones matemáticas de alto nivel.
import random  # Es un módulo que proporciona funciones para generar números pseudoaleatorios y realizar operaciones aleatorias.
from matplotlib import pyplot as plt  # Matplotlib es una librería que incluye varios módulos para la visualización de datos, y uno de ellos es pyplot.

# Configurar los parámetros de la simulación de la Máquina de Galton.
canicas = 3000  # Número de canicas.
niveles = 12    # Número de niveles de obstáculos.
contenedores = niveles + 1  # Número total de contenedores.

# Se inicializa el array para contar el número de canicas en cada contenedor.
cant_contenedores = np.zeros(contenedores, dtype=int)  # np.zeros(), es una función de NumPy que crea un array lleno de ceros.

# Se simula la caída de cada canica.
for canica in range(canicas):  # Se repite la simulación para cada canica.
    # Se inicializa la posición de la canica en el centro.
    posicion_act = 0

    # Se simula el paso de la canica a través de cada nivel.
    for nivel in range(niveles):  # Se repite para cada nivel.
        valor_aleatorio = random.random()  # Se genera un valor aleatorio entre 0 y 1.

        if valor_aleatorio >= 0.5:
            posicion_act += 1  # Si el valor aleatorio es mayor o igual a 0.5, mueve la canica a la derecha.
        # No se necesita el else para mover la canica a la izquierda, ya que el movimiento es implícito.

    # Se ajusta la posición final de la canica para que esté dentro del rango de contenedores.
    posicion_act = min(max(posicion_act, 0), contenedores - 1)
    
    # Se incrementa el conteo del contenedor donde terminó la canica.
    cant_contenedores[posicion_act] += 1

# Se crea el histograma para visualizar los resultados.
plt.bar(range(contenedores), cant_contenedores, color='green', edgecolor='black')
plt.xlabel('Contenedor')  # Etiqueta del eje X.
plt.ylabel('Número de Canicas')  # Etiqueta del eje Y.
plt.title('Distribución de Canicas en la Máquina de Galton')  # Título del gráfico.
plt.xticks(range(contenedores))  # Asegura que todas las posiciones de los contenedores estén etiquetadas.
plt.show()  # Mostrar el gráfico.