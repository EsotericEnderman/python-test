name = input("Enter your name:\n")

age = int(input("Enter your age:\n"))

if age > 24:
    old = True
else:
    old = False

if age < 5:
    baby = True
else:
    baby = False

print("Hello, " + name + ". You are " + str(age) + " years old.")

if old:
    print("You have one foot in the grave!")
elif baby:
    print("You are a baby! 👶")
else:
    print("You are still young!")
