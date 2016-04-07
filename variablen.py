age = 27
name = "Kurt Huber"
teperatur = 18.25
is_sunny = False # oder True

print (age)
print("Mein Name ist " + name)
print("Mein Name ist " + name + " und ich bin " + str(age) + " Jahre alt")
print("Mein Name ist %s und ich bin %d Jahre alt" % (name, age))

name = raw_input("Gib deinen Namen ein: ")
print(name)
