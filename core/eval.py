"""
eval.py

The eval() function is this really cool, but under-used function built into the Python programming language.
Basically, eval() allows you to evaluate, or run Python code in a Python program. While this may seem redundant,
or just unnecessary, it provides control flow for the majority of the interpreter. It is in the eval function 
in which most of the logic for the interpreter is done.

The eval function takes two parameters, the expression to be evaluated, as well as the environment in which
the evaluation is done.

Here is the control flow in the eval function:
	1. First check is if the expression is a Symbol (variable) - In Python this just checks if the expression
	is a string. The symbol is then found in the environment, and returned.

	2. Second check is the constant check. If the expression is not a string, or it's not a list, than it's most
	likely a numerical constant.

	3. Third check is for the quote special form in Scheme. The interpreter supports functionality for both forms 
	of quote, "quote" and '.

	4. Fourth check is for the 
