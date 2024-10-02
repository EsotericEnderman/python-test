english_vowels = [ "a", "e", "i", "o", "u" ]

string = input("Enter a string: ")
vowel_count = 0

for letter in string:
    if letter in english_vowels:
        print(letter)
        vowel_count += 1

print("The string '" + string + "' has " + str(vowel_count) + " vowels.")
