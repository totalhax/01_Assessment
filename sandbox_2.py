import random


complete_history = []
single_question = []

for item in range(1, 4):
    num1 = random.randrange(1, 12)
    num2 = random.randrange(1, 12)

    question = "{} + {}".format(num1, num2)
    answer = eval(question)

    user_ans = int(input(question))

    single_question.append(question)
    single_question.append(answer)
    single_question.append(user_ans)

    complete_history.append(single_question)
    single_question = []

print("complete history", complete_history)
print(complete_history)
print()

row = 0
for line in complete_history:
    print("Question", complete_history[row][0])
    print("Correct ans", complete_history[row][1])
    print("User ans", complete_history[row][2])
    print()


    row += 1