english_vowels = [ "a", "e", "i", "o", "u" ]

word = "random"
vowel_count = 0

for letter in word:
    if letter in english_vowels:
        print(letter)
        vowel_count += 1

print("The word '" + word + "' has " + str(vowel_count) + " vowels.")
