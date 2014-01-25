"""
eval.py

The eval() function is this really cool, but under-used function built into
the Python programming language.

Basically, eval() allows you to evaluate, or run Python code in a Python
program. While this may seem redundant, or just unnecessary, it provides
control flow for the majority of the interpreter. It is in the eval function
in which most of the logic for the interpreter is done.

The eval function takes two parameters, the expression to be evaluated, as
well as the environment in which the evaluation is done.

Here is the control flow in the eval function:
    1. First check is if the expression is a Symbol (variable) - In Python
    this just checks if the expression is a string. The symbol is then found
    in the environment, and returned.

    2. Second check is the constant check. If the expression is not a string,
    or it's not a list, than it's most likely a numerical constant. Returns
    the constant value.

    3. Third check is for the quote special form in Scheme. The interpreter
    supports functionality for both forms of quote, "quote" and '. Returns the
    expression as it is.

    4. Fourth check is for the "if" special form. The expression is then
    tokenized, and separated into three parts: the conditional (test), and the
    conditional statements, consequence and alternative, respectively. The
    condition is then evaluated, and the resulting term is then run through
    the eval() function again.

    5. Fifth check is for the "set!" operator. Set! reassigns a variable or
    field to a different value. The expression is tokenized into two parts,
    the variable, and the expression it is being reset to. The variable is
    then found in the respective environment, and is then reassigned.

    6. Sixth check is for the "define" special form in Scheme. Define assigns
    a variable to a value, or a variable to an expression or function. The
    expression is tokenized into two parts, the variable and the expression.
    This key-value pair is then inserted into the environment.

    7. Seventh check is for the "lambda" special form. Lambda creates an
    in-line function or expression, and evaluates it. The expression is
    tokenized into two parts, the variables and the expression. A lambda is
    then created and returned in Python, with the variables assigned to
    arguments in a new eval() execution.

    8. Eighth check is for the "begin" special form. The expression is
    tokenized into whatever number of expressions, and each is then evaluated
    sequentially, by eval(). Resulting values are returned.

    9. Default check is the procedure check. Sequentially goes through typical
    Scheme left-to-right execution. Evaluates any expression.

The parser reads in and tokenizes a Scheme expression, eval() evaluates it.
Relatively straightforward.
"""

__author__ = "Sidd Karamcheti"

from core.environment import *

#Create global environment to pass to the eval() function
global_environment = global_init(Environment())


def eval(expression, env=global_environment):
    "Take an expression in a given environment, evaluate it"

    #Case 1
    if isinstance(expression, str):
        return env.find(expression)[expression]

    elif not isinstance(expression, list):
        return expression
