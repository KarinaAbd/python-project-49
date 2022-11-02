"""General logic for all games"""

import prompt


def play(game):
    """Greet the player and ask his/her name"""

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.RULE)

    rounds = 0
    ROUNDS_MAXIMUM = 3

    while rounds < ROUNDS_MAXIMUM:
        """Take the question and the correct answer from the game module"""
        question, correct_answer = game.get_content()

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            rounds += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            break

    if rounds == ROUNDS_MAXIMUM:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
