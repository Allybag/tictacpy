import tkinter as tk

class Square(tk.Canvas):
	def __init__(self, master=None, width=None, height=None):
		super().__init__(master, width=width, height=height)
		self.pack()
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
square = Square(master=root, width=200, height=200)
root.mainloop()
