"""
env.py

In Scheme, each variable reference is independent to a specific enviroment. For example, 
given the following trivial example:

(begin (define x 3)
	(define (square x)
		(* x x)))
	(square x))

Here, x is defined twice, once in the global environment, and one in the environment of the
defined function, square. To prevent assignment and reference errors, a new environment must be
created, and each variable must be allocated to its own environment.

As such, the class Environment is created in the following manner: with a dictionary superclass,
an Environment is made up of a series of variables assigned to values, with a field outer, referring to 
the super Environment that the current Environment belongs to. In the example above, the Environment corresponding to
the function square has a super Environment global.

You get the idea.
"""

__author__ = "Sidd Karamcheti"

