'''
Created on Sep 23, 2017

@author: Jason
'''

from Deck import Deck
from Player import Player
import time

def printBreak():
    print()
    print("-------------------------------------------------")
    print()
    
def getBet(bank):
    print("BANK: %.2f" % float(bank))
    accepted = False
    
    while not accepted:
        bet = input("Place your bet (q - Quit):")
        if bet.upper() == "Q":
            break
        elif not bet.isdigit():
            print("You must enter a number.")
        elif float(bet) > float(bank):
            print("You cannot bet more than what is in your bank.")
        else:
            accepted = True
        
    printBreak()
    return bet
    
def printHands(playerCards, dealerCards, hideDealer=True):
    playerHand = ""
    playerScore = 0
    dealerHand = ""
    dealerScore = 0
    
    for card in dealerCards:
        dealerHand += card.getDisplay() + " "
        dealerScore += card.getValue()
    for card in playerCards:
        playerHand += card.getDisplay() + " "
        playerScore += card.getValue()
    
    for card in dealerCards:
        if card.getFace() == "A" and dealerScore > 21:
            dealerScore -= 10

    for card in playerCards:            
        if card.getFace() == "A" and playerScore > 21:
            playerScore -= 10
        
    if hideDealer:
        dealerOutput = dealerCards[0].getDisplay() + " ** (**)"
    else:
        dealerOutput = dealerHand + " ({0})".format(dealerScore)
        
    print("DEALER cards: %s " % dealerOutput)
    print()
    print("  Your cards: %s (%d)" % (playerHand, playerScore))
    print()
    
    return playerScore, dealerScore
    
def main():
    print("Welcome to Text Blackjack!")
    name = input("Enter your name: ")
    printBreak()

    player = Player(name)
    
    bet = getBet(player.bank)
    
    while (bet.upper() != "Q"):
        player.bank -= float(bet)
        deck = Deck()
        deck.shuffle()
        
        playerCards = []
        playerScore = 0
        dealerCards = []
        dealerScore = 0
        
        playerCards.append(deck.dealCard())
        dealerCards.append(deck.dealCard())
        playerCards.append(deck.dealCard())
        dealerCards.append(deck.dealCard())
        
        playerScore, dealerScore = printHands(playerCards, dealerCards)
        
        if playerScore == 21:
            player.bank += float(bet) + (float(bet) * 1.5)
            print("*** YOU GOT BLACKJACK!")
            printBreak()
        else:
            choice = input("Hit (h) or Stand (s)? ")
            printBreak()
            
            while (choice.upper() != "S"):
                if choice.upper() == "H":
                    playerCards.append(deck.dealCard())
                    playerScore, dealerScore = printHands(playerCards, dealerCards)
                
                if playerScore > 21:
                    print("*** YOU BUSTED!")
                    printBreak()
                    break
                else:
                    choice = input("Hit (h) or Stand (s)? ")
                    printBreak()
            
            if playerScore <= 21:
                playerScore, dealerScore = printHands(playerCards, dealerCards, False)
                while dealerScore < 17:
                    print("Dealer hits...")
                    printBreak()
                    time.sleep(3)
                    
                    dealerCards.append(deck.dealCard())
                    playerScore, dealerScore = printHands(playerCards, dealerCards, False)
                    
                    if dealerScore > 21:
                        player.bank += float(bet) * 2
                        print("*** DEALER BUSTED, YOU WIN!")
                        printBreak()
                        break
            
            if playerScore <= 21 and dealerScore <= 21:
                if playerScore > dealerScore:
                    player.bank += float(bet) * 2
                    print("*** YOU WON!")
                    printBreak()
                elif playerScore < dealerScore:
                    print("*** YOU LOST!")
                    printBreak()
                elif playerScore == dealerScore:
                    player.bank += float(bet)
                    print("*** YOU PUSHED.")
                    printBreak()
                
        
        bet = getBet(player.bank)

    print()
    print("Thank you for playing!")
    
    player.saveBank()
    
    
main()