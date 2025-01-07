import tkinter as tk
from tkinter import messagebox

class GameFrame(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("blackjack")
        self.master.configure(bg="#228B22")

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
        self.optionmenu.add_command(label="Change Deck Count", command=self.deckCount)
        self.menubar.add_cascade(menu=self.optionmenu, label="Options")
        self.master.config(menu=self.menubar)

        # button creation
        self.button = tk.Button(self.container, text="Exit", font=("Arial", 20), bg="#ccffcc", fg="#353e43", command=self.exit)
        self.button.grid(row=0, column=9, sticky="ne", padx=10, pady=10)

        self.button = tk.Button(self.container, text="Hit", font=("Arial", 20), bg="#8B0000", fg="#353e43", command=self.hit)
        self.button.grid(row=7, column=9, sticky="se", padx=10, pady=10)

        self.button = tk.Button(self.container, text="Stand", font=("Arial", 20), bg="#ccffcc", fg="#353e43", command=self.stand)
        self.button.grid(row=8, column=9, sticky="se", padx=10, pady=10)

        self.button = tk.Button(self.container, text="Double", font=("Arial", 20), bg="#ccffcc", fg="#353e43", command=self.double)
        self.button.grid(row=9, column=9, sticky="se", padx=10, pady=10)

        # label creation
        self.label = tk.Label(self.container, text="Bank", font=("Arial", 20), bg="#FFFFFF", fg="#353e43")
        self.label.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

        self.label = tk.Label(self.container, text="Dealer", font=("Arial", 20), bg="#FFFFFF", fg="#353e43")
        self.label.grid(row=0, column=5, sticky="n", padx=10, pady=10)

        self.label = tk.Label(self.container, text="Dealer Cards", font=("Arial", 20), bg="#FFFFFF", fg="#353e43")
        self.label.grid(row=1, column=5, sticky="n", padx=10, pady=10)

        self.label = tk.Label(self.container, text="Player", font=("Arial", 20), bg="#FFFFFF", fg="#353e43")
        self.label.grid(row=9, column=5, sticky="s", padx=10, pady=10)

        self.label = tk.Label(self.container, text="Player Cards", font=("Arial", 20), bg="#FFFFFF", fg="#353e43")
        self.label.grid(row=8, column=5, sticky="s", padx=10, pady=10)

        self.label = tk.Label(self.container, text="Bet", font=("Arial", 20),  bg="#FFFFFF", fg="#353e43")
        self.label.grid(row=5, column=5, padx=10, pady=10)

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
            self.master.destroy()

    def hit(self):
        pass

    def stand(self):
        pass

    def double(self):
        pass

    def deckCount(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x800")
    game = GameFrame(master=root)
    root.mainloop()