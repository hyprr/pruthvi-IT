import random
b={1:'r',2:'p',3:'s'}
while True:
	a=input("your choice r/p/s:")
	c=[random.randint(1,3)]
	print("your choice",a,"computer choice",c)
	if(a==c):
		print("draw")
	elif a=='r':
		if c=='p':
			print("you wins")
		else:
			print("player wins")
	elif a=='p':
		if c=='s':
			print("you wins")
		else:
			print("player wins")
	elif a=='s':
		if c=='r':
			print("you wins")
		else:
			print("you wins")
	