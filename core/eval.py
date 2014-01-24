"""
eval.py

The eval() function is this really cool, but under-used function built into the Python programming language.
Basically, eval() allows you to evaluate, or run Python code in a Python program. While this may seem redundant,
or just unnecessary, it provides control flow for the majority of the interpreter. It is in the eval function 
in which most of the logic for the interpreter is done.

Here is the control flow in the eval function:
	1. Check is expression is a Symbol (variable) - In Python this just checks if the expression is a string

	2. Second check is the constant check. If the expression is not a string, or it's not a list, than it's most
	likely a numerical constant.

	3. 