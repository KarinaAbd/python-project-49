#!/usr/bin/env python3

"""Brain Progression Game"""

from brain_games.general_logic import play
from brain_games.games import progression_game


def main():
    """Start to play Progression Game"""
    play(progression_game)


if __name__ == '__main__':
    main()
