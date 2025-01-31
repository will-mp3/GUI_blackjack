import tkinter as tk

class InstructionFrame:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Welcome To Blackjack")

        self.frame = tk.Frame(self.root, bg="#008000", highlightbackground="#0f4d0f", highlightthickness=8)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="HOW TO PLAY", font=("Arial", 20, "bold"), bg="#ccffcc", fg="#353e43", highlightbackground="#353e43", highlightthickness=3)
        self.label.pack(padx=10, pady=10)

        self.instructions = tk.Text(self.frame, height=13, width=35, wrap="word", font=("Arial", 16, "bold"), bg="#ccffcc", fg="#353e43")
        self.instructions.insert("1.0", "1. Place your bet: Before the cards are dealt, players must place a bet.\n\n" 
                                 "2. Receive your cards: Once all bets have been placed, the dealer will deal two cards to each player, face up.\n\n"
                                 "3. Decide to hit or stand: After receiving your two cards, you can choose to “hit” and receive additional cards or “stand” and keep your current hand.\n\n"
                                 "4. Dealer’s turn: After all players have had their turn, the dealer will reveal their face-down card and hit or stand according to predetermined rules.\n\n"
                                 "5. Determine the winner: If neither the player nor the dealer busts, the person with the highest hand value wins.\n")
        self.instructions.config(state=tk.DISABLED)
        self.instructions.pack(padx=10, pady=10)

        self.button = tk.Button(self.frame, text="Lets Go!", highlightbackground="#353e43", bg="#ccffcc", fg="#353e43", font=("Arial", 18), command=self.close)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def close(self):
        self.root.destroy()

InstructionFrame()