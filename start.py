#!/usr/bin/env python

import os, sys
from ChessLibrary import AIChessGame
from ChessLibrary import BoardState

# Prints the parameters at the start of a new game
def printStart(players, useHeuristicY):
	print("\n-------------------------------------------")
	print("Game started...")
	print("Test case " + str(game.testCase) + ": ", end = "")

	# Print starting positions of all pieces
	i = j = 0
	for player in players:
		for piece in player.pieces:
			print(piece.getLabel() + str(piece.position), end = "")
			if (i < len(players) - 1) or (j < len(player.pieces) - 1):
				print(", ", end = "")
			j = j + 1
		i = i + 1

	print("\nHeuristic functions used: ", end = "")
	if useHeuristicY:
		print("heuristicX, heuristicY");
	else:
		print("heuristicX")
	print("-------------------------------------------")

# Plays a game of chess
def play(game):
	whiteMoves = 0
	printStart(game.players, game.useHeuristicY)
	game.printBoard()
	for n in range(game.n):
		for player in game.players:
			# End the game if check mate or stale mate
			game.board.calcBoardState()
			if game.board.state != BoardState["None"] and str(player) == "Black":
				print("Number of moves made: " + str(whiteMoves))
				if game.board.state == BoardState["Checkmate"]:
					print("Game result: Checkmate")
				
				else:
					print("Game result: Stalemate")
				return
			# If the game is not over, make the next move and draw the board
			else:
				player.movePlayer(game)
				game.printBoard()
				if str(player) == "White":
					whiteMoves = whiteMoves + 1

	print("Numer of moves made: " + str(whiteMoves))
	print("Game result: None")

# Begins program execution
if __name__ == "__main__":
    game = ChessLibrary(1)
    game.start()
    play(game)
