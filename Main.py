import random

def main_menu():
    play_again = True

    hangman = (
        '''
        -----
        |   |
        |
        |
        |
        |
        |
        |
        |
        --------
        ''',
        '''
        -----
        |   |
        |   0
        |
        |
        |
        |
        |
        |
        --------
        ''',
        '''
        -----
        |   |
        |   0
        |  -+-
        |
        |
        |
        |
        |
        --------
        ''',
        '''
        -----
        |   |
        |   0
        | /-+-
        |
        |
        |
        |
        |
        --------
        ''',
        '''
        -----
        |   |
        |   0
        | /-+-\ 
        |
        |
        |
        |
        |
        --------
        ''',
        '''
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |
        |
        |
        |
        --------
        ''',
        '''
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |
        |
        |
        --------
        ''',
        '''
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |  |
        |
        |
        --------
        ''',
        '''
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |  | 
        |  | 
        |
        --------
        ''',
        '''
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |  | | 
        |  | 
        |
        --------
        ''',
        '''
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |  | | 
        |  | | 
        |
        --------
        ''')
    word_list = []
    play_again = True
    print('\nWelcome to Hangman\n'
          'The game works like regular hangman, guess letters to find the word\n')
    print('Choose difficulty')
    user_input = input('1. Easy\n'
                       '2. Medium\n'
                       '3. Hard\n'
                       'Choice: ')
    if user_input.lower() == ('1' or 'easy'):
        while play_again:
            words = open('word_list.txt')
            chosen_word = random.choice(words).lower()
            player_guess = None
            guessed_letters = []
            guessed_word = []
            for letter in chosen_word:
                guessed_word.append('-')
            joined_word = None
            print(hangman[0])
            attempts = len(hangman) - 1

            while attempts != 0 and '-' in guessed_word:
                print('\nYou have {} attempts remaining').format(attempts)
                joined_word = ''.join(guessed_word)
                print(joined_word)

                try:
                    player_guess = str(input('\nPlease select a letter between A and Z\n'))
                except:
                    print('That is not a valid input')
                    continue
                else:
                    if not player_guess.isalpha():
                        print('That is not a letter')
                        continue
                    elif len(player_guess) > 1:
                        print('Too many letters')
                        continue
                    elif player_guess in guessed_letters:
                        print('You have already tried that letter')
                    else:
                        pass

                guessed_letters.append(player_guess)

                for letter in range(len(chosen_word)):
                    if player_guess == chosen_word[letter]:
                        guessed_word[letter] = player_guess
                    if player_guess not in chosen_word:
                        attempts -= 1
                        print(hangman[(len(hangman) - 1) - attempts])

            if '-' not in guessed_word:
                print('Congratulations, the word was {}').format(chosen_word)
            else:
                print('Sorry, the word was {}').format(chosen_word)

            print('Would you like to play again?')

            response = input('> ')
            if response not in ('yes' or 'y'):
                play_again = False


main_menu()
