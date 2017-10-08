'''
Created on Sep 23, 2017

@author: Jason
'''

class Card:
    def __init__(self, face, suit):
        """
        Builds the card object with face and suit
        Args:
            None
        Returns:
            None
        """
        face = str(face)
        suit = str(suit)
        
        if (face.isdigit() and int(face) >= 2 and int(face) <= 10):
            value = int(face)
        elif (face == "J" or face == "Q" or face == "K"):
            value = 10
        elif (face == "A"):
            value = 11
        else:
            value = 0
            
        self._face = face
        self._suit = suit
        self._display = "{0}{1}".format(face, suit)
        self._value = value
        
    def getDisplay(self):
        """
        Returns the face and suit of the card
        Args:
            None
        Returns:
            string
        """
        return self._display
    
    def getValue(self):
        """
        Returns the value of the card
        Args:
            None
        Returns:
            int
        """
        return self._value
    
    def getFace(self):
        """
        Returns the face of the card
        Args:
            None
        Returns:
            string
        """
        return self._face
    
