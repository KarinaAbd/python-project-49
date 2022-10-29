from brain_games.cli import welcome_user
from brain_games.games.main_logic import generate_num, ask
from brain_games.games.main_logic import get_answer, check_answer, finish


def play_even_game():
    print('Welcome to the Brain Games!')
    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i != 3:
        random_num = generate_num(2)
        ask(random_num)

        user_answer = get_answer()
        cor_answer = find_answer(random_num)

        if check_answer(user_answer, cor_answer):
            i += 1
        else:
            break

    finish(i, name)


def find_answer(random_num):
    even_num = 'yes'
    odd_num = 'no'
    if random_num % 2 == 0:
        return even_num
    else:
        return odd_num
