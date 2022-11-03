import random
import math

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number > 1:
        i = 0
        divisors = range(2, int(math.sqrt(number) + 1))
        for element in divisors:
            if number % element == 0:
                i += 1
        if i == 0:
            return True
        return False
    return False


def get_content():
    question = random.randint(0, 50)

    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
