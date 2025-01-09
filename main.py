from model.blackjack import Blackjack
from view.gameFrame import GameFrame

import tkinter as tk

def main():
    deckCount = 6
    game = Blackjack(deckCount)
    root = tk.Tk()
    root.geometry("800x800")
    gameState = GameFrame(master=root, game=game)
    root.mainloop()

if __name__ == "__main__":
    main()