import tkinter as tk
import random
import numpy as np
import gamecfg


# The main class
class Square(tk.Canvas):
	"""A Square is a canvas on which nought or cross can be played"""

	# Cross starts, board of length m, and the game has no result yet
	crossToPlay = True
	result = None
	m = gamecfg.n

	# moveList, squareDict and state are all representations of the board
	moveList = []
	squareDict = {}
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
		# Add itself to the dict of squares
		Square.squareDict[self.name] = self

	def draw(self):
		"""This will draw a nought or cross on itself,
		depending on who is to play."""
		if not self.symbol and not self.result:
			tl = self.topLeft
			br = self.bottomRight
			if Square.crossToPlay:
				self.create_line(tl, tl, br, br)
				self.create_line(tl, br, br, tl)
				self.symbol = 'X'
				Square.state[self.name] = 1
			else:
				self.create_oval(tl, tl, br, br)
				self.symbol = 'O'
				Square.state[self.name] = Square.m + 1
			Square.crossToPlay = not Square.crossToPlay
			Square.moveList.append(self)
			Square.print()
			Square.setResult(winCheck(Square.state))

	def tic(self, event):
		""""A tic is a player clicking on a square"""
		self.draw()
		computerMove()

	def tac(self):
		"""A tac is the computer playing"""
		self.master.update()
		self.after(gamecfg.engineWait, self.draw())



	def clear(self):
		""""This will clear the selected Square."""
		if self.symbol:
			self.delete("all")
			self.symbol = None
			Square.result = None
			Square.crossToPlay = not Square.crossToPlay
			Square.print()
			Square.state[self.name] = 0

	@classmethod
	def undo(cls):
		cls.moveList.pop().clear()

	@classmethod
	def print(cls):
		print('Moves:', *[square.name for square in cls.moveList])

	@classmethod
	def setResult(cls, result):
		if result:
			cls.result = result	
			print("Result: {}".format(result))


def winCheck(state):
	"""Takes a position, and returns the outcome of that game"""
	# Sums which correspond to a line across a column
	winNums = list(state.sum(axis=0))
	# Sums which correspond to a line across a row
	winNums.extend(list(state.sum(axis=1)))
	# Sums which correspond to a line across the main diagonal
	winNums.append(state.trace())
	# Sums which correspond to a line across the off diagonal
	winNums.append(np.flipud(state).trace())

	if Square.m in winNums:
		return 'X'
	elif (Square.m**2 + Square.m) in winNums:
		return 'O'
	elif np.count_nonzero(state) == Square.m**2:
		return 'D'
	else:
		return None

def moveFind(state):
	"""Takes a position as an nparray and determines the legal moves"""
	moveChoices = []

	# Iterate over state, to determine which squares are empty
	it = np.nditer(state, flags=['multi_index'])
	while not it.finished:
		if it[0] == 0:
			moveChoices.append(it.multi_index)
		it.iternext()
	return moveChoices

def moveSim(state, move, player):
	"""Create the state of the player having moved without interfering with the board"""
	simState = state.copy()
	if player == 1:
		simState[move] = 1
	else:
		simState[move] = gamecfg.n + 1
	return simState

def positionScore(state):
	"""The game is either won or lost"""
	if winCheck(state) == 'X':
		return 100 - np.count_nonzero(state)
	elif winCheck(state) == 'O':
		return -100 + np.count_nonzero(state)
	else:
		return 0

def negaMax(state, depth, alpha, beta, colour):
	"""Recursively find the best move via a negamax search"""
	depth = min(depth, np.count_nonzero(state==0))
	if depth == 0 or positionScore(state) != 0:
		return positionScore(state) * colour

	highScore = -100

	moveList = moveFind(state)
	for move in moveList:
		score = -negaMax(moveSim(state, move, colour), depth -1, -beta, -alpha, -colour)
		highScore = max(score, highScore)
		alpha = max(alpha, highScore)
		if alpha >= beta:
			break

	return highScore

# This function is called safely anytime it might be the computer's turn
def computerMove():
	# Decide whether or not the computer is to play
	if gamecfg.engineIsCross == Square.crossToPlay and not Square.result:
		if gamecfg.engineIsCross:
			player = 1
		else:
			player = -1
		moveScores = {}
		for move in moveFind(Square.state):
			moveScores[move] = negaMax(moveSim(Square.state, move, player), gamecfg.lvl, -100, 100, player * -1)

		Square.squareDict[min(moveScores.keys(), key=(lambda k: moveScores[k]))].tac()
		print(moveScores)

def clearAll():
	while Square.moveList:
		Square.moveList.pop().clear()
	computerMove()

def main():
	root = tk.Tk()
	root.title("Tic Tac Toe")

	# Creating the board, 600 x 600 pixels, n squares across
	m = gamecfg.n
	size = 600 // m
	squares = [(rank, file) for rank in range(m) for file in range(m)]

	for (rank, file) in squares:
		square = Square((rank, file), master=root, size=size)
		square.grid(row=rank, column=file)

	# Creating File Menu
	menu = tk.Menu(root)
	root.config(menu=menu)

	fileMenu = tk.Menu(menu)
	menu.add_cascade(label="File", menu=fileMenu)
	# Undo calls the clear function on the most recently played square.
	fileMenu.add_command(label="Undo", command=lambda: Square.moveList.pop().clear())
	fileMenu.add_command(label="State", command=lambda: print(Square.state))
	fileMenu.add_command(label="Result", command=lambda: print(Square.result))
	fileMenu.add_command(label="Restart", command=lambda: clearAll())
	computerMove()
	root.mainloop()

if __name__ == '__main__':
	main()
