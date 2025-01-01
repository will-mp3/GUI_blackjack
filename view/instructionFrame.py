import tkinter as tk

class InstructionFrame:

    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="WELCOME TO BLACKJACK", font=("Arial", 20))
        self.label.pack(padx=10, pady=10)

        self.instructions = tk.Text(self.root, height=10, width=40, wrap="word")
        self.instructions.insert("1.0", "Fill Instructions Here")
        self.instructions.config(state=tk.DISABLED)
        self.instructions.pack(pady=10)

        self.button = tk.Button(self.root, text="Lets Go!", font=("Arial", 18), command=self.close)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def close(self):
        self.root.destroy()

InstructionFrame()