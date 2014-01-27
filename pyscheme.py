"""
pyscheme.py

Main file for the Scheme interpreter. Houses the main function, initializers,
and imports the Environment, Parse, and Eval functionality
"""

__author__ = "Sidd Karamcheti"

from core.environment import *
from core.eval import eval as evaluate
from core.parser import parse, toString


def repl(prompt='pyscheme>> '):
    """
    Live, interactive REPL for pyscheme.
    """
    while True:
        val = evaluate(parse(raw_input(prompt)))
        if val is not None:
            print toString(val)


if __name__ == "__main__":
    repl()
