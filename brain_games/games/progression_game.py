import random

RULE = 'What number is missing in the progression?'


def get_progression():
    """Define the beginning of the progression"""
    first_number = random.randint(0, 10)
    progression = [first_number]

    """Define the length & the step of the progression"""
    progression_size = random.randint(5, 10)
    step = random.randint(3, 11)

    """Assemble the progression in the form of a list"""
    while len(progression) < progression_size:
        next_number = progression[-1] + step
        progression.append(next_number)

    return progression


def get_content():
    progression = get_progression()

    """Define the index of the symbol that'll be guessed"""
    last_index = len(progression) - 1
    random_index = random.randint(0, last_index)

    """Find and save the correct answer in string format"""
    answer = progression[random_index]
    correct_answer = str(answer)

    """Replace the number with .. and convert the list to a string"""
    progression[random_index] = '..'
    question = ' '.join(map(str, progression))

    return question, correct_answer
