#!/usr/bin/env python
# This class represents the game graph for the minimax algorithm
# It stores the root of the graph and the currently selected best move
class Graph(object):
	def __init__(self, previousPlayer, startingBoardState):
		self.root = Node(previousPlayer, 0, startingBoardState)
		self.bestMove = None

# This class represents a node in the game graph
# It stores the active player by color, the depth of the node in the graph, the new board state for
# consideration, and a list of child nodes
class Node(object):
	def __init__(self, playerColor, level, board):
		self.activePlayer = playerColor
		self.depth = level
		self.board = board
		self.children = []
