import pygame
import random

WIDTH, HEIGHT = 800, 800
CELL_SIZE = 20
ROWS = (HEIGHT - 1) // CELL_SIZE
COLS = (WIDTH - 1) // CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SCORE = 10000

class Maze:
    def __init__(self):
        self.grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.generate_maze()
        self.start = (1, 1)
        self.end = (ROWS - 2, COLS - 2)

    def generate_maze(self):
        cell_list = [(1, 1)]
        while cell_list:
            x, y = cell_list[-1]
            self.grid[y][x] = 1
            neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
            neighbors = [(nx, ny) for nx, ny in neighbors if 0 < nx < COLS-1 and 0 < ny < ROWS-1 and self.grid[ny][nx] == 0]
            if neighbors:
                nx, ny = random.choice(neighbors)
                self.grid[(y + ny) // 2][(x + nx) // 2] = 1
                cell_list.append((nx, ny))
            else:
                cell_list.pop()

    def draw(self, screen):
        for y in range(ROWS):
            for x in range(COLS):
                if self.grid[y][x] == 1:
                    pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, (self.end[0] * CELL_SIZE, self.end[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Player:

def main():


if __name__ == "__main__":
    main()