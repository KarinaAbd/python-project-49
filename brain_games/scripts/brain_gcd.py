#!/usr/bin/env python3

"""Brain Greatest Common Divisor (GCD) Game"""

from brain_games.game_engine import play
from brain_games.games import gcd


def main():
    """Start to play GCD Game"""
    play(gcd)


if __name__ == '__main__':
    main()
