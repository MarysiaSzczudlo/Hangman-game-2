import random

def read_words_from_file(filename):
    words = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 2:
                    words.append(parts[0].strip().lower())
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return words

def choose_word(difficulty, words):
    if difficulty == "1":
        filtered_words = [word for word in words if len(word) <= 5]
    elif difficulty == "2":
        filtered_words = [word for word in words if 5 < len(word) <= 8]
    elif difficulty == "3":
        filtered_words = [word for word in words if len(word) > 8]
    else:
        return None
    
    if not filtered_words:
        print(f"No words found for difficulty level {difficulty}")
        return None
    
    return random.choice(filtered_words)

def create_hidden_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def display_hangman(lives):
    hangman_art = [
        """
         +---+
         |   |
             |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """
    ]
    
    print(hangman_art[6 - lives])

def hangman():
    print("Welcome to Hangman!")
    
    words = read_words_from_file('countries-and-capitals.txt')
    
    if not words:
        print("No words loaded from file.")
        return
    
    print("Select difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    
    difficulty = input("Enter your choice (1/2/3): ")
    
    word_to_guess = choose_word(difficulty, words)
    
    if word_to_guess is None:
        print("Invalid difficulty level or no words available for the chosen level.")
        return
    
    if difficulty == "1":
        lives = 7
    elif difficulty == "2":
        lives = 5
    elif difficulty == "3":
        lives = 3
    else:
        lives = 5
    
    guessed_letters = []
    already_tried_letters = []
    
    # STEP 3: Display the chosen word with all letters replaced by "_"
    hidden_word = create_hidden_word(word_to_guess, guessed_letters)
    print(f"The word to guess is: {hidden_word}")

    while lives > 0:
        display_word = create_hidden_word(word_to_guess, guessed_letters)
        print(f"Word: {display_word}")
        
        while True:
            # STEP 4: Ask the user to type a letter and validate if it's "quit" in any form
            guess = input("Guess a letter (or type 'quit' to exit): ").lower()
            
            if guess.lower() == 'quit':
                print("You chose to quit the game. Goodbye!")
                return

            # STEP 5: Validate if the letter is already tried
            if guess in already_tried_letters:
                print("You have already tried this letter. Try another one.")
            else:
                already_tried_letters.append(guess)
                break

        if guess in word_to_guess:
            print("Correct!")
            guessed_letters.append(guess)
        else:
            print("Incorrect!")
            lives -= 1
            display_hangman(lives)
        
        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Congratulations! You guessed the word '{word_to_guess}' correctly.")
            break
    
    if lives == 0:
        print(f"Sorry, you ran out of lives. The word was '{word_to_guess}'.")

# Run the game
hangman()