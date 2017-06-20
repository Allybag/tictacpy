import tkinter as tk

class Square(tk.Canvas):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
	

	def tic(self, event):
		""""This will draw a nought or cross on the selected Square."""
		self.create_line(0, 0, 200, 100)

root = tk.Tk()
square = Square(master=root)
square.bind("<Button-1>", lambda event: Square.tic(square, event))
root.mainloop()
