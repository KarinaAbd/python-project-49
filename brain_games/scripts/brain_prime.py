#!/usr/bin/env python3

"""Brain Prime Game"""

from brain_games.game_engine import play
from brain_games.games import prime


def main():
    """Start to play Prime Game"""
    play(prime)


if __name__ == '__main__':
    main()
