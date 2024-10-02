english_vowels = [ "a", "e", "i", "o", "u" ]

seen_vowels = []

string_input = input("Please enter a string: ")
unique_vowel_count = 0

for letter in string_input:
    if letter in english_vowels:
        if letter not in seen_vowels:
            seen_vowels.append(letter)
            unique_vowel_count += 1

print("The string + '" + string_input + "' contains " + str(unique_vowel_count) + " unique vowels!")
