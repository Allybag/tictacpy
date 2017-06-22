import tkinter as tk

# notation is a list of moves played
notation = []

# This class defines a Square, just a clickable canvas which shows a nought or cross when clicked
class Square(tk.Canvas):

	# Cross starts
	crossToPlay = True

	def __init__(self, name, master=None, width=None, height=None):
		super().__init__(master, width=width, height=height)
		self.bind("<Button-1>", self.tic)
		self.config(highlightbackground="Black")
		self.config(highlightthickness=1)
		self.free = True
		self.name = name

	def draw(self):
		"""This will draw a nought or cross on itself,
		depending on who is to play."""
		if Square.crossToPlay:
			self.create_line(30, 30, 170, 170)
			self.create_line(30, 170, 170, 30)
		else:
			self.create_oval(30, 30, 170, 170)
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

for i, name in enumerate('NW N NE W C E SW S SE'.split()):
    s = Square(name, master=root, width=200, height=200)
    row, column = divmod(i, 3)
    s.grid(row=row, column=column)

# Creating File Menu
menu = tk.Menu(root)
root.config(menu=menu)

fileMenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
# Undo calls the clear function on the most recently played square.
fileMenu.add_command(label="Undo", command=lambda: notation.pop().clear())

root.mainloop()
