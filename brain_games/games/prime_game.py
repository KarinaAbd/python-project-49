import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    """The first prime number is 2"""
    if number > 1:
        divisors = range(2, number + 1)
        for element in divisors:
            if number % element == 0 and element == number:
                return 'yes'
            elif number % element == 0 and element != number:
                return 'no'
            continue
    return 'no'


def get_content():
    question = random.randint(0, 50)
    correct_answer = is_prime(question)
    return [question, correct_answer]
