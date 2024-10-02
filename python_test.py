name = input("Enter your name:\n")

age = int(input("Enter your age:\n"))

if age > 24:
    old = True
else:
    old = False

print("Hello, " + name + ". You are " + str(age) + " years old.")

if old:
    print("You have one foot in the grave!")
else:
    print("You are still young!")
