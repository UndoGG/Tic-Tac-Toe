
import tkinter as tk

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Крестики-нолики")
        self.board = [[" " for j in range(3)] for i in range(3)]
        self.buttons = [[tk.Button(master, text="", width=4, height=2, font=("Helvetica", 30),
                                    command=lambda i=i, j=j: self.move(i, j)) for j in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)
        self.current_player = "X"
        self.message = tk.Label(master, text="Ходит игрок " + self.current_player,
                                font=("Helvetica", 20), pady=10)
        self.message.grid(row=3, columnspan=3)

    def move(self, i, j):
        if self.board[i][j] == " ":
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_win():
                self.message.config(text="Игрок " + self.current_player + " выиграл!")
                for i in range(3):
                    for j in range(3):
                        self.buttons[i][j].config(state=tk.DISABLED)
            elif self.check_draw():
                self.message.config(text="Ничья!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.message.config(text="Ходит игрок " + self.current_player)

    def check_win(self):
        board = self.board
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != " ":
                return True
            if board[0][i] == board[1][i] == board[2][i] != " ":
                return True
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return True
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return True
        return False

    def check_draw(self):
        board = self.board
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    return False
        return not self.check_win()
        
root = tk.Tk()
app = Game(root)
root.mainloop()