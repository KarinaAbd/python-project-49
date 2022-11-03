#!/usr/bin/env python3

"""Brain Even Game"""

from brain_games.game_engine import play
from brain_games.games import even


def main():
    """Start to play Even Game"""
    play(even)


if __name__ == '__main__':
    main()
