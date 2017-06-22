import tkinter as tk

# notation is a list of moves played
notation = []

class Square(tk.Canvas):
	"""A Square is a canvas on which nought or cross can be played"""

	# Cross starts
	crossToPlay = True

	def __init__(self, name, master=None, size=None):
		super().__init__(master, width=size, height=size)
		self.bind("<Button-1>", self.tic)
		self.config(highlightbackground="Black")
		self.config(highlightthickness=1)
		self.free = True
		self.name = name
		self.topLeft = size * 0.15
		self.bottomRight = size * 0.85

	def draw(self):
		"""This will draw a nought or cross on itself,
		depending on who is to play."""
		tl = self.topLeft
		br = self.bottomRight
		if Square.crossToPlay:
			self.create_line(tl, tl, br, br)
			self.create_line(tl, br, br, tl)
		else:
			self.create_oval(tl, tl, br, br)
			self.free = False

	def tic(self, event):
		""""This draws the relevant move, marks the square as played,
		sets the next symbol to play, and records the move order."""
		if self.free:
			self.draw()
			self.free = False
			Square.crossToPlay = not Square.crossToPlay
			global notation
			notation.append(self)
			print([m.name for m in notation])


	def clear(self):
		""""This will clear the selected Square."""
		if not self.free:
			self.delete("all")
			self.free = True
			Square.crossToPlay = not Square.crossToPlay
			global notation
			print([m.name for m in notation])

root = tk.Tk()
root.title("Tic Tac Toe")

# Creating the board, 600 x 600 pixels, n squares across
n = 3
size = 600 // n
squares = [(rank, file) for rank in range(1, n + 1) for file in range(1, n + 1)]

for (rank, file) in squares:
	square = Square((rank, file), master=root, size=size)
	square.grid(row=rank, column=file)

# Creating File Menu
menu = tk.Menu(root)
root.config(menu=menu)

fileMenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
# Undo calls the clear function on the most recently played square.
fileMenu.add_command(label="Undo", command=lambda: notation.pop().clear())

root.mainloop()
