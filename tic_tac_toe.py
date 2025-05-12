import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("330x400")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        self.status_label = tk.Label(self.root, text="Player X's turn", font=("Arial", 16))
        self.status_label.pack(pady=10)

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(9):
            button = tk.Button(frame, text="", font='Arial 24', width=5, height=2,
                               command=lambda i=i: self.on_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        self.reset_btn = tk.Button(self.root, text="Reset Game", font='Arial 14',
                                   bg="#444", fg="white", command=self.reset_game)
        self.reset_btn.pack(pady=15)

    def on_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player,
                                       fg="blue" if self.current_player == "X" else "red")

            if self.check_winner(self.current_player):
                self.status_label.config(text=f"Player {self.current_player} wins!")
                self.highlight_winner(self.current_player)
                self.disable_buttons()
            elif "" not in self.board:
                self.status_label.config(text="It's a draw!")
                self.disable_buttons()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self, player):
        self.winning_combo = []
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
            (0, 4, 8), (2, 4, 6)  # diagonals
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] == player:
                self.winning_combo = [a, b, c]
                return True
        return False

    def highlight_winner(self, player):
        for i in self.winning_combo:
            self.buttons[i].config(bg="lightgreen")

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.status_label.config(text="Player X's turn")
        for button in self.buttons:
            button.config(text="", state=tk.NORMAL, bg="SystemButtonFace")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
