import random

def display_board(board):
	print('\n'*100)
	print(board[7] + ' | ' + board[8]+ ' | ' + board[9])
	print('---------')
	print(board[4] + ' | ' + board[5]+ ' | ' + board[6])
	print('---------')
	print(board[1] + ' | ' + board[2]+ ' | ' + board[3])

def player_input():
	marker = ''
	while marker != 'X' and marker != 'O':
		marker = input('Player1: Choose X or O: ').upper()
	if marker == 'X':
		return ('X','O')
	else:
		return ('O','X')
	
def place_marker(board, marker, position):
	board[position] = marker

def win_check(board, mark):
	if (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark) or (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark) or (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark):
		return True

def choose_first():
	number = random.randit(0,1)

	if number == 0:
		return "Player 1"
	else:
		return "Player 2"

def space_check(board, position):
	return board[position] == ' '

# test_board = ['#','X',' ','X','O','X','O','X','O','X']

def full_board_check(board):
	for i in board:
		if i == ' ':
			return False
	return True