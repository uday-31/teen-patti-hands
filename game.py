from cards import Deck
import numpy as np
import itertools
import random

def getHandRankings():    
    rankings = {}
    
    names = {}

    suits = Deck.SUITS
    ranks = Deck.RANKS
    ranksInv = {val:key for key,val in ranks.items()}

    rank = 1

    existingHands = set()

    # Three of a kind (trail)
    for item in list(ranks.keys())[-1::-1]:
        cards = [(item+suit) for suit in suits]
        members = list(itertools.combinations(cards,3))
        for member in members:
            hand = frozenset(member)
            rankings[hand] = rank
            names[hand] = item+" trail"
            existingHands.add(hand)

        rank+=1

    # Straight flush (pure sequence)
    for item in ['A']:
        for suit in suits:
            cards = [(item2+suit) for item2 in ['A','K','Q']]
            hand = frozenset(cards)
            rankings[hand] = rank
            names[hand] = 'A'+'-'+'K'+'-'+'Q'+" straight flush"
            existingHands.add(hand)

        rank+=1
        for suit in suits:
            cards = [(item2+suit) for item2 in ['A','2','3']]
            hand = frozenset(cards)
            rankings[hand] = rank
            names[hand] = 'A'+'-'+'2'+'-'+'3'+" straight flush"
            existingHands.add(hand)

        rank+=1
    for item in range(13,3,-1):
        for suit in suits:
            cards = [ranksInv[item]+suit, ranksInv[item-1]+suit, ranksInv[item-2]+suit]
            hand = frozenset(cards)
            rankings[hand] = rank
            names[hand] = ranksInv[item]+'-'+ranksInv[item-1]+'-'+ranksInv[item-2]+" straight flush"
            existingHands.add(hand)
        rank+=1


    # Straight (sequence)
    for item in ['A']:
        one = ['A'+suit for suit in suits]
        two = ['K'+suit for suit in suits]
        three = ['Q'+suit for suit in suits]
        full = [one,two,three]
        cards = set(itertools.product(*full))
        cards = {frozenset(item2) for item2 in cards}
        cards = cards.difference(existingHands)

        for hand in cards:
    
            rankings[frozenset(hand)] = rank
            names[hand] = 'A'+'-'+'K'+'-'+'Q'+" straight"
            existingHands.add(frozenset(hand))

        rank+=1


        one = ['A'+suit for suit in suits]
        two = ['2'+suit for suit in suits]
        three = ['3'+suit for suit in suits]
        full = [one,two,three]
        cards = frozenset(itertools.product(*full))
        cards = {frozenset(item2) for item2 in cards}
        cards = cards.difference(existingHands)

        for hand in cards:
            rankings[frozenset(hand)] = rank
            names[hand] = 'A'+'-'+'2'+'-'+'3'+" straight"
            existingHands.add(frozenset(hand))
        rank+=1

    for item in range(13,3,-1):
        one = [ranksInv[item]+suit for suit in suits]
        two = [ranksInv[item-1]+suit for suit in suits]
        three = [ranksInv[item-2]+suit for suit in suits]
        full = [one, two, three]
        cards = frozenset(itertools.product(*full))
        cards = {frozenset(item2) for item2 in cards}
        cards = cards.difference(existingHands)
        
        for hand in cards:
            rankings[frozenset(hand)] = rank
            names[hand] = ranksInv[item]+'-'+ranksInv[item-1]+'-'+ranksInv[item-2]+" straight flush"
            existingHands.add(frozenset(hand))
        rank+=1

    # Flush (color)
    for top in range(14,4, -1):
        for mid in range(top-1, 2, -1):
            if top-mid==1:
                for low in range(mid-2, 1, -1):
                    for suit in suits:
                        cards=[ranksInv[top]+suit, ranksInv[mid]+suit, ranksInv[low]+suit]
                        hand = frozenset(cards)
                        names[hand] = ranksInv[top]+"-top flush"
                        rankings[hand] = rank
                        rank+=1
                        existingHands.add(hand)
            else:
                for low in range(mid-1, 1, -1):
                    if ((top==14 and mid==3) and (low==2)):
                        continue
                    else:
                        for suit in suits:
                            cards=[ranksInv[top]+suit, ranksInv[mid]+suit, ranksInv[low]+suit]
                            hand = frozenset(cards)
                            names[hand] = ranksInv[top]+"-top flush"
                            rankings[hand] = rank
                            rank+=1
                            existingHands.add(hand)

    # Pair
    for pair in range(14,1, -1):
        for top in range(14,1, -1):
            if pair==top:
                continue
            else:
                cards = [(ranksInv[pair]+suit) for suit in suits]
                oneTwo = list(itertools.combinations(cards,2))
                three = [ranksInv[top]+suit for suit in suits]
                full = [oneTwo, three]
                cards = list(itertools.product(*full))
                cards = frozenset([(item[0][0],item[0][1],item[1]) for item in cards])
                for hand in cards:
                    hand = frozenset(hand)
                    rankings[hand] = rank
                    names[hand] = ranksInv[pair]+" pair"
                    rank+=1
                    existingHands.add(hand)

    # No pair (high card)
    for top in range(14,4, -1):
        for mid in range(top-1, 2, -1):
            if top-mid==1:
                for low in range(mid-2, 1, -1):
                    one = [ranksInv[top]+suit for suit in suits]
                    two = [ranksInv[mid]+suit for suit in suits]
                    three = [ranksInv[low]+suit for suit in suits]
                    full = [one,two,three]
                    cards = frozenset(itertools.product(*full))
                    cards = {frozenset(item2) for item2 in cards}
                    cards = cards.difference(existingHands)
                    for hand in cards:
                        hand = frozenset(hand)
                        names[hand] = ranksInv[top]+"-top"
                        rankings[hand] = rank
                        existingHands.add(hand)
                    rank+=1
                        
            else:
                for low in range(mid-1, 1, -1):
                    if ((top==14 and mid==3) and (low==2)):
                        continue
                    else:
                        one = [ranksInv[top]+suit for suit in suits]
                        two = [ranksInv[mid]+suit for suit in suits]
                        three = [ranksInv[low]+suit for suit in suits]
                        full = [one,two,three]
                        cards = frozenset(itertools.product(*full))
                        cards = {frozenset(item2) for item2 in cards}
                        cards = cards.difference(existingHands)
                        for hand in cards:
                            hand = frozenset(hand)
                            rankings[hand] = rank
                            names[hand] = ranksInv[top]+"-top"
                            existingHands.add(hand)
                        rank+=1

    return rankings,names


class Game:

    HAND_RANKINGS, HAND_NAMES = getHandRankings()

    def __init__(self, noOfPlayers: int, jokers: list = None, handSize: int = 3):
        self.noOfPlayers = noOfPlayers
        self.deck = Deck()
        self.jokers = jokers
        self.handSize = handSize
        self.hands = self.generateHands()

    def generateHands(self):
        self.deck.shuffleDeck()
        hands = []
        handsShorthand = []
        for _ in range(self.noOfPlayers):
            hands.append([])
        for _ in range(self.handSize):
            for i in range(self.noOfPlayers):
                hands[i].append(self.deck.drawCards(1)[0])

        for i in range(self.noOfPlayers):
            hands[i] = frozenset([item.getShorthand() for item in hands[i]])

        return hands

    def simulateGame(self):
        results = {item:np.array([0,0,1]) for item in self.hands}
        ranks = np.array([Game.HAND_RANKINGS[hand] for hand in self.hands])
        minIndices = np.where(ranks == ranks.min())[0]
        if len(minIndices)==1:
            win=1
            tie=0
        else:
            win=0
            tie=1
        for item in minIndices:
            results[self.hands[item]]=np.array([win,tie,1])
        return results


