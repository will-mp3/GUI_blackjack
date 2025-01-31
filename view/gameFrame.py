from model.blackjack import Blackjack

import tkinter as tk
from tkinter import messagebox
from time import sleep
import sys

class GameFrame(tk.Frame):

    def __init__(self, master=None, game=None):
        # inherite master class
        super().__init__(master)

        # initiate master window
        self.master = master
        self.master.title("blackjack")
        self.master.configure(bg="#228B22")

        # intitiate game
        self.game = game
        self.game.start()

        # intitiate containers & widgets
        self.create_container()
        self.configure_grid()
        self.create_widgets()

    def configure_grid(self):
        # 9 x 9 grid to allow for centering
        for i in range(10):
            self.container.grid_rowconfigure(i, weight=1)
            self.container.grid_columnconfigure(i, weight=1)

    def create_container(self):
        self.container = tk.Frame(self.master, bg="#228B22", highlightbackground="#4B3621", highlightthickness=12)
        self.container.grid(row=0, column=0, rowspan=10, columnspan=10, padx=10, pady=10, sticky="nsew")

        for i in range(10):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def create_widgets(self):
        self.container.grid_propagate(False)   

        # menu bar creation
        self.menubar = tk.Menu(self.master)
        self.optionmenu = tk.Menu(self.menubar, tearoff=0)
        self.optionmenu.add_command(label="Close", command=self.exit)
        self.optionmenu.add_separator()
        # self.optionmenu.add_command(label="Change Deck Count", command=self.deckCount)
        self.menubar.add_cascade(menu=self.optionmenu, label="Options")
        self.master.config(menu=self.menubar)

        # button creation
        self.exitbutton = tk.Button(self.container, text="Exit", font=("Arial", 20), bg="#ccffcc", fg="#353e43", command=self.exit)
        self.exitbutton.grid(row=0, column=9, sticky="ne", padx=10, pady=10)

        self.hitbutton = tk.Button(self.container, text="Hit", font=("Arial", 20), bg="#8B0000", fg="#353e43", command=self.hit)
        self.hitbutton.grid(row=7, column=9, sticky="se", padx=10, pady=10)

        self.standbutton = tk.Button(self.container, text="Stand", font=("Arial", 20), bg="#ccffcc", fg="#353e43", command=self.stand)
        self.standbutton.grid(row=8, column=9, sticky="se", padx=10, pady=10)

        self.doublebutton = tk.Button(self.container, text="Double", font=("Arial", 20), bg="#ccffcc", fg="#353e43", command=self.double)
        self.doublebutton.grid(row=9, column=9, sticky="se", padx=10, pady=10)

        # label creation
        self.label = tk.Label(self.container, text="Bank", font=("Arial", 20), bg="#FFFFFF", fg="#353e43")
        self.label.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

        self.label = tk.Label(self.container, text="Dealer", font=("Arial", 20), bg="#FFFFFF", fg="#353e43")
        self.label.grid(row=0, column=5, sticky="n", padx=10, pady=10)

        self.dcount = tk.StringVar()
        self.dcount.set(str(self.game.dealerCount))
        self.label = tk.Label(self.container, textvariable=self.dcount, font=("Arial", 20), bg="#FFFFFF", fg="#353e43")
        self.label.grid(row=1, column=5, sticky="n", padx=10, pady=10)

        self.label = tk.Label(self.container, text="Player", font=("Arial", 20), bg="#FFFFFF", fg="#353e43")
        self.label.grid(row=9, column=5, sticky="s", padx=10, pady=10)

        self.pcount = tk.StringVar()
        self.pcount.set(str(self.game.playerCount))
        self.label = tk.Label(self.container, textvariable=self.pcount, font=("Arial", 20), bg="#FFFFFF", fg="#353e43")
        self.label.grid(row=8, column=5, sticky="s", padx=10, pady=10)

        self.label = tk.Label(self.container, text="Bet", font=("Arial", 20),  bg="#FFFFFF", fg="#353e43")
        self.label.grid(row=5, column=5, padx=10, pady=10)

    def exit(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.master.destroy()

    # buttons
    def hit(self):
        # call the hit method
        # all values should update within the hit method DO NOT call any exit functions
        # call check values to determine outcome
        self.game.hit()
        self.pcount.set(str(self.game.playerCount))
        

    def stand(self):
        # when hit, this calls for the player side to halt, after this button is hit the player can no longer interact.
        # check current player value and decide whether to continue.
        self.hitbutton["state"] = "disabled"
        self.doublebutton["state"] = "disabled"
        self.dealerAction()

    def double(self):
        # when hit, this calls for the player side to halt, after this button is hit the player can no longer interact.
        # check current player value and decide whether to continue.
        # and double the bet obviously
        pass

    def dealerAction(self):
        # logic for dealer action
        self.game.dealerCount = self.game.getCount("d") # show second card (see start method)
        self.dcount.set(str(self.game.dealerCount))

        if self.game.dealerCount == 21:
            # dealer blackjack
            messagebox.showinfo(title="Dealer 21", message="Dealer 21")
        elif self.game.dealerCount >= 17: # dealer stands
            if self.game.dealerCount > self.game.playerCount:
                # dealer win
                messagebox.showinfo(title="Dealer Wins", message="Dealer Wins")
            elif self.game.dealerCount < self.game.playerCount:
                # player win
                messagebox.showinfo(title="Player Wins", message="Player Wins")
            else:
                # push
                messagebox.showinfo(title="Push", message="Push")
        else: # dealer action
            while self.game.dealerCount <= 17: # action until dealer stands
                self.game.dealerHit()
                self.dcount.set(str(self.game.dealerCount))
                if self.game.dealerCount > 21:
                    # dealer bust
                    messagebox.showinfo(title="Dealer Bust", message="Dealer Bust")
                elif self.game.dealerCount < 21 and self.game.dealerCount >= 17 and self.game.dealerCount > self.game.playerCount:
                    # dealer wins 
                    messagebox.showinfo(title="Dealer Wins", message="Dealers Wins")
                elif self.game.dealerCount < 21 and self.game.dealerCount >= 17 and self.game.dealerCount < self.game.playerCount:
                    # player wins
                    messagebox.showinfo(title="Player Wins", message="Player Wins")
                elif self.game.dealerCount == self.game.playerCount:
                    # push
                    messagebox.showinfo(title="Push", message="Push")
                else:
                    continue
