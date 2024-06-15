import random

def choose_word(difficulty):
    # List of words for each difficulty level
    easy_words = ["eye", "toes", "nose", "chin", "head"]
    medium_words = ["elephant", "giraffe", "rhinoceros", "hippopotamus", "crocodile"]
    hard_words = ["pendimethalin", "glyphosate", "difenconazole", "aminopyralid", "triclopyr"]

    # Select a word based on the difficulty chosen
    if difficulty == "1":
        return random.choice(easy_words)
    elif difficulty == "2":
        return random.choice(medium_words)
    elif difficulty == "3":
        return random.choice(hard_words)
    else:
        return None  # Invalid difficulty level

def hangman():
    print("Welcome to Hangman!")
    
    # Display difficulty menu
    print("Select difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    
    # Get user's choice of difficulty
    difficulty = input("Enter your choice (1/2/3): ")
    
    # Choose a word based on the difficulty
    word = choose_word(difficulty)
    
    if word:
        guessed_letters = []
        tries = 6  # Number of tries allowed
        
        while tries > 0:
            # Display current status of the word
            display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
            print(f"Word: {display_word}")
            
            # Prompt user for a letter
            guess = input("Guess a letter: ").lower()
            
            # Check if the guessed letter is in the word
            if guess in word:
                print("Correct!")
                guessed_letters.append(guess)
            else:
                print("Incorrect!")
                tries -= 1
            
            # Check if the word has been guessed completely
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word '{word}' correctly.")
                break
        
        if tries == 0:
            print(f"Sorry, you ran out of tries. The word was '{word}'.")
    
    else:
        print("Invalid difficulty level. Please choose a valid option (1, 2, or 3).")

# Run the game
hangman()