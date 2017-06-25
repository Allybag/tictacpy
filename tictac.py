import tkinter as tk


class Square(tk.Canvas):
	"""A Square is a canvas on which nought or cross can be played"""

	# Cross starts
	crossToPlay = True
	moveList = []

	def __init__(self, name, master=None, size=None):
		super().__init__(master, width=size, height=size)
		self.bind("<Button-1>", self.tic)
		self.config(highlightbackground="Black")
		self.config(highlightthickness=1)
		self.symbol = None
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
			self.symbol = 'X'
		else:
			self.create_oval(tl, tl, br, br)
			self.symbol = 'O'

	def tic(self, event):
		""""This draws the relevant move, marks the square as played,
		sets the next symbol to play, and records the move order."""
		if not self.symbol:
			self.draw()
			Square.crossToPlay = not Square.crossToPlay
			self.moveList.append(self)
			self.print()


	def clear(self):
		""""This will clear the selected Square."""
		if self.symbol:
			self.delete("all")
			self.symbol = None
			Square.crossToPlay = not Square.crossToPlay
			self.print()

	@classmethod
	def undo(cls):
		cls.moveList.pop().clear()

	@classmethod
	def print(cls):
		print('Moves:', *[square.name for square in cls.moveList])

root = tk.Tk()
root.title("Tic Tac Toe")

# Creating the board, 600 x 600 pixels, n squares across
n = 3
size = 600 // n
squares = [(rank, file) for rank in range(1, n + 1) for file in range(1, n + 1)]

for (rank, file) in squares:
	square = Square((rank, file), master=root, size=size)
	square.grid(row=rank, column=file)

	# Work out which square is opposite the current square
	square.targets=[]
	if rank in (1, n):
		square.targets.append(((n + 1 - rank), file))
	if file in (1, n):
		square.targets.append((rank, (n + 1 -file)))
	if rank in (1, n) and file in (1, n):
		square.targets.append(((n + 1 - rank), (n + 1 -file)))

# Checking for a win



# Creating File Menu
menu = tk.Menu(root)
root.config(menu=menu)

fileMenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
# Undo calls the clear function on the most recently played square.
fileMenu.add_command(label="Undo", command=lambda: Square.moveList.pop().clear())

root.mainloop()
