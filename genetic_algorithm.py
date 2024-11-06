import random

class GeneticAlgorithm:
    def __init__(self, maze, population_size, crossover_rate, mutation_rate):
        self.maze = maze 
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.population = self._initialize_population()
    
    def _initialize_population(self):
        """
        Genera una población inicial aleatoria.
        Retorna una lista de caminos (cada camino es una lista de posiciones).
        """
        population = []
        for _ in range(self.population_size):
            path = self._generate_random_path()
            population.append(path)
        return population
    
    def _generate_random_path(self):
        """
        Genera un camino aleatorio desde el inicio hasta el final.
        Retorna una lista de posiciones.
        """
        path = [self.maze.start]
        current_position = self.maze.start
        while current_position != self.maze.end:
            neighbors = self.maze.get_neighbors(current_position)
            current_position = random.choice(neighbors)
            path.append(current_position)
        return path
    
    def fitness(self, path):
        """
        Calcula el fitness de un camino.
        path: lista de posiciones que representa el camino
        Retorna un valor de fitness basado en la factibilidad, longitud y cantidad de giros.
        """
        length = len(path)  # Minimizar la longitud
        turns = self._count_turns(path)  # Minimizar los giros
        feasibility = self._check_feasibility(path)  # Penalización si cruza obstáculos

        # Ponderaciones
        weight_length = 1
        weight_turns = 2
        weight_feasibility = 3

        return weight_feasibility * feasibility + weight_length * (1 / length) + weight_turns * (1 / (turns + 1))
    
    def _count_turns(self, path):
        """
        Cuenta la cantidad de giros en el camino.
        path: lista de posiciones
        Retorna el número de giros en el camino.
        """
        turns = 0
        for i in range(2, len(path)):
            prev_direction= (path[i-1][0]-path[i-2][0], path[i-1][1]- path[i-2][1])
            current_direction = (path[i][0]-path[i-1][0], path[i][1]-path[i-1][1])
            if prev_direction != current_direction:
                turns += 1
        return turns
    def _check_feasibility(self, path):
        """
        Verifica si un camino es factible (no cruza obstáculos).
        path: lista de posiciones
        Retorna 1 si el camino es factible, 0 en caso contrario.
        """
        for position in path:
            if self.maze.is_obstacle(position):
                return 0
        return 1

