import random
import time

player = random.randint(1,6)
ai = random.randint(1,6)

print("Press return to roll your die")

roll = raw_input()
print("You rolled " + str(player) )
time.sleep(5)
print("The computer rolled " + str(ai) )
time.sleep(2)


if player > ai : 
	print("You Win")
elif player == ai :
	print("Much like in life, no one won this round")
else :
	print("You Lose")
	
	
	
