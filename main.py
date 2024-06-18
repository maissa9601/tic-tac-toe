import tkinter as tk
from tkinter import messagebox

class TicTacToeGame:
    def __init__(self):
        self.buttons = []
        self.current_player = 'X'
        self.win = False
        self.attempts = 0
        self.player_x_wins = 0
        self.player_o_wins = 0

    def place_symbol(self, row, column):
        clicked_button = self.buttons[column][row]
        if clicked_button['text'] == "":
            clicked_button.config(text=self.current_player, bg='cyan', fg='black')
            if self.check_win(self.buttons, self.current_player):
                self.show_result_message(f"Le joueur {self.current_player} a gagné !")
                if self.current_player == 'X':
                    self.player_x_wins += 1
                else:
                    self.player_o_wins += 1
                self.attempts += 1
                if self.attempts % 3 == 0:
                    self.show_final_stats()
                else:
                    self.reset_game()
            elif self.check_nul():
               self.show_result_message("Match nul !")
               self.attempts += 1
               if self.attempts % 3 == 0:
                   self.show_final_stats()
               else:
                   self.reset_game()
            else:
                self.switch_player()
                self.update_turn_label()

    def check_horizontal_win(self, board, player):
        return any(all(cell['text'] == player for cell in row) for row in board)

    def check_vertical_win(self, board, player):
        return any(all(row[i]['text'] == player for row in board) for i in range(3))

    def check_diagonal_win(self, board, player):
        return all(board[i][i]['text'] == player for i in range(3)) or \
               all(board[i][2 - i]['text'] == player for i in range(3))
    def check_nul(self):
        return all(button['text'] != "" for row in self.buttons for button in row)           

    def check_win(self, board, player):
        if (self.check_horizontal_win(board, player) or
            self.check_vertical_win(board, player) or
            self.check_diagonal_win(board, player)):
            return True
       
        return False

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def draw_grid(self, parent):
        grid_frame = tk.Frame(parent, bg='white')  # Frame pour la grille
        grid_frame.grid(row=2, columnspan=3)  # Positionnement au centre

        for column in range(3):
            buttons_in_cols = []
            for row in range(3):
                button = tk.Button(
                    grid_frame, font=("Arial", 40, "bold"),
                    width=5, height=2, bg='lightblue', fg='black',
                    command=lambda r=row, c=column: self.place_symbol(r, c)
                )
                button.grid(row=row, column=column)
                buttons_in_cols.append(button)
            self.buttons.append(buttons_in_cols)

    def reset_game(self):
        for col in self.buttons:
            for button in col:
                button.config(text="", bg='cyan', fg='black')
        self.current_player = 'X'
        self.win = False
        self.update_turn_label()

    def update_turn_label(self):
        turn_label.config(text=f"Tour du joueur : {self.current_player}", fg='black' if self.current_player == 'X' else 'blue')

    def show_result_message(self, result):
        messagebox.showinfo("Résultat", result)
        result_label.config(text=result, fg='green' if 'gagné' in result else 'black')

    def show_final_stats(self):
        result_label.config(text=f"Résultats finaux :\nJoueur X : {self.player_x_wins} victoires\nJoueur O : {self.player_o_wins} victoires", fg='black')

    def run(self, parent):
        self.draw_grid(parent)
        self.update_turn_label()

root = tk.Tk()
root.title("TicTacToe")
root.minsize(500, 500)

game = TicTacToeGame()

COLOR_BACKGROUND = "#ADD8E6"  

COLOR_BUTTON = "#4169E1"  
FONT_LABEL = ("Arial", 14)
FONT_BUTTON = ("Arial", 12, "bold")
COLOR_BACKGROUND = "#ADD8E6"  
COLOR_TEXT = "#000000" 
COLOR_BUTTON = "#4169E1"  
root.configure(bg=COLOR_BACKGROUND)

turn_label = tk.Label(root, text="", font=FONT_LABEL, fg=COLOR_TEXT, bg=COLOR_BACKGROUND)
turn_label.grid(row=0, columnspan=3)

result_label = tk.Label(root, text="", font=FONT_LABEL, fg=COLOR_TEXT, bg=COLOR_BACKGROUND)
result_label.grid(row=1, columnspan=3)

reset_button = tk.Button(root, text="Réinitialiser le jeu", font=FONT_BUTTON, bg=COLOR_BUTTON, command=game.reset_game)
reset_button.grid(row=3, columnspan=3)
game.run(root)

root.mainloop()
