import random
import math

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    divisors = range(2, int(math.sqrt(number) + 1))
    for element in divisors:
        if number % element == 0:
            return False
        elif number % element != 0:
            continue
    return True


def get_content():
    question = random.randint(0, 50)

    if question > 1 and is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
