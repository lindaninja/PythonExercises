import random

guess = random.randint(0, 10)

my_guess = -1
while my_guess != guess:
    my_guess = int(raw_input("Guess the number: "))

    if guess == my_guess:
        print("You guessed right!")
    elif my_guess< guess:
        print("Too small")
    else:
        print("Too big.")

