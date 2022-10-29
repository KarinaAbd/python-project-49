import random
import prompt


def generate_num(level):
    if level == 1:
        return random.randint(0, 30)
    else:
        return random.randint(0, 100)


def ask(question):
    print(f'Question: {question}')


def get_answer():
    return prompt.string('Your answer: ')


def check_answer(user_answer, cor_answer):
    if user_answer == cor_answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{cor_answer}'.")
        return False


def finish(rounds, name):

    if rounds == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
