import random

op = "*"

for item in range(1, 5):
    # make question
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)

    question = "{} {} {}".format(num1, op, num2)
    correct = eval(question)

    ask = int(input("{} = ".format(question)))
    if ask == correct:
        print("great job")
    else:
        print("oops")