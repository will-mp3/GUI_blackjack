from .deck import Deck
from .card import Card

import sys
import tkinter as tk
from tkinter import messagebox

from time import sleep

class Blackjack:

    def __init__(self, deckCount):
        self.deckCount = deckCount
        self.deck = Deck(self.deckCount)
        self.dealerHand, self.playerHand = [], []
        self.playerCount = 0
        self.dealerCount = 0
        self.playerChips = 100

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
        hasAce = False

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
        self.playerHand.append(self.deck.dealCard())  
        self.playerCount = self.getCount("p")
        self.checkPlayer()          
    
    def checkPlayer(self):
        if self.playerCount > 21:
            messagebox.showinfo(title="Player Bust", message="Player Bust")

    def dealerHit(self):
        self.dealerHand.append(self.deck.dealCard())
        self.dealerCount = self.getCount("d")

    def clear(self):
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