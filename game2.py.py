import random
print("welcome to the game of snake and ladder")
count=0
while(count<=100):
	a=input("enter r to roll the dice")#count to roll a dice
	if (a=='r'):
		r=random.randint(1,6)
		print(r)
		count=count+r#counting score
		print("yourscore is ",count)
		if(count==100):
		#checking condition
			print("you have won")
			print("your score is",count)
		elif(count==8):
		#checking condition
			print("you have climbed the ladder")
			print("your score is",count)
			count=37
		elif(count==11):
		#checking condition
			print("you have been bitten by snake")
			print("your score is",count)
			count=2
		elif(count==13):
		#checking condition
			print("you have climbed the ladder")
			print("your score is",count)
			count=34
		elif(count==25):
		#checking condition
			print("you have been bitten by snake")
			print("your score is",count)
			count=4
		elif(count==38):
		#checking condition
			print("you have  bitten by snake")
			print("your score is",count)
			count=9
		elif(count==40):
			#checking condition
			print("you have climbed the ladder")
			print("your score is",count)
			count=68
		elif(count==52):
			#checking condition
			print("you have climbed the ladder")
			print("your score is",count)
			count=81
		elif(count==65):
			#checking condition
			print("you have bitten by snake")
			print("your score is",count)
			count=46
		elif(count==76):
		#checking condition
			print("you have climbed the ladder")
			print("your score is",count)
			count=97
		elif(count==89):
			#checking condition
			print("you have bitten by snake")
			print("your score is",count)
			count=70
		elif(count==93):
			#checking condition
			print("you have bitten by snake")
			print("your score is",count)
			count=64
	else:
		#using it to run the program untill it reaches 100 or more
		break
		




