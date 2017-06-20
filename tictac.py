import tkinter as tk

# This class defines a Square, just a clickable canvas which shows a nought or cross when clicked
class Square(tk.Canvas):
	def __init__(self, master=None, width=None, height=None):
		super().__init__(master, width=width, height=height)
		self.bind("<Button-1>", self.tic)
		self.bind("<Button-2>", self.tac)
	

	def tic(self, event):
		""""This will draw a cross on the selected Square."""
		self.create_line(30, 30, 170, 170)
		self.create_line(30, 170, 170, 30)

	def tac(self, event):
		""""This will draw a nought on the selected Square."""
		self.create_oval(30, 30, 170, 170)

root = tk.Tk()
root.title("Tic Tac Toe")

NW = Square(master=root, width=200, height=200)
NW.grid(row=0, column=0)

N = Square(master=root, width=200, height=200)
N.grid(row=0, column=1)

NE = Square(master=root, width=200, height=200)
NE.grid(row=0, column=2)

W = Square(master=root, width=200, height=200)
W.grid(row=1, column=0)

C = Square(master=root, width=200, height=200)
C.grid(row=1, column=1)

E = Square(master=root, width=200, height=200)
E.grid(row=1, column=2)

SW = Square(master=root, width=200, height=200)
SW.grid(row=2, column=0)

S = Square(master=root, width=200, height=200)
S.grid(row=2, column=1)

SE = Square(master=root, width=200, height=200)
SE.grid(row=2, column=2)

root.mainloop()
