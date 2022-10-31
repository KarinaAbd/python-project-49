import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_answer(number):
    """The first prime number is 2"""
    if number > 1:

        """Collect a list of possible divisors from 1 to half of the number"""
        poss_divisors = [1]
        while poss_divisors[-1] != (number // 2):
            next_num = poss_divisors[-1] + 1
            poss_divisors.append(next_num)

        """Collect a list of real divisors of the number"""
        divisors = []
        for char in poss_divisors:
            if number % char == 0:
                divisors.append(char)
            else:
                continue
        """
        Check the length of the divisor list.
        A prime number should have only 1,
        because we have halved the list of possible divisors.
        """
        if len(divisors) == 1:
            return 'yes'
        return 'no'
    return 'no'


def get_content():
    question = random.randint(0, 50)
    cor_answer = get_answer(question)
    return [question, cor_answer]
