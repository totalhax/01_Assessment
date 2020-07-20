from tkinter import *
from functools import partial
import random


class Start:
    def __init__(self, parent):
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.how_many_questions = Label(self.start_frame, text="How Many Questions?")
        self.how_many_questions.grid(row=1)

        self.entry_frame = Frame(self.start_frame, width=200)
        self.entry_frame.grid(row=2)

        self.start_amount_entry = Entry(self.entry_frame,
                                        font="Arial  19 bold", width=15)
        self.start_amount_entry.grid(row=0, column=0)

        font = "Arial 10"

        self.var = IntVar()

        self.difficulty_frame = Frame(padx=10, pady=10)
        self.difficulty_frame.grid(row=3)

        self.choice = Radiobutton(self.difficulty_frame, font=font, width=5, text="Easy",
                                  variable=self.var, value=1)
        self.choice.grid(row=0, column=0)

        self.choice2 = Radiobutton(self.difficulty_frame, font=font, width=5, text="Medium",
                                   variable=self.var, value=2)
        self.choice2.grid(row=0, column=1)

        self.choice3 = Radiobutton(self.difficulty_frame, font=font, width=5, text="Hard",
                                   variable=self.var, value=3)
        self.choice3.grid(row=0, column=2)

        self.game_choice_frame = Frame(padx=10, pady=10)
        self.game_choice_frame.grid(row=4)

        self.add_button = Button(self.game_choice_frame, font=font, text="Addition",
                                 width=10, height=2)
        self.add_button.grid(row=0, column=0)




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Game")
    something = Start(root)
    root.mainloop()
