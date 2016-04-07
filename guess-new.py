import random

guess = random.randint(0, 10)

my_guess = -1
count = 0

while my_guess != guess:

    count +=1
    if count == 4:
        print("Game Over!")
        break
    my_guess = int(raw_input("Guess the number: "))

    if guess == my_guess:
        print("You guessed right!")
    elif my_guess< guess:
        print("Too small")
    else:
        print("Too big.")



