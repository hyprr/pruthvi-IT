import random
while True:
	n=input("enter q to quit,or any other number to roll dice:")

	if(n=='q'):
		print("bye...")
		exit()

	else(n=='r'):
		r=random.randint(1,6)
		print(r)
		exit()
		