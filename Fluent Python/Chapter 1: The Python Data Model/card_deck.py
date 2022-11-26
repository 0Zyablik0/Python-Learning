import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['spades', 'diamonds', 'clubs', 'hearts']

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card(7, 'diamonds')
print(beer_card)


deck = FrenchDeck()
print(len(deck))

print(deck[0], deck[-1])

print(choice(deck))
print(choice(deck))
print(choice(deck))


print(deck[:3])
print(deck[12::13])

for card in deck:
    print(card)

for card in reversed(deck):
    print(card)
    
    
print(Card('Q', 'hearts') in deck)
print(Card('S', 'hearts') in deck)

