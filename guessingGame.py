import random 

number = random.randint(1,9)

chances = 0
print("Guess a number between 1 and 9")

while chances < 5:
    guess = int(input("Guess your number"))
    print(guess)
    if guess == number:
        print("Congratulations, you won!!!")
        break
    if guess < number:
        print("Your guess is low, guess a higher number than ", guess)
    else:
        print("Your guess is too high, guess a lower number than ", guess)
    
    chances = chances+1

if not chances < 5:
    print("You Lost, the number is" , number)
    