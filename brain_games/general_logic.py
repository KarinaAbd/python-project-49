"""General logic for all games"""

import prompt
from brain_games.cli import welcome_user


def play(game_name):
    """Greet the player and ask his/her name"""

    print('Welcome to the Brain Games!')
    name = welcome_user()

    print(game_name.RULE)

    """The game takes 3 rounds"""
    rounds = 0
    while rounds < 3:
        """Take the question and the correct answer from the game module"""
        [question, cor_answer] = game_name.get_content()

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == cor_answer:
            print('Correct!')
            rounds += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{cor_answer}'.")
            break

    if rounds == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
