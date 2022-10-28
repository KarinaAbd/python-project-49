import random
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    if play_even_game() == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")


def play_even_game():
    i = 0
    while i != 3:
        random_num = random.randint(0, 100)
        print(f'Question: {random_num}')
        answer = prompt.string('Your answer: ')

        if answer == check_answer(random_num):
            print('Correct!')
            i += 1

        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was'{check_answer(random_num)}'.")
            break
    return i


def check_answer(random_num):
    even_num = 'yes'
    odd_num = 'no'
    if random_num % 2 == 0:
        return even_num
    else:
        return odd_num
