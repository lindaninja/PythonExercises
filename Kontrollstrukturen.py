is_sunny = False

print("Das heutige Wetter:")
if is_sunny:
    print("Heute ist es schoen!")
else:
    print("Heute ist es nicht schoen")

name = raw_input("Dein Name:")

if name == "Linda":
        print("0k, wilkommen!")
elif name == "Susi":
    print("auch noch OK.")
else:
    print("Du darfst nicht rein!")



import random
guess = random.randint(0,10)

my_guess = raw_input("Guess the number: ")
if guess == my_guess:
    print("You guessed right!")
    else:
    print("Wrong number.")
