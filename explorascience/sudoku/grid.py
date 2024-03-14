import math
import random
import time
import copy
from threading import Thread, Event

import pygame.display

DIM = 9
FRAME_TIME = 0.02


class Grid:
    def __init__(self, grid):
        self.OriginalGrid = grid
        self.CopyGrid = copy.deepcopy(self.OriginalGrid)

    def displayGrid(self, screen, evt):
        while True:
            if evt.isSet():
                return ()
            for i in range(DIM):
                for j in range(DIM):
                    self.CopyGrid[i][j].show(screen)

            pygame.display.update()

    def solve(self, screen):

        e = Event()
        display_thread = Thread(target=self.displayGrid, args=[screen, e])  # Avoid unresponsivity
        display_thread.start()

        while self.notSolved():
            success = self.waveFunction_collapse()
            if success:
                time.sleep(FRAME_TIME)
            else:
                print("Solving failed. Resetting")
                self.reset()

        e.set()
        display_thread.join()
        return True

    def notSolved(self):

        for i in range(DIM):
            for j in range(DIM):
                if self.CopyGrid[i][j].collapsed is False:
                    return True

        return False

    def waveFunction_collapse(self):
        min_options = math.inf
        for i in range(DIM):
            for j in range(DIM):
                if not self.CopyGrid[i][j].collapsed:
                    min_options = min(min_options, len(self.CopyGrid[i][j].options))

        least_entropy_cells = []
        for i in range(DIM):
            for j in range(DIM):
                if not self.CopyGrid[i][j].collapsed:
                    if len(self.CopyGrid[i][j].options) == min_options:
                        self.CopyGrid[i][j].highlight = True
                        least_entropy_cells.append(self.CopyGrid[i][j])

        if len(least_entropy_cells) > 0:
            random_cell = random.choice(least_entropy_cells)

            if len(random_cell.options) == 0:
                return False

            random_cell.collapse()

            self.reduce_entropy(random_cell)
            return True

    def reduce_entropy(self, cell):
        row = cell.row
        column = cell.column
        block = cell.block
        pick = cell.options[0]

        for i in range(DIM):
            for j in range(DIM):
                if self.CopyGrid[i][j] != cell and self.CopyGrid[i][j].collapsed is False:

                    if self.CopyGrid[i][j].row == row:
                        if pick in self.CopyGrid[i][j].options:
                            self.CopyGrid[i][j].options.remove(pick)

                    if self.CopyGrid[i][j].column == column:
                        if pick in self.CopyGrid[i][j].options:
                            self.CopyGrid[i][j].options.remove(pick)

                    if self.CopyGrid[i][j].block == block:
                        if pick in self.CopyGrid[i][j].options:
                            self.CopyGrid[i][j].options.remove(pick)

    def setEntropy(self):
        input_cells = []

        for i in range(DIM):
            for j in range(DIM):
                if self.CopyGrid[i][j].value != 0:
                    input_cells.append(self.CopyGrid[i][j])

        if len(input_cells) > 0:
            for cell in input_cells:
                value = cell.value
                cell.collapse(value)
                self.reduce_entropy(cell)

    def reset(self):
        self.CopyGrid = copy.deepcopy(self.OriginalGrid)  # Reset grid
        self.setEntropy()  # Reset entropy


def isValidGrid(grid):
    input_cells = []

    for i in range(DIM):
        for j in range(DIM):
            if grid[i][j].value != 0:
                input_cells.append(grid[i][j])

    for cell in input_cells:
        if check_RowsColsBlocks(cell, grid) is False:
            return False

    return True


def check_RowsColsBlocks(cell, grid):
    row = cell.row
    column = cell.column
    block = cell.block
    value = cell.value

    for i in range(DIM):
        for j in range(DIM):
            if grid[i][j] != cell:
                if grid[i][j].row == row or grid[i][j].column == column or grid[i][j] == block:
                    if grid[i][j].value == value:
                        return False
    return True