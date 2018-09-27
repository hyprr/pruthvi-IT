import random
print("welcome to the game of snake and ladder")
count=0
while(count<=100):
	a=input("enter r to roll the dice")
	if (a=='r'):
		r=random.randint(1,6)
		print(r)
		count=count+r
		print("yourscore is ",count)
		if(count==100):
			print("you have won")
			print("your score is",count)
		elif(count==8):
			print("you have climbed the ladder")
			print("your score is",count)
			count=37
		elif(count==11):
			print("you have been bitten by snake")
			print("your score is",count)
			count=2
		elif(count==13):
			print("you have climbed the ladder")
			print("your score is",count)
			count=34
		elif(count==25):
			print("you have been bitten by snake")
			print("your score is",count)
			count=4
		elif(count==38):
			print("you have  bitten by snake")
			print("your score is",count)
			count=9
		elif(count==40):
			print("you have climbed the ladder")
			print("your score is",count)
			count=68
		elif(count==52):
			print("you have climbed the ladder")
			print("your score is",count)
			count=81
		elif(count==65):
			print("you have bitten by snake")
			print("your score is",count)
			count=46
		elif(count==76):
			print("you have climbed the ladder")
			print("your score is",count)
			count=97
		elif(count==89):
			print("you have bitten by snake")
			print("your score is",count)
			count=70
		elif(count==93):
			print("you have bitten by snake")
			print("your score is",count)
			count=64
	else:
		break
		




