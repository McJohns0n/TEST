import random

def create_list(row,col):
	list = [[0 for y in range(col)] for x in range(row)]
	num = 1
	for x in range(row):
		if x % 2 == 0:
			for y in range(col):
				list[x][y] = num
				num += 1
		else:
			for y in range(col - 1,-1,-1):
				list[x][y] = num
				num += 1
	return(list)

def roll_dice ():
    num=random.randint(1,6)
    return num

def show_dice(num):
	if num == 1:
		print(" ___________")
		print("|           |")
		print("|           |")
		print("|     0     |")
		print("|           |")
		print("|___________|")
	elif num == 2:
		print(" ___________")
		print("|           |")
		print("|       0   |")
		print("|           |")
		print("|   0       |")
		print("|___________|")
	elif num == 3:
		print(" ___________")
		print("|           |")
		print("|       0   |")
		print("|     0     |")
		print("|   0       |")
		print("|___________|")
	elif num == 4:
		print(" ___________")
		print("|           |")
		print("|   0   0   |")
		print("|           |")
		print("|   0   0   |")
		print("|___________|")
	elif num == 5:
		print(" ___________")
		print("|           |")
		print("|   0   0   |")
		print("|     0     |")
		print("|   0   0   |")
		print("|___________|")
	elif num == 6:
		print(" ___________")
		print("|           |")
		print("|   0   0   |")
		print("|   0   0   |")
		print("|   0   0   |")
		print("|___________|")

def show_map(PlayerPieceLocation,playerShape,playerNum):
	showMap = create_list(5,5)
	for i in range(playerNum):
		x = PlayerPieceLocation[i][0]
		y = PlayerPieceLocation[i][1]
		if x != -1 and type(showMap[y][x]) == int:
			showMap[y][x] = playerShape[i]
		elif x != -1 and type(showMap[y][x]) != int:
			showMap[y][x] += playerShape[i]
	for i in range(len(showMap) - 1,-1,-1):
		print(showMap[i])
	return()

def calculate_piece_postion(positionX,positionY,diceNum):
    # an 5*5 length should be 0-4,so length -1
	if positionY%2 == 0: #line0,2,4
		positionX += diceNum
		if positionX <= 4: #0,1,2,3,4,[5,6,7,8,9],[10]
			return(positionX,positionY)
		elif positionX > 4 and positionX < 10:
			positionX = 5 - (positionX - 4) #next line is odd,so minus
			positionY += 1
		elif positionX == 10:
			positionX = 0
			positionY += 2
	else:#line1,3,5
		positionX -= diceNum
		if positionX >= 0: #[-6],[-5,-4-3,-2,-1],0,1,2,3,4,
			return(positionX,positionY)
		elif positionX < 0 and positionX >= -5:
			positionX = -positionX - 1 #next line is even, so convert to positive
			positionY += 1
		elif positionX == -6:
			positionX = 4
			positionY += 2
	if positionY == 5:
		positionX -= 1
		if positionX == -1:
			positionX = 0
			positionY = 3
		else:
			positionY = 4
	return(positionX,positionY)

def add_ladder():
	first_ladder_head_Y = random.randint(0,3)  						 #first ladder, the haed can't be at the top row
	first_ladder_head_X = random.randint(0,4)
	first_ladder_tail_Y = random.randint(first_ladder_head_Y+1,4)

	if first_ladder_tail_Y == 4:									#tail can't be at the last square
		first_ladder_tail_X = random.randint(0,3)
	else:
		first_ladder_tail_X = random.randint(0,4)

	second_ladder_head_Y = random.randint(0,3)  						#second ladder head
	second_ladder_head_X = random.randint(0,4)

	while (second_ladder_head_Y == first_ladder_head_Y and second_ladder_head_X == first_ladder_head_X) or (second_ladder_head_Y == first_ladder_tail_Y and second_ladder_head_X == first_ladder_tail_X):  #two heads can't be the same, and the second head can't be the same as the fist tail either
			second_ladder_head_Y = random.randint(0,3)  						 
			second_ladder_head_X = random.randint(0,4)

	second_ladder_tail_Y = random.randint(second_ladder_head_Y+1,4) #second ladder tail
	if second_ladder_tail_Y == 4:									#the tail can't be at the last square
		second_ladder_tail_X = random.randint(0,3)
	else:
		second_ladder_tail_X = random.randint(0,4)
	while (second_ladder_tail_Y == first_ladder_tail_Y and second_ladder_tail_X == first_ladder_tail_X) or (second_ladder_tail_Y == first_ladder_head_Y and second_ladder_tail_X == first_ladder_head_X):
			second_ladder_tail_Y = random.randint(second_ladder_head_Y+1,4)
			if second_ladder_tail_Y == 4:									
				second_ladder_tail_X = random.randint(0,3)
			else:
				second_ladder_tail_X = random.randint(0,4)
	return([[first_ladder_head_X,first_ladder_head_Y],[first_ladder_tail_X,first_ladder_tail_Y]],[[second_ladder_head_X,second_ladder_head_Y],[second_ladder_tail_X,second_ladder_tail_Y]])

def add_snake(): 
	# head
	snake_head_Y = random.randint(1,4)         #head can't be at first row
	if snake_head_Y == 4:                      #head can't be at the last square
		snake_head_X = random.randint(0,3)
	else:
		snake_head_X = random.randint(0,4)
	
	# tail
	snake_tail_Y = random.randint(0,snake_head_Y - 1)  #tail row must be lower than tail head
	snake_tail_X = random.randint(0,4)
		
	return([[snake_head_X,snake_head_Y],[snake_tail_X,snake_tail_Y]])

def check_location_of_snake_and_ladder(SnakeLocation,FirstLadderLocation,SecondLadderLocation):
	while True:
		for i in range(2):
			if(SnakeLocation[i] in FirstLadderLocation) or (SnakeLocation[i] in SecondLadderLocation):
				SnakeLocation = add_snake()
		else:
			return(SnakeLocation)

def check_encounter_and_move(PlayerPieceLocation,SnakeLocation,FirstLadderLocation,SecondLadderLocation):
	if PlayerPieceLocation == SnakeLocation[0]:
		PlayerPieceLocation = SnakeLocation[1]
		print('You triggered a snake!')
	elif PlayerPieceLocation == FirstLadderLocation[0]:
		PlayerPieceLocation = FirstLadderLocation[1]
		print('You triggered the first ladder!')
	elif PlayerPieceLocation == SecondLadderLocation[0]:
		PlayerPieceLocation = SecondLadderLocation[1]
		print('You triggered the second ladder!')
	else:
		print('Nice throw, everything is fine!')
	return(PlayerPieceLocation[0],PlayerPieceLocation[1])

def check_six(num):
	if num == 6:
		return(True)
	else:
		return(False)

def check_win(positionX,positionY,playershape):
	if positionX == 4 and positionY == 4:
		print('Player ',playershape," win!!!!")
		return(True)

def how_many_player():
	intFlag = False
	rangeFlag = False
	while intFlag == False or rangeFlag == False:
		try:
			playerNum = input("Enter how many player? from 1 - 5. \n")
			playerNum = int(playerNum)
			intFlag = True
		except:
			print("your should enter an integer,enter an integer next time")
			intFlag = False
		if intFlag == True:
			if playerNum >= 1 and playerNum <= 5:
				rangeFlag = True
			else:
				print("the range of number should between 1 - 5")
	return(playerNum)

def test():
	PlayerPieceLocation = [[-1,0],[-1,0],[-1,0],[-1,0],[-1,0]]
	#five player's piece location :player0,player1,player2,player3,player4
	#player3's x location is PlayerPieceLocation[3][0]
	playerNum = how_many_player()
	playerShape = ["A","B","C","D","E"]

	show_map(PlayerPieceLocation,playerShape,playerNum)
	Back_SnakeLocation = add_snake()
	Back_FirstLadderLocation,Back_SecondLadderLocation = add_ladder()
	Back_SnakeLocation = check_location_of_snake_and_ladder(Back_SnakeLocation,Back_FirstLadderLocation,Back_SecondLadderLocation)
	SnakeLocation,FirstLadderLocation,SecondLadderLocation = Back_SnakeLocation,Back_FirstLadderLocation,Back_SecondLadderLocation 


	print('This is the location of the snake: ', SnakeLocation)
	print('This is the location of the first ladder: ', FirstLadderLocation)
	print('This is the location of the second ladder: ', SecondLadderLocation )
	print('This is PlayerPieceLocation: ',PlayerPieceLocation)
	flag = False
	while  flag == False:
		for i in range(playerNum):
			if player(i,playerShape,playerNum,PlayerPieceLocation,SnakeLocation,FirstLadderLocation, SecondLadderLocation):
				flag = True
				break

def player(i,playerShape,playerNum,PlayerPieceLocation,SnakeLocation,FirstLadderLocation, SecondLadderLocation):
	print("player",playerShape[i]," ,use enter to roll dice")
	enter = input()
	num = roll_dice()
	show_dice(num)
	PlayerPieceLocation[i][0],PlayerPieceLocation[i][1] = calculate_piece_postion(PlayerPieceLocation[i][0],PlayerPieceLocation[i][1],num)
	PlayerPieceLocation[i][0],PlayerPieceLocation[i][1] = check_encounter_and_move(PlayerPieceLocation[i],SnakeLocation,FirstLadderLocation,SecondLadderLocation)
	show_map(PlayerPieceLocation,playerShape,playerNum)
	
	if check_win(PlayerPieceLocation[i][0],PlayerPieceLocation[i][1],playerShape[i]):
		return(True)
	print('This is the location of the snake: ', SnakeLocation)
	print('This is the location of the first ladder: ', FirstLadderLocation)
	print('This is the location of the second ladder: ', SecondLadderLocation )
	print('This is PlayerPieceLocation: ',PlayerPieceLocation)
	print()
	print()

	while check_six(num):
		print("six! player ",playerShape[i],"roll again")
		enter = input()
		num = roll_dice()
		show_dice(num)
		PlayerPieceLocation[i][0],PlayerPieceLocation[i][1] = calculate_piece_postion(PlayerPieceLocation[i][0],PlayerPieceLocation[i][1],num)
		PlayerPieceLocation[i][0],PlayerPieceLocation[i][1] = check_encounter_and_move(PlayerPieceLocation[i],SnakeLocation,FirstLadderLocation,SecondLadderLocation)
		show_map(PlayerPieceLocation,playerShape,playerNum)
		if check_win(PlayerPieceLocation[i][0],PlayerPieceLocation[i][1],playerShape[i]):
			return(True)
		print('This is the location of the snake: ', SnakeLocation)
		print('This is the location of the first ladder: ', FirstLadderLocation)
		print('This is the location of the second ladder: ', SecondLadderLocation )
		print('This is PlayerPieceLocation: ',PlayerPieceLocation)		
		print()
		print()
	
test()