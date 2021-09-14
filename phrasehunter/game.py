from phrase import Phrase
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
        while self.missed < 5 and self.guesses != self.game_phrase.phrase_set:
            self.game_phrase.display()
            print(f'you have {self.missed} strikes!!')
            self.get_guess()
            
        if self.guesses == 5:
            self.game_over('lose')
        elif self.guesses == self.game_phrase.phrase_set:
            self.game_over('win')


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
        if guess in self.game_phrase.phrase_set:
            self.guesses.add(guess)
            self.game_phrase.phrase_correct_letters.add(guess)
        elif guess not in self.game_phrase.phrase_set:
            self.missed += 1 

    def game_over (self, outcome):
        if outcome == 'win':
            print ('Congratulations! YOU WON!!!')
        elif outcome == 'lose':
            print("""I'm sorry, but you lost! Better luck next time! """)


while __name__ == "__main__":
    new_game = Game()
    new_game.start()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # self.words = start_phrase.new_phrase
        # self.set_of_letters = start_phrase.set_of_charechters
        # self.letters_total = start_phrase.letters
        # self.locations_of_letters =''
        # self.strikes= 5 
        
#     def opening_display(self):
#         print ("""
#         WELCOME TO THE PHRASE HUNTER GAME!!!!

#         INSTRUCTIONS:
#         - A random phrase will be displayed on as a series of "_". 
#         - Your objective is to guess the hidden letters represented by the "_"
#         - If you guess a letter that is in the phrase, it will be revealed.
#         - If you guess a incorrect letter , you will recieve a strike.
#         - After 5 strikes, it's GAME OVER!!
#         - ***HINT...  all of the phrases are movie titles...   
        
#         """)
#     # def start_game_question(self):
#     #     while True:
#     #         start_answer = input('Are you ready to play? (Y/N)...     ')
#     #         if start_answer.upper() == 'Y':
#     #             self.start_game()
#     #         elif start_answer.upper() == 'N':
#     #             quit()
#     #         else:
#     #             print ("Hmmm... the input you gave doesnt make sense , please try again!....")
#     #             continue
#     def set_game_board(self):
#         self.gameboard_key_list = []
#         self.gameboard_hidden_list = []
#         for letter in self.letters_total:
#             self.gameboard_key_list.append(letter)
#         for letter in self.gameboard_key_list:
#             if letter == ' ':
#                 self.gameboard_hidden_list.append(' ')
#                 continue
#             self.gameboard_hidden_list.append('_')
        
#         print (self.gameboard_hidden_list)
#     def display_gameboard(self):
#         self.hidden_word_display = ' '.join(
#             [str(letter) for letter in self.gameboard_hidden_list])
#         print(self.hidden_word_display)


#     def quess_letter(self):
#         guess = input('What letter would you like to guess?   ')
#         if guess in start_phrase.set_of_charechters:
#             print('Good Guess!! that letter was correct...')
            
#         elif guess not in start_phrase.set_of_charechters:
#             self.strikes -= 1
#             print (f"""That was an incorrect guess, please guess again.
#                 you now have {self.strikes} strikes remaining! """)



    
    
    
    
#     # def start_game(self):
#     #     game_running = True
        


# start_phrase = Phrase()
# new_game = Game()
# new_game.opening_display()
# new_game.set_game_board()
# new_game.display_gameboard()
