import pygame
import math
from sudoku import grid, gui
import time



DIM = 9
CELL_W = 50
CELL_H = 50
X_OFFSET = 30
Y_OFFSET = 100

new_gui = None
isValidGrid = grid.isValidGrid
Grid = grid.Grid

def start():
    global new_gui
    print(f'You choose the game Sudoku')
    new_gui = gui.GUI()
    play()


def play():
    global new_gui

    SOLVING = False
    SOLVED = False
    GRID = None

    while True:

        if not SOLVING:

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos

                    cell_row = math.floor((mouse_y - Y_OFFSET) / CELL_H)
                    cell_column = math.floor((mouse_x - X_OFFSET) / CELL_W)

                    if 0 <= cell_row < DIM and 0 <= cell_column < DIM:
                        new_gui.grid_cells[cell_row][cell_column].update_value()

                    elif new_gui.button_rec.collidepoint(event.pos):
                        SOLVING = True

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        if SOLVING:

            new_gui.clearSpace()

            if not isValidGrid(new_gui.grid_cells):  # Check prefilled values
                new_gui.showError()
                pygame.display.update()
                time.sleep(3)

                new_gui.showButton()
                SOLVING = False
                pygame.display.update()

            else:

                GRID = Grid(new_gui.grid_cells)  # Once the grid is correct, initalise the grid object
                GRID.setEntropy()  # Set initial entropy from user set values

            if GRID:
                SOLVED = GRID.solve(new_gui.screen)  # COllapse the grid cell by cell
                SOLVING = False

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        if SOLVED:
            new_gui.showSolved()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        if GRID is None:
            for i in range(DIM):
                for j in range(DIM):  # Keep updating and displaying grid values until user click solve
                    new_gui.grid_cells[i][j].show(new_gui.screen)

        pygame.display.update()