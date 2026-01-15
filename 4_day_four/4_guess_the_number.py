# You will create a game where the person will have four lives to try and guess a number from 1 to 100:
import random

lives = 4
number_to_guess = random.randint(1,100)

while lives>=0:
    your_number = int(input("Put a number from 1 to 100: "))
    if your_number < number_to_guess and lives>0:
        print(f"Your number is less than the number to be guessed; you lost a life. lives: {lives} ")
        lives -= 1
    elif your_number > number_to_guess and lives>0:
        print(f"Your number is higher than the number to be guessed; you lost a life lives: {lives}. ")
        lives -= 1
    elif your_number == number_to_guess and lives>=0:
        print("You found a number, congratulations!!!!")
        break
    elif lives == 0:
        print(f"You lose. The number was '{number_to_guess}'!")
        break
