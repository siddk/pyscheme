"""
pyscheme.py

Main file for the Scheme interpreter. Houses the main function, initializers, and imports the 
Environment, Parse, and Eval functionality
"""

__author__ = "Sidd Karamcheti"

from core.environment import *

if __name__ == "__main__":
    global_environment = global_init(Environment())
