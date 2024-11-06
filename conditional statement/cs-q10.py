# Write a program to determine if a given character is a vowel or consonant.
def check_character(char):
    if char.isalpha() and len(char) == 1:
        char = char.lower()
        if char in 'aeiou':
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "Invalid input. Please enter a single alphabetic character."