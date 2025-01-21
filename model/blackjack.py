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
        self.playerHand.append(self.deck.dealCard())
        self.dealerHand.append(self.deck.dealCard())

        self.playerCount = self.getCount("p")
        self.dealerCount = self.getCount("d")

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
            sys.exit()

    def dealerHit(self):
        self.dealerHand.append(self.deck.dealCard())
        self.dealerCount = self.getCount("d")

    def dealerAction(self):
        if self.dealerCount == 21:
            messagebox.showinfo(title="Dealer 21", message="Dealer 21")
            sys.exit()
        elif self.dealerCount >= 17:
            if self.dealerCount > self.playerCount:
                messagebox.showinfo(title="Dealer Wins", message="Dealer Wins")
                sys.exit()
            elif self.dealerCount < self.playerCount:
                messagebox.showinfo(title="Player Wins", message="Player Wins")
                sys.exit()
            else:
                messagebox.showinfo(title="Push", message="Push")
                sys.exit()
        else:
            while self.dealerCount <= 17:
                sleep(2.0)
                self._dealerHit()
                if self.dealerCount > 21:
                    messagebox.showinfo(title="Dealer Bust", message="Dealer Bust")
                    sys.exit()
                elif self.dealerCount < 21 and self.dealerCount >= 17 and self.dealerCount > self.playerCount: 
                    messagebox.showinfo(title="Dealer Wins", message="Dealers Wins")
                    sys.exit()
                elif self.dealerCount < 21 and self.dealerCount >= 17 and self.dealerCount < self.playerCount:
                    messagebox.showinfo(title="Player Wins", message="Player Wins")
                    sys.exit()
                elif self.dealerCount == self.playerCount:
                    messagebox.showinfo(title="Push", message="Push")
                    sys.exit()
                else:
                    continue

    def clear(self):
        self.deck = Deck(self.deckCount)
        self.dealerHand, self.playerHand = [], []
        self.playerCount = 0
        self.dealerCount = 0

    def _playAgain(self):

        if self.playerChips <= 0:
            return
        choice = input("Would you like to play again? (Y/N) ")
        if choice == "Y":
            self.run()
        elif choice == "N":
            return False
        else:
            self._playAgain()

    def _cardEval(self):

        if self.playerCount <= 21:
            return True
        else:
            return False

    def _checkBJ(self):

        if self.playerCount == 21:
            return True
        else:
            return False


    def run(self):
        self._clear()

        print()
        print("You have", self.playerChips, "chips")
        print()

        self.deck.shuffleDeck()
        print("Welcome to the table! Please take a seat and place your bets.")
        print()
        while 1:
            bet = input("BET AMOUNT: ")
            print()
            bet = int(bet)
            if bet <= self.playerChips:
                break
            else:
                print("Invalid bet amount.")
                print()
                continue

        # deal cards, in this order
        self.playerHand.append(self.deck.dealCard())
        self.dealerHand.append(self.deck.dealCard())
        self.playerHand.append(self.deck.dealCard())
        self.dealerHand.append(self.deck.dealCard())

        print("The dealer is showing a", self.dealerHand[0].printCard())
        print()
        print("You have", self.playerHand[0].printCard() + ",", self.playerHand[1].printCard())
        self.playerCount = self._getCount("p")
        self.dealerCount = self._getCount("d")

        if self._checkBJ():
            playerChips += bet * 1.5
            choice = self._playAgain()
            if not choice:
                return

        # hit or stand logic
        while 1:
            print()
            move = input("Would you like to hit, stand, or double: (H/S/D) ")
            print()
            if move == "H":
                val = self._hit()
                if val:
                    continue
                else:
                    break

            elif move == "S":
                break

            elif move == "D":
                if (bet * 2) <= self.playerChips:
                    bet = bet * 2
                    self.playerHand.append(self.deck.dealCard())
                    print("You have", self.playerHand[0].printCard() + ",", self.playerHand[1].printCard(), ",", self.playerHand[2].printCard())
                    print()
                    self.playerCount = self._getCount("p")
                    break
            else:
                print("Invalid response, please respond again.")
                print()
        
        if self.playerCount > 21:
            self.playerChips -= bet
            self._playAgain()

        self._dealerAction(bet)