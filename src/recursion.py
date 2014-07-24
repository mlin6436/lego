def factorial(n):
    """
    The factorial function
    The factorial of a positive integer n, denoted n!, is defined as the product of the integers from 1 to n.
    If n = 0, then n! is defined as 1 by convention.
    :param n:
    :return:
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)