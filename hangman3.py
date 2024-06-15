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

def create_hidden_word(word):
    return ' '.join(['_' for _ in word])

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
    
    # STEP 3: Display the chosen word with all letters replaced by "_"
    hidden_word = create_hidden_word(word_to_guess)
    print(f"The word to guess is: {hidden_word}")

    while lives > 0:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
        print(f"Word: {display_word}")
        
        guess = input("Guess a letter: ").lower()
        
        if guess in word_to_guess:
            print("Correct!")
            guessed_letters.append(guess)
        else:
            print("Incorrect!")
            lives -= 1
        
        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Congratulations! You guessed the word '{word_to_guess}' correctly.")
            break
    
    if lives == 0:
        print(f"Sorry, you ran out of lives. The word was '{word_to_guess}'.")

# Run the game
hangman()