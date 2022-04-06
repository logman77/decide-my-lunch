import sys
import random
import time

#Decide-My-Lunch Version 1.0 Created By @logman77 2018
#Welcome Message
print("""Thank you for using Decide My Lunch! 
Please follow the directions. Let's get started
How many choices are you deciding between (2-5)?""")

#prompt user to input how number of options
option_number = input("> ")
print(f"Ok, so you have {option_number} options")
#define variable choices as an integar
choices = int(option_number)
#if user enters 1 or less than 1 -  close program
if choices <= 1:
	print("Stop wasting my time! Enter between 2 and 5 choices please.")
	time.sleep(4)
	sys.exit(0)
#if user enter 6 or more than 6 - close program
elif choices >= 6:
	print("Stop wasting my time! Enter between 2 and 5 choices please.")
	time.sleep(4)
	sys.exit(0)
#if everything is good, continue
else:
	print("Now you will enter the restaurant names: ")
#user enters 2 restaurants
if choices == 2:
	print("Restaurant Name 1:")
	name1 = input("> ")
	print("Restaurant Name 2:")
	name2 = input("> ")
	choice_of_2 = [name1, name2]
	print("You should go to: ",random.choice(choice_of_2))
#user enters 3 restaurants
if choices == 3:
	print("Restaurant Name 1:")
	name1 = input("> ")
	print("Restaurant Name 2:")
	name2 = input("> ")
	print("Restaurant Name 3:")
	name3 = input("> ")
	choice_of_3 = [name1, name2, name3]
	print("You should go to: ",random.choice(choice_of_3))
#user enters 4 restaurants
if choices == 4:
	print("Restaurant Name 1:")
	name1 = input("> ")
	print("Restaurant Name 2:")
	name2 = input("> ")
	print("Restaurant Name 3:")
	name3 = input("> ")
	print("Restaurant Name 4:")
	name4 = input("> ")
	choice_of_4 = [name1, name2, name3, name4]
	print("You should go to: ",random.choice(choice_of_4))
#user enters 5 restaurants
if choices == 5:
	print("Restaurant Name 1:")
	name1 = input("> ")
	print("Restaurant Name 2:")
	name2 = input("> ")
	print("Restaurant Name 3:")
	name3 = input("> ")
	print("Restaurant Name 4:")
	name4 = input("> ")
	print("Restaurant Name 5:")
	name5 = input("> ")
	choice_of_5 = [name1, name2, name3, name4, name5]
	print("You should go to: ",random.choice(choice_of_5))
#Pause and end script
print("Thanks for using Decide My Lunch. Goodbye")
time.sleep(10)
