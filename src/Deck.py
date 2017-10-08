'''
Created on Sep 23, 2017

@author: Jason
'''

from Card import Card
import random

class Deck:
    NUMBERS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    SUITS = ["H", "D", "C", "S"]
    
    def __init__(self):
        """
        Builds the deck of cards with numbers and suits
        Args:
            None
        Returns:
            None
        """
        self._cards = []
        for number in self.NUMBERS:
            for suit in self.SUITS:
                self._cards.append(Card(number, suit))
                
    def shuffle(self):
        """
        Shuffles the cards in the deck into a random order
        Args:
            None
        Returns:
            None
        """
        random.shuffle(self._cards)
    
    def dealCard(self):
        """
        Removes a card from the deck
        Args:
            None
        Returns:
            Card object
        """
        deltCard = self._cards.pop()
        return deltCard
