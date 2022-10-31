import random


RULE = 'What is the result of the expression?'


def get_expression():
    num1 = random.randint(0, 20)
    num2 = random.randint(0, 20)

    operator = ['+', '-', '*']
    op = random.choice(operator)

    """Assemble the expression from random numbers and operator"""
    expression = f'{num1} {op} {num2}'
    return expression


def get_answer(expression):
    """Calculating the expression"""
    return str(eval(expression))


def get_content():
    question = get_expression()
    cor_answer = get_answer(question)
    return [question, cor_answer]
