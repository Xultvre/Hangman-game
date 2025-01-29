import random

def hangman():
    # Word list and selection
    languages = [
    "english", "spanish", "chinese", "hindi", "arabic", "bengali", 
    "portuguese", "russian", "japanese", "french", "german", "italian", 
    "korean", "urdu", "turkish", "vietnamese", "thai", "swahili", 
    "dutch", "greek", "hebrew", "polish", "persian", "tamil", 
    "telugu", "indonesian", "malay", "punjabi", "gujarati", 
    "romanian", "czech", "hungarian", "ukrainian", "finnish", "swedish"
]
    word = random.choice(languages).lower()
    guessed_word = ["_"] * len(word)
    guessed_letters = set()
    attempts = 6
    
    # Simplified Hangman stages
    hangman_stages = [
        """
         -----
         |   |    
             |    
             |    
             |    
             |
        ====
        """,
        """
         -----
         |   |
         O   |
             |
             |
             |
        ====
        """,
        """
         -----
         |   |
         O   |
         |   |
             |
             |
        ====
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
             |
        ====
        """,
        """
         -----
         |   |
         O   |
        /|\  |
             |
             |
        ====
        """,
        """
         -----
         |   |
         O   |
        /|\  |
        /    |
             |
        ====
        """,
        """
         -----
         |   |
         O   |
        /|\  |
        / \  |
             |
        ====
        """
    ]           
    
    print("Welcome to the Hangman presented by Usman!")
    while True:
        username = input("Enter your name: ")
        if username.isalpha():
            print(f"Welcome, {username}! Let's play Hangman!")
            break
        else:
            print("Please use alphabets only for your name.")
    print(f"Your word is a language and it has {len(word)} letters.")
    
        # Game loop
    while attempts > 0:
        print(hangman_stages[6 - attempts])  # Show the hangman stage
        print("Word: " + " ".join(guessed_word))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")
        
        # Take user input
        guess = input(f"Guess a letter, {username}: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good guess {username}! '{guess}' is in the word.")
            # Update guessed_word
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Wrong guess {username}! '{guess}' is not in the word.")
            attempts -= 1
        
        # Check for win condition
        if "_" not in guessed_word:
            print(f"Congratulations, {username}! You guessed the word!")
            print("Word: " + "".join(guessed_word))
            break
    
    # End of game
    if attempts == 0:
        print(hangman_stages[-1])  # Show final hangman
        print(f"You're out of attempts, {username}! The word was:", word)
        print("Game over.")

# Run the game
hangman()
