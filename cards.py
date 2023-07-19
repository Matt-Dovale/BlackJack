class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        faces = {
            1: 'Ace',
            11: 'Jack',
            12: 'Queen',
            13: 'King'
        }

        if self.value == 1 or self.value >= 11:
            return f'{faces[self.value]} of {self.suit}'
             
        return f'{self.value} of {self.suit}'