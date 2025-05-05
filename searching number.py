import random
guess_number=random.randint(1,100)
guess = None
attempts = 0
print("welcome to number guessing game^")
print("Please enter the one number between 1 to 100")
while guess!=guess_number:
    guess= int(input("Guess the number:"))
    attempts += 1
    if guess < guess_number:
        print("sorry but it's too low number")
    elif guess >  guess_number:
        print("sorry but it's too high number")
    else:
        print("Congratulations!!!!!!Your guessed number is rigth")
        