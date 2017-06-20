import tkinter as tk

# notation is a list containing all moves made
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
			notation.append(self.name)
			print(notation)

	def tac(self, event):
		""""This will draw a nought on the selected Square."""
		if self.free:
			self.create_oval(30, 30, 170, 170)
			self.free = False
			global notation
			notation.append(self.name)
			print(notation)

root = tk.Tk()
root.title("Tic Tac Toe")

NW = Square("NW", master=root, width=200, height=200)
NW.grid(row=0, column=0)

N = Square("N", master=root, width=200, height=200)
N.grid(row=0, column=1)

NE = Square("NE", master=root, width=200, height=200)
NE.grid(row=0, column=2)

W = Square("W", master=root, width=200, height=200)
W.grid(row=1, column=0)

C = Square("C", master=root, width=200, height=200)
C.grid(row=1, column=1)

E = Square("E", master=root, width=200, height=200)
E.grid(row=1, column=2)

SW = Square("SW", master=root, width=200, height=200)
SW.grid(row=2, column=0)

S = Square("S", master=root, width=200, height=200)
S.grid(row=2, column=1)

SE = Square("SE", master=root, width=200, height=200)
SE.grid(row=2, column=2)

root.mainloop()
