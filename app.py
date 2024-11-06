import pygame
import random
import time
from maze import Maze
from genetic_algorithm import GeneticAlgorithm

# Definición de la cuadrícula del laberinto, punto de inicio y final
grid = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
end = (4, 4)

# Parámetros de visualización
CELL_SIZE = 40
GRID_WIDTH = len(grid[0])
GRID_HEIGHT = len(grid)

# Inicializar pygame
pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
pygame.display.set_caption("Visualización del Algoritmo Genético en el Laberinto")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Crear instancia de Maze y GeneticAlgorithm
maze = Maze(grid, start, end)
ga = GeneticAlgorithm(maze, population_size=50, crossover_rate=0.7, mutation_rate=0.1)

# Función para dibujar el laberinto
def draw_maze():
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            color = WHITE if maze.is_free((row, col)) else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    # Dibujar el punto de inicio y el final
    pygame.draw.rect(screen, GREEN, (start[1] * CELL_SIZE, start[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (end[1] * CELL_SIZE, end[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Función para dibujar el camino actual
def draw_path(path, color=BLUE):
    for position in path:
        pygame.draw.rect(screen, color, (position[1] * CELL_SIZE, position[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Ejecutar y visualizar el algoritmo genético
def run_genetic_algorithm(ga, generations):
    for generation in range(generations):
        screen.fill(WHITE)
        draw_maze()

        # Evolucionar una generación
        ga.evolve(1)

        # Obtener el mejor camino de la generación actual
        best_path = max(ga.population, key=ga.fitness)

        # Dibujar el camino explorado por la población en amarillo
        for path in ga.population:
            draw_path(path, color=YELLOW)

        # Dibujar el mejor camino en azul
        draw_path(best_path, color=BLUE)
        
        # Redibujar el punto de inicio y final para que no queden cubiertos
        pygame.draw.rect(screen, GREEN, (start[1] * CELL_SIZE, start[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, (end[1] * CELL_SIZE, end[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        
        pygame.display.flip()

        # Mostrar la generación y el fitness en consola
        print(f"Generación {generation + 1}: Mejor camino encontrado {best_path} con fitness {ga.fitness(best_path)}")
        
        # Esperar un tiempo para visualizar cada generación
        time.sleep(0.5)
     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

    # Mantener la ventana abierta después de completar las generaciones
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False

# Correr el algoritmo genético con visualización
run_genetic_algorithm(ga, 20)

# Cerrar pygame después de ejecutar el algoritmo
pygame.quit()
