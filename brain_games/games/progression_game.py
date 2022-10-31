import random


RULE = 'What number is missing in the progression?'


def get_progression():
    """Define the beginning of the progression"""
    first_num = random.randint(0, 10)
    progression = [first_num]

    """Define the length & the step of the progression"""
    len_of_progr = random.randint(5, 10)
    step = random.randint(3, 11)

    """Assemble the progression in the form of a list"""
    while len(progression) < len_of_progr:
        next_num = progression[-1] + step
        progression.append(next_num)

    return progression


def get_content():
    progression = get_progression()

    """Define the index of the symbol that'll be guessed"""
    last_index = len(progression) - 1
    random_index = random.randint(0, last_index)

    """Delete the symbol and save it in the correct answer"""
    answer = progression.pop(random_index)
    cor_answer = str(answer)

    """Replace the deleted character with .. and convert the list to a string"""
    progression.insert(random_index, '..')
    question = ''
    for elem in progression:
        question += f'{elem} '

    return [question, cor_answer]
