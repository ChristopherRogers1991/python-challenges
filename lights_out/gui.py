import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter.constants import S, YES
from typing import Callable, List
from answer import Light, Board

class LightButton(tk.Button):
    def __init__(self, master, board: Board, row: int, column: int, handle_click: Callable) -> None:
        self.board = board
        self.row = row
        self.column = column
        self.hande_click = handle_click
        self.light = board.lights[row][column]
        super().__init__(master=master, command=self.on_click, height=5, width=10, activebackground=self.get_background())
        self.draw()

    def get_background(self):
        if self.light.on:
            return "yellow"
        return "black"

    def draw(self):
        self.configure(bg=self.get_background(), activebackground=self.get_background())

    def on_click(self):
        self.board.toggle_light(self.row, self.column)
        self.hande_click()

class LightBoard(tk.Frame):
    def __init__(self, master, board: Board) -> None:
        self.board = board
        self.buttons: List[LightButton] = []
        super().__init__(master=master)
        for row_index, lights in enumerate(board.lights):
            for column_index, _light in enumerate(lights):
                new_button = LightButton(self, board, row_index, column_index, self.handle_click)
                new_button.grid(row=row_index, column=column_index)
                self.buttons.append(new_button)

    def draw(self):
        for button in self.buttons:
            button.draw()

    def check_game_over(self):
        if self.board.all_off():
            result = askyesno("You win!", "Would you like to play again?")
            if result:
                self.board.initialize_lights()
                self.draw()
            else:
                self.master.destroy()

    def handle_click(self):
        self.draw()
        self.check_game_over()


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Lights Out!")
    window.resizable(False, False)
    window.configure(padx=10, pady=10)
    board = Board(5)
    light_frame = LightBoard(window, board)
    light_frame.pack()

    window.mainloop()
