import nltk
import random
import os
nltk.download('words')

def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

words = nltk.corpus.words.words()
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''



print(logo + "\n Welcome to the Hangman game.\n" )
random_word = random.choice(words)
word_lenght = len(random_word)
lives = 6
end_of_game = False

display= []
for _ in range(word_lenght):
     display += "_"


while not end_of_game:
        guess = input("Guess a letter.\n").lower()


        for position in range(word_lenght):  
            letter = random_word[position]
            if letter == guess :           
                display[position] = letter
        if guess not in random_word:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win!")
            print(lives)            
print(f"Random Word Was: {random_word}")