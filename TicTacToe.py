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
	if (board[1] == board[2] == board[3] == mark) or \
		(board[4] == board[5] == board[6] == mark) or \
		(board[7] == board[8] == board[9] == mark) or \
		(board[1] == board[5] == board[9] == mark) or \
		(board[3] == board[5] == board[7] == mark) or \
		(board[1] == board[4] == board[7] == mark) or \
		(board[2] == board[5] == board[8] == mark) or \
		(board[3] == board[6] == board[9] == mark):
		return True

def choose_first():
	number = 0
	number = random.randint(0,1)
	if number == 0:
		return "Player 1"
	else:
		return "Player 2"

def space_check(board, position):
	return board[position] == ' '

def full_board_check(board):
	for i in board:
		if i == ' ':
			return False
	return True

def player_choice(board):
	position = 0
	while position not in range(1,10) or not space_check(board, position):
		position = int(input('Please choose your position (1-9): '))
	return position

def replay():
	play = ' '
	while play != 'Y' and play != 'N':
		play = input('Do you want to play the game again?(Y/N) ').upper()
	if play == 'Y':
		return True
	elif play == 'N':
		return False
	
print('Welcome to my Tic Tac Toe game!')

while True:
	board = [' ']*10

	player1_marker,player2_marker = player_input()
	player = choose_first()
	print(player + ' will go first')

	play_game = input('Are you ready? Y/N ').upper()
	if play_game == "Y":
		game_on = True
	else:
		game_on = False


	while game_on:
		if player == 'Player 1':
			display_board(board)
			print("Player 1 ")
			position = player_choice(board)
			place_marker(board,player1_marker,position)
			if win_check(board,player1_marker) == True:
				display_board(board)
				print('Player 1 won!')
				game_on = False
			else:
				if full_board_check(board) == True:
					display_board(board)
					print("Its a tie game!")
					game_on = False
				else:
					player = 'Player 2'
		else:
			player == 'Player 2'
			display_board(board)
			print("Player 2 ")
			position = player_choice(board)
			place_marker(board,player2_marker,position)
			if win_check(board,player2_marker) == True:
				display_board(board)
				print('Player 2 won!')
				game_on = False
			else:
				if full_board_check(board) == True:
					display_board(board)
					print("Its a tie game!")
					game_on = False
				else:
					player = 'Player 1'

	if replay() == False:
		break
