import random
from maze import Maze
from genetic_algorithm import GeneticAlgorithm

# Definición de la cuadrícula del laberinto, punto de inicio y final
grid = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
end = (4, 4)

# Crear instancia de Maze y GeneticAlgorithm
maze = Maze(grid, start, end)
ga = GeneticAlgorithm(maze,50,0.7,0.1) #population_size=50, crossover_rate=0.7, mutation_rate=0.1
# Ejecutar el algoritmo genético
ga.evolve(20)

#----------------------------------------------------------------------
print('---------------------------------------------------------------------')
print('')

print('Pruebas con diferentes valores de probabilidades de cruce y mutación')
# Funcion que nos permite asignar los valores de probabilidades de cruce y mutación para realizar pruebas
def test_with_varying_parameters(maze, population_size, crossover_rate, mutation_rate, generations):
    ga = GeneticAlgorithm(maze, population_size=population_size, crossover_rate=crossover_rate, mutation_rate=mutation_rate)  # Población más pequeña
    ga.evolve(generations)  # Menos generaciones
    print("\n--------------------------------------\n")

# Ejemplo de laberinto 5x5 (denso)
dense_grid_small = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 1]
]

start_small = (1, 1)
end_small = (3, 4)

# Crear una instancia del laberinto
maze_small = Maze(dense_grid_small, start_small, end_small)

# Probar con diferentes combinaciones de crossover_rate y mutation_rate
print('Prueba 1:')
test_with_varying_parameters(maze_small, 50, 0.7,0.1, 10)
print('Prueba 2:')
test_with_varying_parameters(maze_small, 50, 0.5,0.2, 10)
print('Prueba 3:')
test_with_varying_parameters(maze_small, 50, 0.5,0.5, 10)
