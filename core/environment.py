"""
environment.py

In Scheme, each variable reference is independent to a specific enviroment.
For example, given the following trivial example:

(begin (define x 3)
    (define (square x)
        (* x x)))
    (square x))

Here, x is defined twice, once in the global environment, and one in
the environment of the defined function, square. To prevent assignment and
reference errors, a new environment must be created, and each variable must be
allocated to its own environment.

As such, the class Environment is created in the following manner: with a
dictionary superclass, an environment is made up of a series of variables
assigned to values, with a field outer, referring to the super environment
that the current environment belongs to. In the example above, the environment
corresponding to the function square has a super environment global. These are
how environments work, and why they are intrinsically important.

For us though, in writing the Scheme interpreter, all we really care about is
finding the correct instance of a variable. Let's look at another example:

(define make-account
    (lambda (balance)
        (lambda (amt)
            (begin (set! balance (+ balance amt)) balance))))

(define account_1 (make-account 10))
(account_1 -2)

There are three environments in the above code, the global environment where
make-account is defined, the balance environment, and the amt environment. In
the last line of code, where (account_1 -2) is called, the first code that is
executed is the (set! ...) code, where balance is set to the new balance.

However, balance only exists in the super amt super environment (this is to
prevent reference/call issues). So in the execution of the code, we need to
look for balance in the super environment, and then change it there, which is
how we will define the Environment class find function.

You get the idea.
"""

__author__ = "Sidd Karamcheti"

import math
import operator


class Environment(dict):
    """
    An environment frame, comprised of a dictionary of variables mapped
    to values
    """
    def __init__(self, params=(), args=(), outer_environment = None):
        self.update(zip(params, args))
        self.outer_env = outer_environment

    def find(self, var):
        """
        Finds the first environment in which var appears
        """
        if var in self.keys():
            #print "Found in self.keys"
            return self
        else:
            #Recursive call, base case not necessary because
            #at the global level, it will return null
            #print "Not in self"
            if self.outer_env:
                #print self.outer_env
                return self.outer_env.find(var)


def global_init(Env):
    """
    Initialize function for the global environment. Adds necessary Scheme
    functionality, and basic functions
    """
    Env.update(vars(math))
    Env.update(
        {'+': operator.add, '-': operator.sub, '*': operator.mul,
            '/': operator.div, 'not': operator.not_, '>': operator.gt,
            '<': operator.lt, '>=': operator.ge, '<=': operator.le,
            '=': operator.eq, 'equal?': operator.eq, 'eq?': operator.is_,
            'length': len, 'cons': lambda x, y: cons(x, y),
            'car': lambda x: x[0], 'cdr': lambda x: x[1:],
            'append': operator.add, 'list': lambda *x: list(x),
            'list?': lambda x: isinstance(x, list),
            'null?': lambda x: x is None,
            'symbol?': lambda x: isinstance(x, str)})
    return Env


def cons(x, y):
    """
    My quasi-cons function. Basically, the try block accounts for two of
    the most-used cons cases where y is a list, x is an item:
        1. cons(1, (2, 3)) returns [1, 2, 3]
        2. cons((1), (2, 3)) returns [[1], 2, 3]

    The except block accounts for the third cons case
        3. cons(1, 2) returns [1, 2]

    This isn't really (1 . 2), but it'll do for now
    """
    try:
        return [x] + y
    except:
        return [x] + [y]
