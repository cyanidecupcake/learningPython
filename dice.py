#!/usr/bin/python

##Open in Terminal to play this game of chance.

import random
import time


def dice() :   ##Function

	player = random.randint(1,6)
	ai = random.randint(1,6)

	print("You rolled " + str(player) )
	time.sleep(5)
	print("The computer rolled " + str(ai) )
	time.sleep(3)


	if player > ai : 
		print("You win... this round")
	elif player == ai :
		print("Much like in life, no one won this round")
	else :
		print("You Lose")

	
	time.sleep(4)
	
	print("")
	print("Would you like to quit? Y/N") 
	cont = raw_input()
	if cont == "Y" or cont == "y" :
		exit()
		
	elif cont == "N" or cont == "n" : 
		pass
	else :
		print("What do you want from me?!")
	
	
while True :
	print(" ")
	print("Press return to roll your die")
	roll = raw_input()
	dice()
	
	
