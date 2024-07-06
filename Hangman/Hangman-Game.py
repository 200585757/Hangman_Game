import random
from hangman_word import word_list
from hangman_art import logo
from hangman_art import stages

# Initialize the game state
end_of_game = False
chosen_word = random.choice(word_list)  # Randomly select a word from the word list
word_length = len(chosen_word)
lives = 6

print(logo)  # Print the hangman game logo

# Debug: Show the chosen word for testing purposes
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks for the chosen word
display = []
for _ in range(word_length):
    display += "_"

# Main game loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()  # Get the player's guess and convert it to lowercase
    
    # Check if the letter has already been guessed
    if guess in display:
        print(f"You've already guessed {guess}")
        
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # Replace blanks with the guessed letter if it matches
        if letter == guess:
            display[position] = letter
    
    # If the guessed letter is not in the chosen word
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1  # Reduce the number of lives by 1
        if lives == 0:  # If no lives are left, the game ends
            end_of_game = True
            print("You lose.")
        
    # Print the current state of the guessed word
    print(f"{' '.join(display)}")
    
    # Check if the player has guessed all the letters
    if "_" not in display:
        end_of_game = True
        print("You win.")
        
    # Print the current stage of the hangman
    print(stages[lives])
