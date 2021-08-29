import random

class Card:
    """ Defines a card that is used in the game """

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
        """Initialize the card

        Parameters
        ----------
        suit : str
            Suit of the card
        rank : str
            Rank of the card
        """
        self.suit = suit
        self.color = Card.SUIT_COLOR_MAP[suit]
        self.rank = rank

    def printCard(self):
        """Prints the full name of the card
        """
        name = Card.RANK_MAP[self.rank] + " of " + Card.SUIT_MAP[self.suit]
        print(name)

    def getShorthand(self) -> str:
        """Get the shorthand name of the card

        Returns
        -------
        str
            Shorthand name of the card
        """
        return self.rank + self.suit

class Deck:
    """This class defines a deck that is used in the game """

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
        """Initialize a deck of 52 cards """
        deck = list()
        for rank in Deck.RANKS:
            for suit in Deck.SUITS:
                deck.append(Card(suit,rank))
        self.deck = deck
        self.size = len(deck)

    def getDeck(self) -> list:
        """Returns the current deck

        Returns
        -------
        list
            list of objects of type Card
        """
        return self.deck

    def drawCards(self, numberOfDraws: int = 1) -> list:
        """Draw a given number of cards from the top of the deck

        Parameters
        ----------
        numberOfDraws : int, optional
            Number of cards to be drawn, by default 1

        Returns
        -------
        list
            List of cards drawn, of type Card
        """

        assert self.size >= numberOfDraws, "Deck doesn't have enough cards!"

        cardsDrawn = []
        for i in range(numberOfDraws):
            cardsDrawn.append(self.deck.pop(-1))
            self.size = self.size - 1
        
        return cardsDrawn

    def shuffleDeck(self):
        """Shuffle the deck
        """
        random.shuffle(self.deck)