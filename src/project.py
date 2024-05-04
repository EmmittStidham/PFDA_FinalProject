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

class Player:

def main():


if __name__ == "__main__":
    main()