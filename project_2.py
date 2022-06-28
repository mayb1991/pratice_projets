import random

def guess(x):
    ramdom_number = random.randint(1, x)
    guess = 0
    while guess != ramdom_number:
        guess = int(input(f"Guess a number betweek 1 and {x}: "))
        if guess < ramdom_number:
            print("Sorry your guess is too low try again.")
        elif guess > ramdom_number:
            print("Sorry your guess is too high try again.")
    print("Congrautions you guessed the right number!")

def compture_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
          guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} to high (h) too low (l) or correct (c)")
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess +1
    print("Yay! The compture guessed the number right")

compture_guess(50)
