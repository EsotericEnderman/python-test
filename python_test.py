name = input("Enter your name:\n")

age = int(input("Enter your age:\n"))

print(age + 2)
print("This will be your age in 2 years!")
print(name)

if age > 24:
    old = True
else:
    old = False

print("Hello, " + name + ". You are " + str(age) + " years old.")

if old:
    print("You have one foot in the grave!")
else:
    print("You are still young!")
