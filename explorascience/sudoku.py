import pygame as py
import tkinter as tk
from tkinter import messagebox
import os


def start():
    print(f'You choose the game Sudoku')
    input_grid()

def input_grid():
    grid_dic = {}

    grid_window = tk.Tk()
    grid_window.title('Input the grid')
    grid_window.geometry('255x198')

    for i in range(9):
        for j in range(9):
            name = f'{i}{j}'
            entry = tk.Entry(grid_window, width=4)
            entry.grid(row=i, column=j)
            grid_dic[name] = entry

    def validate():
        grid = [[0 for _ in range(9)] for _ in range(9)]
        for key in grid_dic.keys():
            i = int(key[0])
            j = int(key[1])
            data = grid_dic[key].get()
            if data:
                grid[i][j] = data

        grid_window.destroy()
        solve(grid)

    validate = tk.Button(grid_window, command=validate, text="Validate")
    validate.grid(row=11, column=3, columnspan=3)

def solve(grid):
    pass