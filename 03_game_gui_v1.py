from tkinter import *
from functools import partial
import random


class Game:

    def __init__(self, parent):

        self.game_frame = Frame(padx=10, pady=10)
        self.game_frame.grid()

        op = "/"

        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        num3 = num1 * num2

        if op == "/":
            question = "{} {} {}".format(num3, op, num1)
        else:
            question = "{} {} {}".format(num1, op, num2)

        eval(question)

        print(eval(question))

        self.question = Label(self.game_frame, text=question, font="Arial 20")
        self.question.grid(row=0)

        self.answer_entry = Entry(self.game_frame,
                                  font="Arial  19 bold", width=13)
        self.answer_entry.grid(row=1, column=0)

        self.button_frame = Frame(self.game_frame, width=200)
        self.button_frame.grid(row=2)

        self.submit_button = Button(self.button_frame, text="Submit",
                                    width=12, height=2, command=self.check_ans)
        self.submit_button.grid(row=0, column=0)

        self.next_button = Button(self.button_frame, text="Next",
                                  width=12, height=2)
        self.next_button.grid(row=0, column=1)

    def check_ans(self):

        try:
            answer = int(self.answer_entry.get())
            if answer == eval(                                      ):
                print("correct")

            else:
                print("wrong")

        except ValueError:
            print("number please")




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Game")
    something = Game(root)
    root.resizable(False, False)
    root.mainloop()
