import tkinter as tk

class InstructionFrame:

    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="WELCOME TO BLACKJACK", font=("Arial", 20))
        self.label.pack(padx=10, pady=10)

        self.root.mainloop()

InstructionFrame()