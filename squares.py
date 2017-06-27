import tkinter as tk
import numpy as np
import gamecfg

class Square(tk.Canvas):
	"""A Square is a canvas on which nought or cross can be played"""

	# Number of squares
	m = gamecfg.n

	# Cross starts, and the game has no result yet
	crossToPlay = True
	result = None

	# moveList and state are both representations of the board
	moveList = []
	state = np.zeros((m, m))

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
			Square.state[self.gr] = 1
		else:
			self.create_oval(tl, tl, br, br)
			self.symbol = 'O'
			Square.state[self.gr] = Square.m + 1

	def tic(self, event):
		""""This draws the relevant move, marks the square as played,
		sets the next symbol to play, and records the move order."""
		if not self.symbol and not self.result:
			self.draw()
			Square.crossToPlay = not Square.crossToPlay
			Square.moveList.append(self)
			Square.print()
			Square.winCheck()


	def clear(self):
		""""This will clear the selected Square."""
		if self.symbol:
			self.delete("all")
			self.symbol = None
			Square.result = None
			Square.crossToPlay = not Square.crossToPlay
			Square.print()
			Square.state[self.gr] = 0

	@classmethod
	def undo(cls):
		cls.moveList.pop().clear()

	@classmethod
	def print(cls):
		print('Moves:', *[square.name for square in cls.moveList])

	@staticmethod
	def winCheck():
		# Sums which correspond to a line across a column
		winNums = list(Square.state.sum(axis=0))
		# Sums which correspond to a line across a row
		winNums.extend(list(Square.state.sum(axis=1)))
		# Sums which correspond to a line across the main diagonal
		winNums.append(Square.state.trace())
		# Sums which correspond to a line across the off diagonal
		winNums.append(np.flipud(Square.state).trace())
		
		if Square.m in winNums:
			print("Victory for X!")
			Square.result = 1
		elif (Square.m**2 + Square.m) in winNums:
			print("Victory for O!")
			Square.result = -1
		elif np.count_nonzero(Square.state) == Square.m**2:
			print("It's a draw!")
			Square.result = 0
