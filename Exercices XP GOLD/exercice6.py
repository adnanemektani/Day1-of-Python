number = int(input("Please enter a number from 1 to 9: "))
import random
random_number = random.randint(1, 9)
if number == random_number:
    print("Congratulations! You guessed the correct number:", random_number)
else:
    print("Sorry, the correct number was:", random_number)
