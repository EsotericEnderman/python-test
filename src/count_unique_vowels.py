english_vowels = [ "a", "e", "i", "o", "u" ]

seen_vowels = []

string_input = input("Please enter a string: ")
unique_vowel_count = 0

letter_index = 0

while letter_index < len(string_input):
    letter = string_input[letter_index]
    if letter in english_vowels and letter not in seen_vowels:
        seen_vowels.append(letter)
        unique_vowel_count += 1
    letter_index += 1

print("The string + '" + string_input + "' contains " + str(unique_vowel_count) + " unique vowels!")
