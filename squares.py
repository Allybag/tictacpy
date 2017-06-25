import tkinter as tk
import numpy as np

class Square(tk.Canvas):
	"""A Square is a canvas on which nought or cross can be played"""

	# Cross starts
	crossToPlay = True
	# moveList and state are both representations of the board
	moveList = []
	state = np.zeros((3, 3))

	def __init__(self, name, master=None, size=None):
		super().__init__(master, width=size, height=size)
		self.bind("<Button-1>", self.tic)
		self.config(highlightbackground="Black")
		self.config(highlightthickness=1)
		self.symbol = None
		self.name = name
		self.topLeft = size * 0.15
		self.bottomRight = size * 0.85
		self.gr = tuple(np.subtract(self.name, (1,1)))

	def draw(self):
		"""This will draw a nought or cross on itself,
		depending on who is to play."""
		tl = self.topLeft
		br = self.bottomRight
		if Square.crossToPlay:
			self.create_line(tl, tl, br, br)
			self.create_line(tl, br, br, tl)
			self.symbol = 'X'
			self.state[self.gr] = 1
		else:
			self.create_oval(tl, tl, br, br)
			self.symbol = 'O'
			self.state[self.gr] = 4

	def tic(self, event):
		""""This draws the relevant move, marks the square as played,
		sets the next symbol to play, and records the move order."""
		if not self.symbol:
			self.draw()
			Square.crossToPlay = not Square.crossToPlay
			self.moveList.append(self)
			self.print()
			self.winCheck()


	def clear(self):
		""""This will clear the selected Square."""
		if self.symbol:
			self.delete("all")
			self.symbol = None
			Square.crossToPlay = not Square.crossToPlay
			self.print()
			self.state[self.gr] = 0

	@classmethod
	def undo(cls):
		cls.moveList.pop().clear()

	@classmethod
	def print(cls):
		print('Moves:', *[square.name for square in cls.moveList])

	@staticmethod
	def winCheck():
		winNums = list(Square.state.sum(axis=0))
		winNums.extend(list(Square.state.sum(axis=1)))
		winNums.append(Square.state.trace())
		winNums.append(np.flipud(Square.state).trace())
		
		if 3 in winNums:
			print("Victory for X!")

		if 12 in winNums:
			print("Victory for O!")
