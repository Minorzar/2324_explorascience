import tkinter as tk
from tkinter import messagebox


mat = turn = buttons = totTurn = win = winner_window = None

def start():
    global mat, turn, buttons, totTurn

    mat = [["", "", ""] for _ in range(3)]
    turn = 0
    buttons = []
    totTurn = 1

    print(f'You have choosen the game Tic-Tac-Toe !')

    turn_select()

def turn_select():
    turn_window = tk.Tk()
    turn_window.title('Choose Turn')
    turn_window.geometry('250x100')

    label = tk.Label(turn_window, text='Choose the starting turn:')
    label.pack(pady=10)

    def set_turn(turn_value):
        global turn
        turn = turn_value
        turn_window.destroy()
        window()

    button0 = tk.Button(turn_window, text='Player 1 (X)', command=lambda: set_turn(0))
    button1 = tk.Button(turn_window, text='Player 2 (O)', command=lambda: set_turn(1))

    button0.pack(side=tk.LEFT, padx=20)
    button1.pack(side=tk.RIGHT, padx=20)

    turn_window.mainloop()

def restart():
    global mat, turn, buttons, totTurn, winner_window

    winner_window.destroy()

    mat = [["", "", ""] for _ in range(3)]
    turn = 0
    totTurn = 1
    buttons = []

    turn_select()

def update(mat):
    global buttons, turn

    for i in range(3):
        for j in range(3):
            value = mat[i][j]
            if value == "X":
                buttons[i][j].config(text="✕", state=tk.DISABLED)
            elif value == "O":
                buttons[i][j].config(text="◯", state=tk.DISABLED)
            else:
                buttons[i][j].config(text="", state=tk.NORMAL)

    game_end(mat)

def game_end(mat):
    global turn, totTurn

    for i in range(3):
        if ((mat[i][0] == mat[i][1] == mat[i][2]) or (mat[0][i] == mat[1][i] == mat[2][i])) and mat[i][i]:
            winner(turn)

    if ((mat[0][0] == mat[1][1] == mat[2][2]) or (mat[0][2] == mat[1][1] == mat[2][0])) and mat[1][1]:
        winner(turn)

    if totTurn == 9:
        winner(-1)

    turn = (turn + 1) % 2
    totTurn += 1


def game(mat, i, j, turn):
    if turn == 0:
        mat[i][j] = "X"
    else:
        mat[i][j] = "O"

    update(mat)


def window():
    global mat, turn, buttons, win

    win = tk.Tk()
    win.title('Tic-Tac-Toe')
    win.geometry('420x400')

    buttons = [[None, None, None] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(win, width=7, height=3, font=('Arial', 24), command=lambda i=i, j=j: game(mat, i, j, turn))
            buttons[i][j].grid(row=i, column=j)

    win.mainloop()

def winner(player):
    global win, winner_window

    win.destroy()

    winner_window = tk.Tk()
    winner_window.title('Winner')
    winner_window.geometry('250x150')

    if player == -1:
        message = "Draw !"
    else:
        message = f"Player {player + 1} won !"

    winner_label = tk.Label(winner_window, text=message, font=('Helvetica', 16))
    winner_label.pack(pady=20)

    replay_button = tk.Button(winner_window, text="Replay ?", command=restart)
    replay_button.pack()

    close_button = tk.Button(winner_window, text="Close", command=winner_window.destroy)
    close_button.pack()

    winner_window.mainloop()
