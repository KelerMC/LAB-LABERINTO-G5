# Clase Maze para definir la cuadrícula del laberinto
class Maze:
    def __init__(self, grid, start, end):
        """
        Inicializa el laberinto.
        grid: matriz que representa el laberinto (0 = celda libre, 1 = obstáculo)
        start: coordenadas de inicio (fila, columna)
        end: coordenadas del objetivo (fila, columna)
        """
        self.grid = grid
        self.start = start
        self.end = end
        self.rows = len(grid)
        self.cols = len(grid[0])

    def is_free(self, position):
        """
        Verifica si una posición en el laberinto está libre.
        position: tupla (fila, columna)
        Retorna True si la celda es libre, de lo contrario False.
        """
        r, c = position
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 0

    def get_neighbors(self, position):
        """
        Obtiene los vecinos de una posición que son accesibles.
        position: tupla (fila, columna)
        Retorna una lista de posiciones vecinas libres.
        """
        r, c = position
        neighbors = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]  # Arriba, Abajo, Izquierda, Derecha
        return [n for n in neighbors if self.is_free(n)]
    
    def is_obstacle(self, position):
        r, c = position
        return 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == 1