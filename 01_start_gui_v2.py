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
        font_bold = "Arial 10 bold"

        # radio buttons to choose the difficulty of the questions, the difficulty is the scale of the numbers used
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

        # four buttons to choose which type of questions you would like
        self.game_choice_frame = Frame(padx=10, pady=10)
        self.game_choice_frame.grid(row=4)

        self.add_button = Button(self.game_choice_frame, font=font, text="Addition",
                                 width=12, height=2)
        self.add_button.grid(row=0, column=0)

        self.sub_button = Button(self.game_choice_frame, font=font, text="Subtraction",
                                 width=12, height=2)
        self.sub_button.grid(row=0, column=1)

        self.mul_button = Button(self.game_choice_frame, font=font, text="Multiplication",
                                 width=12, height=2)
        self.mul_button.grid(row=1, column=0)

        self.div_button = Button(self.game_choice_frame, font=font, text="Division",
                                 width=12, height=2)
        self.div_button.grid(row=1, column=1)

        # stats and quit button are below game_choice_frame
        self.stats_button = Button(self.game_choice_frame, font=font_bold, text="Help & History",
                                   width=12, height=2, bg="Blue", fg="White")
        self.stats_button.grid(row=5, column=0, pady=20)

        self.quit_button = Button(self.game_choice_frame, font=font_bold, text="Quit",
                                  width=12, height=2, command=self.to_quit, bg="Red", fg="White")
        self.quit_button.grid(row=5, column=1, pady=20)

    def to_quit(self):
        root.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Game")
    something = Start(root)
    root.resizable(False, False)
    root.mainloop()
