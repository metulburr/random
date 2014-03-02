import random

class Deck:
    def __init__(self):
        self.numbers = range(2,15)
        self.suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
        self.set_deck()
        
    def set_deck(self, shuffle=True):
        self.deck = []
        for suit in self.suits:
            for number in self.numbers:
                self.deck.append((number,suit))
        if shuffle:
            self.shuffle()
            
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        if self.deck:
            return self.deck.pop()
        

players_hand = []
game = Deck()
for i in range(5):
    players_hand.append(game.deal())
print(players_hand)
print(game.deck)
