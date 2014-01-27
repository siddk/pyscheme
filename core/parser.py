"""
parser.py

Parses out Scheme expressions from input. Takes a string, tokenizes it, creates a sequential list of Scheme forms.
"""

__author__ = "Sidd Karamcheti"


def parse(scheme_expression):
    """
    Calls the read() function on the tokenized expression.
    """
    return read(tokenize(scheme_expression))

def tokenize(expression):
    """
    Inserts spaces between parentheses in a scheme expression, then splits the expression to keep track of
    all sub-expressions
    """
    expression = expression.replace('(', ' ( ')
    expression = expression.replace(')', ' ) ')

    return expression.split()
