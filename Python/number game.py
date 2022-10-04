import random

n = random.randint(1, 100)
guess = 1

while (guess <= 6):
    i = int(input("Enter Your Guess: "))

    if (i < n):
        print("Your guess is smaller than the number.")
    elif (i > n):
        print("Your guess is greater than the number.")
    else:
        print("YOU WON!")
        print("You took", guess, "guesses")
        break
    print("You have", 6-guess, "guesses left")
    guess = guess+1

if (guess > 6):
    print("GAME OVER")