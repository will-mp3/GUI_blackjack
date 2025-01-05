import tkinter as tk
from tkinter import messagebox

class GameFrame:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Blackjack")

        self.frame = tk.Frame(self.root, bg="#008000", highlightbackground="#0f4d0f", highlightthickness=8)
        self.frame.pack()

        # menu bar creation
        self.menubar = tk.Menu(self.root)
        self.optionmenu = tk.Menu(self.menubar, tearoff=0)
        self.optionmenu.add_command(label="Force Close", command=exit)
        self.optionmenu.add_separator()
        self.optionmenu.add_command(label="Change Deck Count", command=self.deckCount)
        self.menubar.add_cascade(menu=self.optionmenu, label="Options")
        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="WELCOME TO BLACKJACK", font=("Arial", 20))
        self.label.pack(padx=10, pady=10)

        self.root.mainloop()

    def table(self):
        # create exit, hit, stand, and double buttons for player interaction
        # organize table to contain:
        # - player bank in top left, showing current chip count
        # - the four initialized buttons with exit in the top right and the three action buttons in the bottom right, stacked
        # - a window to display the dealers cards top center, with room to display cards to come
        # - a similar window to displayer the players cards bottom center with the same display technology
        # - inbetween the two sets of cards, the current bet on the table
        pass

    def exit(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    def hit(self):
        pass

    def stand(self):
        pass

    def double(self):
        pass

    def deckCount(self):
        pass

GameFrame()