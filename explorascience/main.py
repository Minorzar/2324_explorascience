import tkinter as tk
import tictactoe as ttt
import sudoku as sd
import connect_4 as cf
from extract_double import extract


def choose_game():
    window = tk.Tk()
    window.geometry('450x85')

    def set_flag(value):
        match value:
            case 0:
                window.destroy()
                ttt.start()
            case 1:
                window.destroy()
                cf.start()
            case 2:
                window.destroy()
                sd.start()
            case _:
                pass

    window.title("Choose window")
    tictac = tk.Button(window, text="Tic-Tac-Toe", command=lambda: set_flag(0), width=20, height=5)
    confour = tk.Button(window, text="Connect 4", command=lambda: set_flag(1), width=20, height=5)
    sudoku = tk.Button(window, text="Sudoku", command=lambda: set_flag(2), width=20, height=5)

    tictac.grid(row=0, column=0)
    confour.grid(row=0, column=1)
    sudoku.grid(row=0, column=2)

    window.mainloop()


if __name__ == '__main__':
    choose_game()