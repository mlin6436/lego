from binascii import Error


def basic_fibonacci(n):
    """
    O(2^n) way of implementing fibonacci number.
    :param n: The nth fibonacci number
    :return: The fibonacci number
    """
    if n < 0:
        raise Error('Invalid input')

    if n == 0 or n == 1:
        return 1
    else:
        return basic_fibonacci(n - 1) + basic_fibonacci(n - 2)


def improved_fibonacci(n):
    """
    O(n) way of implementing fibonacci number.
    :param n: The nth fibonacci number
    :return: The nth fibonacci number, the (n-1)th fibonacci number
    """
    if n < 0:
        raise Error('Invalid input')

    if n == 0:
        return 1, 0
    elif n == 1:
        return 1, 1
    else:
        (a, b) = improved_fibonacci(n - 1)
        return a + b, a