from cards import Card  
import random

class Deck:
    def __init__(self):
        self.deck = []
        self.top_of_deck = len(self.deck) - 1

        for i in range(1,14):
            for j in range(0,4):    
                if j == 0:
                    self.deck.append(Card('Spades', i))
                if j == 1:
                    self.deck.append(Card('Hearts', i))
                if j == 2:
                    self.deck.append(Card('Diamonds', i))
                else:
                    self.deck.append(Card('Clubs', i))

    def shuffle(self):
        random.shuffle(self.deck)
        self.top_of_deck = len(self.deck) - 1
        

    def draw(self):
        card = self.deck[self.top_of_deck]
        self.top_of_deck -= 1

        return card
    
    def show_deck(self):
        for card in self.deck:
            print(card)