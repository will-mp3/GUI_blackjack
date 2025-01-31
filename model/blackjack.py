from .deck import Deck
from .card import Card

from tkinter import messagebox

class Blackjack:

    def __init__(self, deckCount):
        # initialize all blackjack class variables
        self.deckCount = deckCount
        self.deck = Deck(self.deckCount)
        self.dealerHand, self.playerHand = [], []
        self.playerCount = 0
        self.dealerCount = 0
        self.playerChips = 100 # default bet

    def start(self):
        self.deck.shuffleDeck()

        # deal cards, in this order
        self.playerHand.append(self.deck.dealCard())
        self.dealerHand.append(self.deck.dealCard())
        self.dealerCount = self.getCount("d") # only show first card
        self.playerHand.append(self.deck.dealCard())
        self.dealerHand.append(self.deck.dealCard())

        self.playerCount = self.getCount("p")

    def getCount(self, person):
        count = 0
        hasAce = False # boolean to handle soft aces

        # count for player
        if person == "p":
            for card in self.playerHand:
                if card.card in ['Jack', 'Queen', 'King']:
                    count += 10
                elif card.card == 'Ace':
                    hasAce = True
                    count += 11
                else:
                    count += int(card.card)
            
            if count > 21 and hasAce:
                count -= 10
        
            return count

        # count to update dealer
        if person == "d":
            for card in self.dealerHand:
                if card.card in ['Jack', 'Queen', 'King']:
                    count += 10
                elif card.card == 'Ace':
                    hasAce = True
                    count += 11
                else:
                    count += int(card.card)
            
            if count > 21 and hasAce:
                count -= 10
        
            return count

    def hit(self):
        # updates player count and calls chekc player
        self.playerHand.append(self.deck.dealCard())  
        self.playerCount = self.getCount("p")
        self.checkPlayer()          
    
    def checkPlayer(self):
        # checks for player bust
        if self.playerCount > 21:
            messagebox.showinfo(title="Player Bust", message="Player Bust")

    def dealerHit(self):
        # adds card object to dealers hand and updates count
        self.dealerHand.append(self.deck.dealCard())
        self.dealerCount = self.getCount("d")

    def clear(self):
        # TODO
        self.deck = Deck(self.deckCount)
        self.dealerHand, self.playerHand = [], []
        self.playerCount = 0
        self.dealerCount = 0

    def playAgain(self):
        if self.playerChips <= 0:
            return
        choice = input("Would you like to play again? (Y/N) ")
        if choice == "Y":
            self.run()
        elif choice == "N":
            return False
        else:
            self._playAgain()