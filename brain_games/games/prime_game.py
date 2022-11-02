import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    divisors = range(2, number + 1)
    for element in divisors:
        if number % element == 0 and element == number:
            return True
        elif number % element == 0 and element != number:
            return False
        continue
    return False


def get_content():
    question = random.randint(0, 50)

    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
