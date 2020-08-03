from tkinter import *
from functools import partial
import random


class Start:

    def __init__(self, partner):
        # defining history list used to store game history
        self.history = []

        # operation variable (string variable)
        self.operation = StringVar()

        # sets up the amount of questions box and label
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
                                   width=12, height=2, bg="Blue", fg="White", command=lambda: self.to_stats(self.history))
        self.stats_button.grid(row=5, column=0, pady=20)

        self.quit_button = Button(self.game_choice_frame, font=font_bold, text="Quit",
                                  width=12, height=2, command=self.to_quit, bg="Red", fg="White")
        self.quit_button.grid(row=5, column=1, pady=20)

    def check_start_ans(self, operation, diff, question_number):
        # checks answer and configures buttons based on whether or not the answer was correct
        try:
            # retrieves difficulty
            diff_choice = self.var.get()
            diff_choice = int(diff_choice)

            # retrieves the amount of questions
            num_quest = self.start_amount_entry.get()
            num_quest = int(num_quest)

            # checking if either difficulty or amount of questions is blank and throwing an error
            if num_quest == "":
                self.how_many_questions.config(text="Please choose an amount of questions", fg="red")
            elif diff_choice == 0:
                self.how_many_questions.config(text="Please select a difficulty", fg="red")
            else:
                self.to_add(operation, diff, question_number)

        except ValueError:
            self.how_many_questions.config(text="Please choose an amount of questions", fg="red")

    # function to go to the game function and take the difficulty and amount of questions with it
    def to_add(self, operation, diff, question_number):
        self.add_button.config(state=DISABLED)
        self.sub_button.config(state=DISABLED)
        self.mul_button.config(state=DISABLED)
        self.div_button.config(state=DISABLED)
        # self.operation.set("+")
        Game(self, operation, diff, question_number)

    # function to take history to gamestats class
    def to_stats(self, history):
        GameStats(self, history)

    # function to quit program entirely
    def to_quit(self):
        root.destroy()


class Game:

    def __init__(self, partner, operation, diff, question_number):

        # lists for history taken from start class using partner and question answer for sending information back
        partner.history = []
        self.quest_ans = []

        self.game_frame = Frame(padx=25, pady=10)
        self.game_frame.grid()

        # true_answer variable (integer)
        self.true_answer = IntVar()
        self.true_answer.set(0)

        # amount_questions variable (integer)
        self.amount_questions = IntVar()
        self.amount_questions.set(question_number)

        # num_questions variable (integer)
        self.num_questions = IntVar()
        self.num_questions.set(0)

        # var_operation variable (string)
        self.var_operation = StringVar()
        self.var_operation.set(operation)

        # difficulty variable (integer)
        self.difficulty = IntVar()
        self.difficulty.set(diff)

        self.game_frame = Toplevel()

        # question starts as "press start" and will be change to show the current question later
        question = "Press Start"

        # game box labels and entry box for answer
        self.question_label = Label(self.game_frame, text=question, font="Arial 20")
        self.question_label.grid(row=1)

        self.info_label = Label(self.game_frame, text="\n", font="Arial 10 italic")
        self.info_label.grid(row=2)

        self.answer_entry = Entry(self.game_frame,
                                  font="Arial  19 bold", width=13)
        self.answer_entry.grid(row=3, column=0)

        # submit and next button code with a question count at the bottom
        self.button_frame = Frame(self.game_frame, width=200)
        self.button_frame.grid(row=4)

        self.submit_button = Button(self.button_frame, text="Submit",
                                    width=12, height=2, command=partial(self.check_ans, partner))
        self.submit_button.grid(row=0, column=0)

        self.submit_button.config(state=DISABLED)

        self.next_button = Button(self.button_frame, text="Start",
                                  width=12, height=2, command=partial(self.ask_question, partner), bg="#abff94")
        self.next_button.grid(row=0, column=1)

        # question number
        self.count_label = Label(self.game_frame, text="Question 0")
        self.count_label.grid(row=5)

        self.game_frame.protocol('WM_DELETE_WINDOW', partial(self.close_game,
                                                             partner))

    # function to ask question
    def ask_question(self, partner):
        # retrieves difficulty, amount_questions and num_questions
        diff = self.difficulty.get()
        quest = self.amount_questions.get()
        how_many = self.num_questions.get()
        # disables next button
        self.next_button.config(state=DISABLED, text="Next", bg="SystemButtonFace")
        op = self.var_operation.get()
        # if we have reached end of questions, change button to finish and end game
        if how_many == quest-1:
            self.next_button.config(text="Finish", bg="#abff94")
            self.next_button.config(command=partial(self.close_game, partner))

        # sets question number label and increases it by 1
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

        # evaluates question and sets the answer to answer
        answer = int(eval(question))

        self.question_label.config(text=question)

        self.true_answer.set(answer)

        # places question and correct answer to the question into the quest_ans list
        self.quest_ans.append(question)
        self.quest_ans.append(answer)

    # close game box function
    def close_game(self, partner):
        # Put buttons back to normal...
        partner.add_button.config(state=NORMAL)
        partner.mul_button.config(state=NORMAL)
        partner.sub_button.config(state=NORMAL)
        partner.div_button.config(state=NORMAL)
        self.game_frame.destroy()

    # check answer function
    def check_ans(self, partner):
        # checks answer and configures buttons based on whether or not the answer was correct
        try:
            true_answer = self.true_answer.get()
            true_answer = int(true_answer)

            user_input = self.answer_entry.get()
            user_input = int(user_input)

            self.quest_ans.append(user_input)
            partner.history.append(self.quest_ans)
            self.quest_ans = []

            # if answer is correct make button background green and say correct
            if user_input == true_answer:
                self.info_label.config(text="\nCorrect!", fg="green")
                self.submit_button.config(bg="#abff94")
            # if answer is incorrect make button background red and say incorrect and shows correct answer
            else:
                self.info_label.config(text="Incorrect!\n"
                                            "The correct answer was {}".format(true_answer), fg="red")
                self.submit_button.config(bg="#ff9f94")

            # Disables submit button, enables next button and clears out entry box
            self.submit_button.config(state=DISABLED)
            self.next_button.config(state=NORMAL)
            self.answer_entry.delete(0, 'end')

        except ValueError:
            # if no answer was given turn button background yellow and says to enter a number
            self.info_label.config(text="Please enter\n"
                                        "a number", fg="black")
            self.submit_button.config(bg="#fffd94")
            self.answer_entry.delete(0, 'end')


class GameStats:
    def __init__(self, partner, history):

        all_game_stats = [
            0, 3
        ]

        # disables buttons
        partner.stats_button.config(state=DISABLED)
        partner.add_button.config(state=DISABLED)
        partner.sub_button.config(state=DISABLED)
        partner.mul_button.config(state=DISABLED)
        partner.div_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.stats_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button

        self.stats_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats,
                                                            partner))

        # Set up GUI Frame
        self.stats_frame = Frame(self.stats_box)
        self.stats_frame.grid()

        # Set up Help heading (row 0)
        self.help_heading_label = Label(self.stats_frame, text="Help",
                                         font="arial 19 bold")
        self.help_heading_label.grid(row=0)

        # To Export <instructions> (row 1)
        self.export_instructions = Label(self.stats_frame,
                                         text="Select the amount of questions "
                                              "that you would like from the "
                                              "menu and choose a difficulty. "
                                              "Finally select an operation "
                                              "and the you will be given questions "
                                              "fitting your choices. "
                                              "Bellow you are able to export your "
                                              "history to a text file.", wrap=250,
                                         font="arial 10 italic",
                                         justify=LEFT, fg="green",
                                         padx=10, pady=10)
        self.export_instructions.grid(row=1)

        # Starting Balance (row 2)
        self.details_frame = Frame(self.stats_frame)
        self.details_frame.grid(row=2)

        # Dismiss Button (row 3)
        self.export_dismiss_frame = Frame(self.stats_frame)
        self.export_dismiss_frame.grid(row=3)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export...",
                                    command=partial(self.export, history))
        self.export_button.grid(row=0, column=0, padx=5)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=0, column=1, pady=10)

    def close_stats(self, partner):
        # Put buttons back to normal...
        partner.stats_button.config(state=NORMAL)
        partner.add_button.config(state=NORMAL)
        partner.sub_button.config(state=NORMAL)
        partner.mul_button.config(state=NORMAL)
        partner.div_button.config(state=NORMAL)
        self.stats_box.destroy()

    def export(self, history):
        Export(self, history)


class Export:
    def __init__(self, partner, history):

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export,
                                                             partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, )
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / "
                                                         "Instructions",
                                 font="arial 14 bold")
        self.how_heading.grid(row=0)

        # Export Instructions (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the "
                                                         "box below and press the "
                                                         "Save button to save your "
                                                         "game history to a "
                                                         "text file.",
                                 justify=LEFT, width=40, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename you "
                                                         "enter below already "
                                                         "exists, its contents "
                                                         "will be replaced with "
                                                         "your game history",
                                 justify=LEFT, bg="#ffafaf", fg="maroon",
                                 font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon")
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="Arial 15 bold", bg="#003366", fg="white",
                                  command=partial(
                                      lambda: self.save_history(partner, history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    font="Arial 15 bold", bg="#660000", fg="white",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, game_history):

        # Regular expression to check filname is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()
        # checks filename for errors
        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break
        # checks if filename is blank
        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # If there are no errors, generate text file and then close dialogue
            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # Heading for Game History
            f.write("Game History\n\n")

            # checks if answer was correct then prints it into text file
            for item in game_history:
                if item[1] == item[2]:
                    result = "correct"
                else:
                    result = "incorrect"

                line = "{} = {}, user answer {}, {}".format(item[0], item[1], item[2], result)
                f.write(line + "\n")

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Game")
    something = Start(root)
    root.resizable(False, False)
    root.mainloop()
