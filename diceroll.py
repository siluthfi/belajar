# import libraries
import random
import time
import os

def help():
	print('')
	print('======== WELCOME TO DICEROLL GAME ========')
	print('1. 1-17')
	print('2. 18-30')
	print('3. 31-42')
	print('0. Exit')
	result = int(input('Choose dice roll type that you want to roll> '))
	# time.sleep for delay 2 sec
	time.sleep(2)

	# to clear screen cmd
	os.system('cls')

	if result == 1 :
		print(first_roll())
	elif result == 2 :
		print(second_roll())
	elif result == 3 :
		print(third_roll())
	elif result == 0 :
		exit()
	else:
		print('Please choose correctly!')

def first_roll():
	return random.randint(1,17)

def second_roll():
	return random.randint(18,30)

def third_roll():
	return random.randint(31,42)

# to loop the program
if __name__ == '__main__':
	while(True) :
		help()