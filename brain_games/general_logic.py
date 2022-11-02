"""General logic for all games"""

import prompt


def play(game):
    """Greet the player and ask his/her name"""

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.RULE)

    # rounds = 0
    ROUNDS_MAXIMUM = 3

    for round in range(0, ROUNDS_MAXIMUM):
        question, correct_answer = game.get_content()

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            round += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    else:
        print(f'Congratulations, {name}!')
