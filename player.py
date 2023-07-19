from deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def give_hand(self,deck):
        self.hand.append(deck.draw())
        self.hand.append(deck.draw())
    
    def draw_card(self, deck):
        self.hand.append(deck.draw())
    
    def return_hand(self):
        self.hand = []

    def hand_value(self):
        sum = 0

        for card in self.hand:
            if card.value > 10:
                sum += 10
            elif card.value == 1:
                sum += 11
            else:    
                sum += card.value

        if sum > 21:
            for card in self.hand:
                if card.value == 1:
                    sum -= 10
        
        return sum
    
    def show_hand(self):
        for card in self.hand:
            print(card)
    
    def show_dealer_cards(self):
        print(f'1st Card: {self.hand[0]}')

    def __str__(self):
        return self.name
