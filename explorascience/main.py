import tkinter as tk
import tictactoe as ttt
import sudoku as sd
import connect_4 as cf


def choose_game():
    window = tk.Tk()
    window.geometry('450x110')

    window.title("Choose window")
    tictac = tk.Button(window, text="Tic-Tac-Toe", command=ttt.start, width=20, height=5)
    confour = tk.Button(window, text="Connect 4", command=cf.start, width=20, height=5)
    sudoku = tk.Button(window, text="Sudoku", command=sd.start, width=20, height=5)
    close = tk.Button(window, text="Close", command=window.destroy)

    tictac.grid(row=0, column=0)
    confour.grid(row=0, column=1)
    sudoku.grid(row=0, column=2)
    close.grid(row=2, column=1)

    window.mainloop()


if __name__ == '__main__':
    choose_game()
