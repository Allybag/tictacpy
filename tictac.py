import tkinter as tk

# notation is a list of moves played
notation = []

# This class defines a Square, just a clickable canvas which shows a nought or cross when clicked
class Square(tk.Canvas):
	def __init__(self, name, master=None, width=None, height=None):
		super().__init__(master, width=width, height=height)
		self.bind("<Button-1>", self.tic)
		self.bind("<Button-2>", self.tac)
		self.config(highlightbackground="Black")
		self.config(highlightthickness=1)
		self.free=True
		self.name=name
	

	def tic(self, event):
		""""This will draw a cross on the selected Square."""
		if self.free:
			self.create_line(30, 30, 170, 170)
			self.create_line(30, 170, 170, 30)
			self.free = False
			global notation
			notation.append(self)
			print([m.name for m in notation])

	def tac(self, event):
		""""This will draw a nought on the selected Square."""
		if self.free:
			self.create_oval(30, 30, 170, 170)
			self.free = False
			global notation
			notation.append(self)
			print([m.name for m in notation])

	def clear(self):
		""""This will clear the selected Square."""
		if not self.free:
			self.delete("all")
			self.free = True
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
fileMenu.add_command(label="Undo", command=lambda: notation.pop().clear())

root.mainloop()
