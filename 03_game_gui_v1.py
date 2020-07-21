from tkinter import *
from functools import partial
import random


class Game:

    def __init__(self, parent):

        self.game_frame = Frame(padx=10, pady=10)
        self.game_frame.grid()

        self.how_many_questions = Label(self.game_frame, text="1 + 2 = ", font="Arial 20")
        self.how_many_questions.grid(row=0)

        self.start_amount_entry = Entry(self.game_frame,
                                        font="Arial  19 bold", width=13)
        self.start_amount_entry.grid(row=1, column=0)

        self.button_frame = Frame(self.game_frame, width=200)
        self.button_frame.grid(row=2)

        self.add_button = Button(self.button_frame, text="Submit",
                                 width=12, height=2)
        self.add_button.grid(row=0, column=0)

        self.add_button = Button(self.button_frame, text="Next",
                                 width=12, height=2)
        self.add_button.grid(row=0, column=1)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Game")
    something = Game(root)
    root.resizable(False, False)
    root.mainloop()
