import random

class Deck:
    def __init__(self):
        self.numbers = range(2,15)
        self.suits = ['Diamonds', 'Clubs', 'Spades', 'Hearts']
        self.deck = self.new_deck()
    def new_deck(self):
        d = {}
        for suit in self.suits:
            d[suit] = list(self.numbers)
        return d
    def deal_one(self):
        while True:
            suit = random.choice(self.suits)
            num = random.choice(list(self.numbers))
            try:
                self.deck[suit].remove(num)
            except ValueError:
                continue
            return (num, suit)
    def format_display(self, num):
        if num == 11:
            return 'Jack'
        elif num == 12:
            return 'Queen'
        elif num == 13:
            return 'King'
        elif num == 14:
            return 'Ace'
            
game = Deck()
print(game.deck)
for i in range(10):
    print(game.deal_one())
print(game.deck)
