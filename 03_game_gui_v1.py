from tkinter import *
from functools import partial
import random


class Game:

    def __init__(self, parent):

        self.game_frame = Frame(padx=25, pady=10)
        self.game_frame.grid()

        # operation variable (string variable)
        self.operation = StringVar()
        self.operation.set("+")

        # difficulty variable (?string)
        self.difficulty = StringVar()
        self.difficulty.set("easy")

        # true_answer variable (integer)
        self.true_answer = IntVar()
        self.true_answer.set(0)

        self.num_questions = IntVar()
        self.num_questions.set(0)

        question = "Press Start"

        self.question_label = Label(self.game_frame, text=question, font="Arial 20")
        self.question_label.grid(row=1)

        self.info_label = Label(self.game_frame, text="\n", font="Arial 10 italic")
        self.info_label.grid(row=2)

        self.answer_entry = Entry(self.game_frame,
                                  font="Arial  19 bold", width=13)
        self.answer_entry.grid(row=3, column=0)

        self.button_frame = Frame(self.game_frame, width=200)
        self.button_frame.grid(row=4)

        self.submit_button = Button(self.button_frame, text="Submit",
                                    width=12, height=2, command=self.check_ans)
        self.submit_button.grid(row=0, column=0)

        self.submit_button.config(state=DISABLED)

        self.next_button = Button(self.button_frame, text="Start",
                                  width=12, height=2, command=self.ask_question, bg="#abff94")
        self.next_button.grid(row=0, column=1)

        self.count_label = Label(self.game_frame, text="Question 0")
        self.count_label.grid(row=5)

    def ask_question(self):

        diff = self.difficulty.get()

        how_many = self.num_questions.get()

        self.next_button.config(state=DISABLED, text="Next", bg="SystemButtonFace")

        # if we have 10 questions, end game
        if how_many == 9:
            self.next_button.config(text="Finish", bg="#abff94")
        elif how_many >= 10:
            self.next_button.config(command=self.close_game())

        how_many += 1
        self.num_questions.set(how_many)
        self.count_label.config(text="Question {}".format(how_many))

        # generates question
        op = self.operation.get()

        self.info_label.config(text="\n")
        self.submit_button.config(bg="SystemButtonFace")
        self.submit_button.config(state=NORMAL)

        if diff == "easy":
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        elif diff == "medium":
            num1 = random.randint(1, 25)
            num2 = random.randint(1, 25)
        else:
            num1 = random.randint(1, 40)
            num2 = random.randint(1, 40)

        num3 = num1 * num2

        if op == "/":
            question = "{} {} {}".format(num3, op, num1)
        else:
            question = "{} {} {}".format(num1, op, num2)

        answer = int(eval(question))

        print(eval(question))

        self.question_label.config(text=question)

        self.true_answer.set(answer)

    def check_ans(self):
        # checks answer and configures buttons based on whether or not the answer was correct
        try:
            true_answer = self.true_answer.get()
            true_answer = int(true_answer)

            user_input = self.answer_entry.get()
            user_input = int(user_input)

            if user_input == true_answer:
                self.info_label.config(text="\nCorrect!", fg="green")
                self.submit_button.config(bg="#abff94")
                self.submit_button.config(state=DISABLED)
                self.next_button.config(state=NORMAL)
                self.answer_entry.delete(0, 'end')

            else:
                self.info_label.config(text="Incorrect!\n"
                                            "The correct answer was {}".format(true_answer), fg="red")
                self.submit_button.config(bg="#ff9f94")
                self.submit_button.config(state=DISABLED)
                self.next_button.config(state=NORMAL)
                self.answer_entry.delete(0, 'end')

        except ValueError:
            self.info_label.config(text="Please enter\n"
                                   "a number", fg="black")
            self.submit_button.config(bg="#fffd94")
            self.answer_entry.delete(0, 'end')


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Game")
    something = Game(root)
    root.resizable(False, False)
    root.mainloop()
