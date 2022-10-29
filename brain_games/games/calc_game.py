from brain_games.cli import welcome_user
from brain_games.games.main_logic import generate_num, ask
from brain_games.games.main_logic import get_answer, check_answer, finish
import random


def play_calc_game():
    print('Welcome to the Brain Games!')
    name = welcome_user()

    print('What is the result of the expression?')
    i = 0
    while i != 3:
        random_exp = get_expression()
        ask(random_exp)

        user_answer = get_answer()
        cor_answer = str(eval(random_exp))

        if check_answer(user_answer, cor_answer):
            i += 1
        else:
            break

    finish(i, name)


def get_expression():
    num1 = generate_num(1)
    num2 = generate_num(1)

    expression_1 = f'{num1} + {num2}'
    expression_2 = f'{num1} - {num2}'
    expression_3 = f'{num1} * {num2}'

    return random.choice([expression_1, expression_2, expression_3])
