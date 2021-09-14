import random



class Phrase():

    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.phrase_set = set(self.phrase)
        self.phrase_correct_letters = set()


    def display(self):
        self.phrase_hidden_list = []
        for letter in self.phrase:
            if letter == ' ':
                self.phrase_hidden_list.append(' ')
                continue
            elif letter in self.phrase_correct_letters:
                self.phrase_hidden_list.append(letter)
                continue
            self.phrase_hidden_list.append('_')
        self.display_string = ' '.join(
            [str(letter) for letter in self.phrase_hidden_list])
        print(self.display_string)


    def check_letter(self, letter):
        phrase_set = set(self.phrase)
        if letter in phrase_set:
            return True
        else:
            return False


    def check_complete(self):
        if Game.guesses == phrase_set:
            game.game_over(win)
        elif Game.missed == 5:
            game.game_over(lose)
        else:
            return 'keep playing'
    
new_phrase = Phrase('The quick and the dead')
new_phrase.display()
result = new_phrase.check_letter ('v')
print(result)
# self.possible_phrases = Phrase.phrase_bank
# self.new_phrase = random.choice(self.possible_phrases)
# self.num_of_charechters = len(self.new_phrase)
# self.letters = list(self.new_phrase)
# self.set_of_charechters = set(self.new_phrase)
