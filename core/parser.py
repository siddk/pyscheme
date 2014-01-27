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


def read(expression_tokens):
    """
    Takes a list of tokens, reads a scheme expression.
    """

    #Check if tokens are empty
    if len(expression_tokens) == 0:
        raise SyntaxError('unexpected EOF while parsing')

    #Pop off first token
    token = expression_tokens.pop(0)

    #Get full Scheme expression out of larger set
    if token is '(':
        expr = []

        #Recursively add all tokens belonging to a single expression to a list
        while expression_tokens[0] is not ')':
            expr.append(read(expression_tokens))

        #Remove ')'
        expression_tokens.pop(0)

        return expr

    #Check for unexpected parenthesis
    elif token is ')':
        raise SyntaxError('unexpected ) while parsing')

    #Get type of token
    else:
        return getType(token)




