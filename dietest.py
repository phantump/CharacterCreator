import sys
import die
import die.roll

global die1,die2,die3,die4,nums
numrolls = input("Enter number of rolls needed: ")
int(numrolls)


def statnum(numrolls):
	global die1,die2,die3,die4,nums
	for x in range(numrolls) :
		#Sets up the dice roll
		d6 = die.Standard(6)
		die1 = (d6.roll())
		die2 = (d6.roll())
		die3 = (d6.roll())
		die4 = (d6.roll())

		#based on DnD character creation method: roll four and remove lowest die
		results = [die1, die2,die3,die4]
		del results[results.index(min(results))]
		#getting the sum of each set of dice to be used for stats
		nums = sum(results)
		print(nums)
print("these are the rolls for your character creation stats:")


statnum(int(numrolls))

