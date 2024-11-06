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
            if not self.maze.is_free(position):

                return 0
        return 1

    def selection(self):
        """
        Selecciona padres para la reproducción mediante el método de ruleta.
        Retorna dos caminos seleccionados como padres.
        """
        total_fitness = sum(self.fitness(path) for path in self.population)
        pick = random.uniform(0, total_fitness)
        current = 0
        for path in self.population:
            current += self.fitness(path)
            if current > pick:
                return path
        return self.population[-1]

    def crossover(self, parent1, parent2):
        """
        Realiza el cruce entre dos caminos.
        parent1, parent2: caminos padres
        Retorna dos caminos hijos.
        """
        if random.random() > self.crossover_rate:
            return parent1, parent2  # No cruce
        cut = random.randint(1, min(len(parent1), len(parent2)) - 1)
        child1 = parent1[:cut] + parent2[cut:]
        child2 = parent2[:cut] + parent1[cut:]
        return child1, child2
    
    def mutate(self, path):
        """
        Realiza la mutación en un camino.
        path: camino a mutar
        Retorna un camino mutado.
        """
        if random.random() < self.mutation_rate:
            pos = random.randint(1, len(path) - 2)
            neighbors = self.maze.get_neighbors(path[pos])
            if neighbors:
                path[pos] = random.choice(neighbors)
        return path

    def evolve(self, generations):
        """
        Evoluciona la población durante un número de generaciones.
        generations: número de generaciones
        """
        for _ in range(generations):
            new_population = []
            for _ in range(self.population_size // 2):
                parent1 = self.selection()
                parent2 = self.selection()
                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                new_population.extend([child1, child2])
            self.population = sorted(new_population, key=lambda p: -self.fitness(p))[:self.population_size]
            best_path = max(self.population, key=self.fitness)
            print(f"Mejor camino: {best_path}, Fitness: {self.fitness(best_path)}")