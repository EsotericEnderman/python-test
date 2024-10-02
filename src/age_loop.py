age = int(input("Enter your age:\n"))

for i in range(age):
    print(i)

name = input("Enter your name:\n")

print("The first letter of your name is " + name[0])

for letter in name:
    print(letter)

name_length = len(name)
i = 0

while i < name_length:
    print(name[i])
    i += 1
