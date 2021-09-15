from phrase import Phrase
from valid_charachters import Valid_charachters

import random


class Game ():
    def __init__(self):
        self.missed = 0 
        self.phrases = ['Citizen Kane', 'Knives Out', 'Casablanca', 'Black Panther', 'Modern Times',
                        'The Wizard of Oz', 'Parasite', 'Get Out', 'The Godfather', 'Wonder Woman', 'A Quiet Place',
                        'Dunkirk', 'Arrival', 'Logan', 'The Adventures of Robin Hood', 'Alien', 'La La Land',
                        'The Maltese Falcon', 'Psycho', 'Baby Driver', 'Goodfellas', 'Tombstone', 'Chef']
        self.active_phrase = ''
        self.guesses = set()


    def start(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        self.game_phrase = Phrase (self.active_phrase)
        while True:
            self.game_phrase.display()
            print(f'you have {self.missed} strikes!!')
            self.get_guess()
            self.check = self.game_phrase.check_complete()
            if self.check == 'complete':
                self.game_over ('win')
                continue
            elif self.check == 'not complete':
                if self.missed == 5:
                    self.game_over('lose')
                    continue
                else:
                    continue


    def get_random_phrase (self):
        self.random_phrase = random.choice(self.phrases)
        return self.random_phrase


    def welcome (self):
        print("""
        WELCOME TO THE PHRASE HUNTER GAME!!!!
        INSTRUCTIONS:         
        - A random phrase will be displayed on as a series of "_". 
        - Your objective is to guess the hidden letters represented by the "_"
        - If you guess a letter that is in the phrase, it will be revealed.
        - If you guess a incorrect letter , you will recieve a strike.
        - After 5 strikes, it's GAME OVER!!
        - ***HINT...  all of the phrases are movie titles...   
        
        """)


    def get_guess (self):
        guess = input ('What letter would you like to guess?    ')
        while True:
            if len(guess) > 1:
                print('This is an invalid guess, please choose 1 character...')
                return
            if guess.lower() not in Valid_charachters:
                print('This is an invalid guess, please choose a letter... not a number...')
                return
            else:
                break
        if guess in self.game_phrase.phrase_set:
            self.guesses.add(guess)
            self.game_phrase.phrase_correct_letters.add(guess)
        elif guess not in self.game_phrase.phrase_set:
            self.missed += 1 


    def game_over (self, outcome):
        if outcome == 'win':
            print (f"""Congratulations! YOU WON!!!
                    The phrase was {self.active_phrase}""")
        elif outcome == 'lose':
            print(f"""I'm sorry, but you lost! The hidden Phrase was {self.active_phrase}, Better luck next time! """)
        
        while True:
            play_again = input('Would you like to play again? (Y/N)     ')
            if play_again.upper() == "Y":
                self.start()
                break
            elif play_again.upper() == "N":
                print('Thanks for playing!...Ending game now...')
                quit()
            else:
                print("Hmm, that doesnt seem to be a valid answer , please try again...")
                continue
