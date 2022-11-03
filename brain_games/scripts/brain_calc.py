#!/usr/bin/env python3

"""Brain Calc Game"""

from brain_games.general_logic import play
from brain_games.games import calc


def main():
    """Start to play Calc Game"""
    play(calc)


if __name__ == '__main__':
    main()
