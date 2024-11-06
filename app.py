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