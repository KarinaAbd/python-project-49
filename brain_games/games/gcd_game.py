import random
from math import gcd

RULE = 'Find the greatest common divisor of given numbers.'


def get_content():
    num1 = random.randint(0, 25)
    num2 = random.randint(25, 50)

    question = f'{num1} {num2}'
    cor_answer = str(gcd(num1, num2))
    return [question, cor_answer]
