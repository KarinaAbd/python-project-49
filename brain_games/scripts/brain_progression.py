#!/usr/bin/env python3

"""Brain Progression Game"""

from brain_games.game_engine import play
from brain_games.games import progression


def main():
    """Start to play Progression Game"""
    play(progression)


if __name__ == '__main__':
    main()
