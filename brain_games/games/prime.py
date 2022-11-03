import random
import math

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number > 1:
        first_divisor = 2
        while first_divisor <= math.sqrt(number):
            if number % first_divisor == 0:
                return False
            first_divisor += 1
        return True


def get_content():
    question = random.randint(0, 50)

    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
