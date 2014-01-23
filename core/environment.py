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
an environment is made up of a series of variables assigned to values, with a field outer, referring to 
the super environment that the current environment belongs to. In the example above, the environment corresponding to
the function square has a super environment global. These are how environments work, and why they are intrinsically 
important.

For us though, in writing the Scheme interpreter, all we really care about is finding the correct instance of 
a variable. Let's look at another example:

(define make-account
	(lambda (balance) 
		(lambda (amt)
			(begin (set! balance (+ balance amt)) balance))))

(define account_1 (make-account 10))
(account_1 -2)

There are three environments in the above code, the global environment where make-account is defined, the balance 
environment, and the amt environment. In the last line of code, where (account_1 -2) is called, the first code that is 
executed is the (set! ...) code, where balance is set to the new balance. However, balance only exists in the super amt super
environment (this is to prevent reference/call issues). So in the execution of the code, we need to look for balance in the super
environment, and then change it there, which is how we will define the Environment class find function.

You get the idea.
"""

__author__ = "Sidd Karamcheti"

class Environment(dict):
	"""
	An environment frame, comprised of a dictionary of variables mapped to values
	"""
	def __init__(self, params = (), args = (), outer_environment = None):
		self.update(zip(params, args))
		self.outer = outer

	def find(self, var):
		"""
		Finds the first environment in which var appears
		"""
		
