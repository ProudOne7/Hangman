# Asking the word to be guessed
hidden_word = str(input("Enter a word for the second user to guess: "))
playing = True

# How many lives the guesser has
lives = 5

# List to store the words found
hidden_word_store = []

# Filling the list with dashes
for x in hidden_word:
    hidden_word_store.append("-")

while playing:
    # Checking if the player ran out of lives
    if lives == 0:
        playing = False
        print(f"You lost! The word was: {hidden_word}")
    # Checking if the player has guess the whole word
    elif "-" not in hidden_word_store:
        print(f"You guess the word! It was {hidden_word}")
        playing = False
    # Runs if the word has not been guessed yet
    else:
        print(f"Here is the board {hidden_word_store}")
        print(f"You have {lives} lives left")
        guess = input("Guess a letter in the hidden word: ")
        # If the guessed letter is in the hidden word
        if guess in hidden_word:
            for x in range(len(hidden_word)):
                if guess == hidden_word[x]:
                    hidden_word_store[x] = guess
        # If the guesser incorrectly guesses the word
        else:
            print("That's not in the word!")
            lives -= 1
    print()
