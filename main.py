import random

# List of words for the game
words = ["apple", "banana", "cherry", "date", "fig", "grape", "lemon", "lime", "mango", "orange", "pineapple", "papaya"]

# Select a random word from the list
word = random.choice(words)

# Initialize the guessed letters and attempt counter
guessed_letters = []
attempts = 0

# ASCII art for the hangman figure
hangman_art = [
    """
     +---+
     |   |
         |
         |
         |
         |
    ==========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    ==========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    ==========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    ==========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    ==========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    ==========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    ==========
    """
]

# Loop until the player guesses the word or runs out of attempts
while True:
    # Print the hangman figure, word with guessed letters filled in, and display attempts remaining
    print(hangman_art[attempts])
    masked_word = ""
    for letter in word:
        if letter in guessed_letters:
            masked_word += letter
        else:
            masked_word += "_"
    print("Word: " + masked_word)
    print("Attempts remaining: " + str(max(0, 6 - attempts)))

    # Get the player's guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess is a single letter and not already guessed
    if len(guess) != 1 or not guess.isalpha() or guess in guessed_letters:
        print("Invalid guess. Please enter a single letter that has not been guessed before.")
        continue

    # Add the guessed letter to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guessed letter is in the word
    if guess in word:
        print("Correct!")
    else:
        print("Incorrect.")
        attempts += 1

    # Check if the player has guessed the entire word
    if set(word).issubset(set(guessed_letters)):
        print("Congratulations! You guessed the word: " + word)
        break

    # Check if the player has run out of attempts
    if attempts == 6:
        print(hangman_art[attempts])
        print("Game over. You failed to guess the word: " + word)

        break
