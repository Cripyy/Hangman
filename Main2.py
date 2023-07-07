import random, sys, time
from typing import List

print('Welcome to the game of hangman!')

wordlist = ['noroff', 'digital', 'forensics', 'computer', 'windows', 'police', 'dick', 'vagina', 'sex', 'dirty']
letters_used = []
guessed_word = []

def main_def():
    main_input = input('Would you like to start the game?\n')
    if main_input.lower() == 'y' or main_input.lower() == 'yes':
        hangman()
    if main_input.lower() == 'n' or main_input.lower() == 'no':
        time.sleep(1.5)
        sys.exit()


def hangman():

    computer_word = random.choice(wordlist)
    print(len(computer_word))
    for characters in computer_word:
        guessed_word.append('-')


if __name__ == "__main__":
    main_def()
