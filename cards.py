import random

class Card:

    SUIT_MAP = {
        'D': 'Diamonds',
        'S': 'Spades',
        'C': 'Clubs',
        'H': 'Hearts'
    }

    RANK_MAP = {
        '2': "Two",
        '3': "Three",
        '4': "Four",
        '5': "Five",
        '6': "Six",
        '7': "Seven",
        '8': "Eight",
        '9': "Nine",
        '10': "Ten",
        'J': "Jack",
        'Q': "Queen",
        'K': "King",
        'A': "Ace"
    }

    COLOR_MAP = {
        'R': "Red",
        'B': "Black"
    }

    COLOR_SUIT_MAP = {
        'R':['H', 'D'],
        'B': ['S', 'C']
    }

    SUIT_COLOR_MAP = {
        'H': 'R',
        'D': 'R',
        'S': 'B',
        'C': 'B'
    }

    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.color = Card.SUIT_COLOR_MAP[suit]
        self.rank = rank

    def getSuit(self) -> str:
        return self.suit

    def getColor(self) -> str:
        return self.color

    def getRank(self) -> str:
        return self.rank

    def printCard(self):
        name = Card.RANK_MAP[self.rank] + " of " + Card.SUIT_MAP[self.suit]
        print(name)

    def getShorthand(self):
        return self.rank + self.suit

class Deck:

    SUITS = ['S', 'H', 'D', 'C']
    
    RANKS = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    COLORS = ['R','B']

    def __init__(self):
        deck = list()
        for rank in Deck.RANKS:
            for suit in Deck.SUITS:
                deck.append(Card(suit,rank))
        self.deck = deck
        self.size = len(deck)

    def getDeck(self):
        return self.deck

    def drawCards(self, numberOfDraws: int = 1) -> list:

        assert self.size >= numberOfDraws, "Deck doesn't have enough cards!"

        cardsDrawn = []
        for i in range(numberOfDraws):
            cardsDrawn.append(self.deck.pop(-1))
            self.size = self.size - 1
        
        return cardsDrawn

    def shuffleDeck(self):
        random.shuffle(self.deck)