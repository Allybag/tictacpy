import tkinter as tk
import numpy as np
from squares import Square

root = tk.Tk()
root.title("Tic Tac Toe")

# Creating the board, 600 x 600 pixels, n squares across
m = Square.n
size = 600 // m
squares = [(rank, file) for rank in range(1, m + 1) for file in range(1, m + 1)]

for (rank, file) in squares:
	square = Square((rank, file), master=root, size=size)
	square.grid(row=rank, column=file)

# Checking for a win

# Creating File Menu
menu = tk.Menu(root)
root.config(menu=menu)

fileMenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
# Undo calls the clear function on the most recently played square.
fileMenu.add_command(label="Undo", command=lambda: Square.moveList.pop().clear())
fileMenu.add_command(label="State", command=lambda: print(Square.state))
fileMenu.add_command(label="Result", command=lambda: print(Square.result))

root.mainloop()
