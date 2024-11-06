# Write a program that continues to ask for a number until the correct number is guessed.
secret_number = 42

def guess_the_number():
    while True:

        guess = int(input("Guess the secret number: "))
        if guess == secret_number:
            print("Congratulations! You've guessed the correct number!")
            break
        else:
            print("Incorrect! Try again.")
guess_the_number()