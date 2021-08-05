#pyngo.py
import random

strike_for_player1 = 0 
strike_for_player2 = 0

p1_nums = []
p2_nums = []

bingo1 = ['B', 'I', 'N', 'G', 'O']
bingo2 = ['B', 'I', 'N', 'G', 'O']

result_for_horizontal1 = [False, False, False, False, False]
result_for_horizontal2 = [False, False, False, False, False]
result_for_vertical1 = [False, False, False, False, False]
result_for_vertical2 = [False, False, False, False, False]
result_for_diagonal1 = [False, False]
result_for_diagonal2 = [False, False]

def randomBoard(l1,l2):

	l1 = list(range(1,26))
	random.shuffle(l1)
	for i in range(25):
		l1[i] = str(l1[i]).rjust(2,'0')
	p1_nums	= l1
	
	l2 = list(range(1,26))
	random.shuffle(l2)
	for i in range(25):
		l2[i] = str(l2[i]).rjust(2,'0')

	p2_nums = l2
	

	printBoard(p1_nums, p2_nums)
	theGame(p1_nums, p2_nums)


def customBoard(l1,l2):
	#taking input from player 1:
	print(f"{player1} may enter the numbers in 1x1, 1x2 (row-wise) order")
	i1 = 0
	while i1 <= 24:

		try:
			bingoBoard1 = int(input())
		except ValueError:
			print("I said \"numbers\". You idiot")
			continue

		if bingoBoard1 in l1:
			print("That number is already on the board. Please input different number.")
		elif int(bingoBoard1) not in range(1,26):
			print("Please enter an integer between 1 to 25")
		else:
			l1.append(bingoBoard1)
			i1 += 1
		print(f"{player1} has entered entered following numbers so far: \n{l1}")

	for i in range(25):
		l1[i] = str(l1[i]).rjust(2,'0')

	p1_nums = l1


	#same steps repeated for player2: 

	print(f"Now, {player2} may enter the numbers in 1x1, 1x2 (row-wise) order.")
	i2 = 0
	while i2 <= 24:
		
		try:
			bingoBoard2 = int(input())
		except ValueError:
			print("I said \"numbers\". You idiot")
			continue

		if bingoBoard2 in l2:
			print("You have already entered that number. Please input different number.")
		elif int(bingoBoard2) not in range(1,26):
			print("Please enter an integer between 1 to 25")
		else:
			l2.append(bingoBoard2)
			i2 += 1
		print(f"{player2} has entered entered following numbers so far: \n{l2}")

	for i in range(25):
			l1[i] = str(l1[i]).rjust(2,'0')
	p2_nums = l2

	printBoard(p1_nums, p2_nums)
	theGame(p1_nums, p2_nums)

def theGame(l1,l2):
	game_round = 1
	crossed_nums = []
	while True:
		print(f"Round {game_round} begins:")
		#asking number from player 1 and striking on both boards:
		try:
			strike = int(input(f"\n{player1} may enter a number.To end the game, enter any word."))
		except ValueError:
			quit(f"{player1} ended the game. Thank you for playing BINGO")
		

		if strike not in range(1,26):
			print("Please enter a number between 1 to 25.")
		elif strike in crossed_nums:
			print(f"This number has already been taken {player1}. Please enter another number.")
			continue
		crossed_nums.append(strike)
			

		for i in range(25):
			if l1[i] == str(strike).rjust(2,'0'):
				l1[i] = ' X'
		p1_nums = l1

		for i in range(25):
			if l2[i] == str(strike).rjust(2,'0'):
				l2[i] = ' X'
		p2_nums = l2

		gameProgress(p1_nums, p2_nums)

		#asking number from player 2 and striking on both boards:
		try:
			strike = int(input(f"\n{player2} may enter a number.To end the game, enter any word."))
		except ValueError:
			quit(f"{player2} ended the game. Thank you for playing BINGO")
		

		if strike not in range(1,26):
			print("Please enter a number between 1 to 25.")
		elif strike in crossed_nums:
			print(f"This number has already been taken {player2}. Please enter another number.")
			continue
		crossed_nums.append(strike)

		for i in range(25):
			if l1[i] == str(strike).rjust(2,'0'):
				l1[i] = ' X'
		p1_nums = l1

		for i in range(25):
			if l2[i] == str(strike).rjust(2,'0'):
				l2[i] = ' X'
		p2_nums = l2

		gameOver()


		printBoard(p1_nums, p2_nums)
		
		gameProgress(p1_nums, p2_nums)

		game_round += 1

def gameProgress(l1,l2):
	global strike_for_player1
	global strike_for_player2

	#yielding list of horizontals for player 1 :
	horizontal_list1 = []
	x = 0 
	for i in range(5):
		horizontal_list1.append(l1[x:x+5])
		x += 5

	#yielding horizontal results for player 2:
	horizontal_list2 = []
	x = 0 
	for i in range(5):
		horizontal_list2.append(l2[x:x+5])
		x += 5 

	#yielding vertical results for player 1:
	vertical_list1 = []
	x = 0
	for i in range(5):
		vertical_list1.append([l1[x],l1[x+5],l1[x+10],l1[x+15],l1[x+20]])
		x += 1
	# yielding vertical results for player 2
	vertical_list2 = []
	x = 0
	for i in range(5):
		vertical_list2.append([l2[x],l2[x+5],l2[x+10],l2[x+15],l2[x+20]])
		x += 1

	
	#checking for all horizontal strikethrough of game for player 1:		
	for i in range(5):
		if result_for_horizontal1[i] == False:
			result_for_horizontal1[i] = all([k == ' X' for k in horizontal_list1[i]])
			if result_for_horizontal1[i] == True:
				horizontal_list1[i] = []
				strike_for_player1+=1
				

	#checkingg for all vertical strikethrough of game for player 1:

	for i in range(5):
		if result_for_vertical1[i] == False:
			result_for_vertical1[i] = all([k == ' X' for k in vertical_list1[i]])
			if result_for_vertical1[i] == True:
				vertical_list1[i] = []
				strike_for_player1+=1

	#checking for all horizontal strikethrough of game for player 2:

	for i in range(5):
		if result_for_horizontal2[i] == False:
			result_for_horizontal2[i] = all([k == ' X' for k in horizontal_list2[i]])

			if result_for_horizontal2[i] == True:
				horizontal_list2[i] = []
				strike_for_player2+=1

			
	#checkingg for all vertical strikethrough of game for player 2:

	x = 0
	for i in range(5):
		if result_for_vertical2[i] == False:
			result_for_vertical2[i] = all([k == ' X' for k in vertical_list2[i]])
			x+=1
			if result_for_vertical2[i] == True:
				vertical_list2[i] = []
				strike_for_player2+=1

	#checking for 1st diagonal strikethrough of game for player 1:
	
	if result_for_diagonal1[0] == False:
		x = 0
		result_for_diagonal1[0] = all([l1[x] == l1[x+6] == l1[x+12] == l1[x+18] == l1[x+24] == ' X'])
		if result_for_diagonal1[0] == True:
			strike_for_player1 += 1
		 

	#checking for 1st diagonal strikethrough of game for player 2:
	
	if result_for_diagonal1[1] == False:
		x = 0
		result_for_diagonal1[1] = all([l2[x] == l2[x+6] == l2[x+12] == l2[x+18] == l2[x+24] == ' X'])
		if result_for_diagonal1[1] == True:
			strike_for_player2 += 1

	#checking for 1st diagonal strikethrough of game for player 1:
	
	if result_for_diagonal2[0] == False:
		x = 4 
		result_for_diagonal2[0] = all([l1[x] == l1[x+4] == l1[x+8] == l1[x+12] == l1[x+16] == ' X'])
		if result_for_diagonal2[0] == True:
			strike_for_player1+=1

	#checking for 1st diagonal strikethrough of game for player 2:
	
	if result_for_diagonal2[1] == False:
		x = 4
		result_for_diagonal2[1] = all([l2[x] == l2[x+4] == l2[x+8] == l2[x+12] == l2[x+16] == ' X'])
		if result_for_diagonal2[1] == True:
			strike_for_player2+=1



def gameOver():
	global strike_for_player1
	global strike_for_player2
	#crossing bingo for plater 1:

	print(f"Strike for player 1 = {strike_for_player1}, Strike for player 2 = {strike_for_player2}")

	if strike_for_player1 == 1:
		bingo1[0] = 'X'
	if strike_for_player1 == 2:
		bingo1 [0] = 'X' 
		bingo1[1] = 'X'
	if strike_for_player1 == 3:
		bingo1 [0] = 'X' 
		bingo1[1] = 'X'
		bingo1[2] = 'X'
	if strike_for_player1 == 4:
		bingo1 [0] = 'X' 
		bingo1[1] = 'X'
		bingo1[2] = 'X'
		bingo1[3] = 'X'
	if strike_for_player1 == 5:
		bingo1 [0] = 'X' 
		bingo1[1] = 'X'
		bingo1[2] = 'X'
		bingo1[3] = 'X'
		bingo1[4] = 'X'

		quit(f"{player1} has won!!!. Thank you for playing BINGO.")

	if strike_for_player2 == 1:
		bingo2[0] = 'X'
	if strike_for_player2 == 2:
		bingo2[0] = 'X'
		bingo2[1] = 'X'
	if strike_for_player2 == 3:
		bingo2[0] = 'X'
		bingo2[1] = 'X'
		bingo2[2] = 'X'
	if strike_for_player2 == 4:
		bingo2[0] = 'X'
		bingo2[1] = 'X'
		bingo2[2] = 'X'
		bingo2[3] = 'X'
	if strike_for_player2 == 5:
		bingo2[0] = 'X'
		bingo2[1] = 'X'
		bingo2[2] = 'X'
		bingo2[3] = 'X'
		bingo2[4] = 'X'
		quit(f"{player2} has won!!!. Thank you for playing BINGO")

def printBoard(l1,l2):

	print(f"\nBoard for {player1}: \n")
	x=0
	for i in range(5):
		for j in range(5):
			print(l1[x], end = ' | ')
			x+=1
		if i in range(4):
			print(bingo1[i],"\n---+----+----+----+----+----")
		else:
			print(bingo1[i],"\n")

	print(f"\nBoard for {player2}: \n")
	x=0
	for i in range(5):
		for j in range(5):
			print(l2[x], end =' | ')
			x+=1
		if i in range(4):
			print(bingo2[i],"\n---+----+----+----+----+----")
		else:
			print(bingo2[i],"\n")



random_or_custom = input('Type "custom" if you want a custom board.\nType anything if you want a random board.\n')

player1 = input("Enter name for player 1: ")
player2 = input("Enter name for player 2: ")


if random_or_custom == "custom":
	customBoard(p1_nums,p2_nums)
else:
	randomBoard(p1_nums,p2_nums)
