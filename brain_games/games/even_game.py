import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_answer(number):
    even_num = 'yes'
    odd_num = 'no'
    if number % 2 == 0:
        return even_num
    else:
        return odd_num


def get_content():
    question = random.randint(0, 100)
    cor_answer = get_answer(question)
    return [question, cor_answer]
