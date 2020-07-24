from tkinter import *
from functools import partial
import random


class Game:

    def __init__(self, parent):

        self.game_frame = Frame(padx=10, pady=10)
        self.game_frame.grid()

        # set up operation variable (string variable)

        # set up difficulty variable (?string)

        # true_answer variable (integer)
        self.true_answer = IntVar()
        self.true_answer.set(0)

        question = "? <press next>"

        self.question_label = Label(self.game_frame, text=question, font="Arial 20")
        self.question_label.grid(row=0)

        self.answer_entry = Entry(self.game_frame,
                                  font="Arial  19 bold", width=13)
        self.answer_entry.grid(row=1, column=0)

        self.button_frame = Frame(self.game_frame, width=200)
        self.button_frame.grid(row=2)

        self.submit_button = Button(self.button_frame, text="Submit",
                                    width=12, height=2, command=self.check_ans)
        self.submit_button.grid(row=0, column=0)

        self.next_button = Button(self.button_frame, text="Next",
                                  width=12, height=2, command=self.ask_question)
        self.next_button.grid(row=0, column=1)

    def ask_question(self):
        # generate question
        op = "+"

        self.submit_button.config(bg="SystemButtonFace")
        self.submit_button.config(state=NORMAL)

        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        num3 = num1 * num2

        if op == "/":
            question = "{} {} {}".format(num3, op, num1)
        else:
            question = "{} {} {}".format(num1, op, num2)

        answer = int(eval(question))

        print(eval(question))

        self.question_label.config(text=question)

        self.true_answer.set(answer)

        self.next_button.config(state=DISABLED)
        # set your true_answer variable

        # configure the label so that it is asked

    def check_ans(self):
        # retrieve true answer
        try:
            true_answer = self.true_answer.get()
            print("true answer", true_answer)
            true_answer = int(true_answer)

            user_input = self.answer_entry.get()
            user_input = int(user_input)

            if user_input == true_answer:
                print("correct")
                self.submit_button.config(bg="green")
                self.submit_button.config(state=DISABLED)
                self.next_button.config(state=NORMAL)

            else:
                print("wrong")
                self.submit_button.config(bg="red")
                self.submit_button.config(state=DISABLED)
                self.next_button.config(state=NORMAL)

        except ValueError:
            print("number please")
            self.submit_button.config(bg="red")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Game")
    something = Game(root)
    root.resizable(False, False)
    root.mainloop()
