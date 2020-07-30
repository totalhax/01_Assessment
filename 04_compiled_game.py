from tkinter import *
from functools import partial
import random


class Start:

    def __init__(self, partner):

        # operation variable (string variable)
        self.operation = StringVar()

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
        self.var.set = 0

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
                                 width=12, height=2, command=lambda: self.check_start_ans("+", self.var.get(),
                                                                                          self.start_amount_entry.get()))
        self.add_button.grid(row=0, column=0)

        self.sub_button = Button(self.game_choice_frame, font=font, text="Subtraction",
                                 width=12, height=2, command=lambda: self.check_start_ans("-", self.var.get(),
                                                                                          self.start_amount_entry.get()))
        self.sub_button.grid(row=0, column=1)

        self.mul_button = Button(self.game_choice_frame, font=font, text="Multiplication",
                                 width=12, height=2, command=lambda: self.check_start_ans("*", self.var.get(),
                                                                                          self.start_amount_entry.get()))
        self.mul_button.grid(row=1, column=0)

        self.div_button = Button(self.game_choice_frame, font=font, text="Division",
                                 width=12, height=2, command=lambda: self.check_start_ans("/", self.var.get(),
                                                                                          self.start_amount_entry.get()))
        self.div_button.grid(row=1, column=1)

        # stats and quit button are below game_choice_frame
        self.stats_button = Button(self.game_choice_frame, font=font_bold, text="Help & History",
                                   width=12, height=2, bg="Blue", fg="White")
        self.stats_button.grid(row=5, column=0, pady=20)

        self.quit_button = Button(self.game_choice_frame, font=font_bold, text="Quit",
                                  width=12, height=2, command=self.to_quit, bg="Red", fg="White")
        self.quit_button.grid(row=5, column=1, pady=20)

    def check_start_ans(self, operation, diff, question_number):
        # checks answer and configures buttons based on whether or not the answer was correct
        try:
            diff_choice = self.var.get()
            diff_choice = int(diff_choice)

            num_quest = self.start_amount_entry.get()
            num_quest = int(num_quest)

            if num_quest == "":
                self.how_many_questions.config(text="Please choose an amount of questions", fg="red")
            elif diff_choice == 0:
                self.how_many_questions.config(text="Please select a difficulty", fg="red")
            else:
                self.to_add(operation, diff, question_number)

        except ValueError:
            self.how_many_questions.config(text="Please choose an amount of questions", fg="red")

    def to_add(self, operation, diff, question_number):
        # self.operation.set("+")
        print(operation)
        print(diff)
        Game(self, operation, diff, question_number)

    def to_quit(self):
        root.destroy()


class Game:

    def __init__(self, partner, operation, diff, question_number):

        self.game_frame = Frame(padx=25, pady=10)
        self.game_frame.grid()

        # true_answer variable (integer)
        self.true_answer = IntVar()
        self.true_answer.set(0)

        self.amount_questions = IntVar()
        self.amount_questions.set(question_number)

        self.num_questions = IntVar()
        self.num_questions.set(0)

        self.var_operation = StringVar()
        self.var_operation.set(operation)

        self.difficulty = IntVar()
        self.difficulty.set(diff)

        self.game_frame = Toplevel()

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
        quest = self.amount_questions.get()
        how_many = self.num_questions.get()
        self.next_button.config(state=DISABLED, text="Next", bg="SystemButtonFace")
        op = self.var_operation.get()
        # if we have 10 questions, end game
        if how_many == quest-1:
            self.next_button.config(text="Finish", bg="#abff94")
        elif how_many >= quest:
            self.next_button.config(command=self.close_game())

        how_many += 1
        self.num_questions.set(how_many)
        self.count_label.config(text="Question {}".format(how_many))

        # generates question

        self.info_label.config(text="\n")
        self.submit_button.config(bg="SystemButtonFace")
        self.submit_button.config(state=NORMAL)

        if diff == 1:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        elif diff == 2:
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
    something = Start(root)
    root.resizable(False, False)
    root.mainloop()
