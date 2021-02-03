"""
The implementation of Fibonacci Sequence in Python.
Fibonacci Sequence - https://www.mathsisfun.com/numbers/fibonacci-sequence.html
"""


def createSequence(n: int):
    """
    This function creates a sequence of Fibonacci numbers from 0th to nth term
        onwards or backwards

    Examples:
    >>> createSequence(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    >>> createSequence(-10)
    [0, 1, -1, 2, -3, 5, -8, 13, -21, 34, -55]
    """
    # create a nth Fibonacci number
    def fiboNum(n):
        if (n == 0) or (n == 1):
            return n
        else:
            return fiboNum(n - 2) + fiboNum(n - 1)

    # create a Fibonacci Sequence up to nth term
    try:
        if n >= 0:
            seq = [fiboNum(i) for i in range(n + 1)]
            return seq
        else:
            seq = [(-1) ** (i + 1) * fiboNum(i) for i in range(abs(n) + 1)]
            return seq
    except TypeError:
        print("The 'n' term must be an integer.")


def sumSequence(n: int):
    """
    This function calculates the sum of a n-term Fibonacci Sequence

    Examples:
    >>> sumSequence(10)
    143
    >>> sumSequence(-10)
    -33
    """
    try:
        seq = createSequence(n)
        return sum(seq)
    except TypeError:
        pass


def estimatePhi(n: int):
    """
    The function estimates the phi (golden ratio) from the ratio
        between the last and the second last Fibonacci numbers of
        a n-term Fibonacci Sequence, in absolute value

    The real value of phi equals to (1 + sqrt(5)) / 2

    Example:
    >>> estimatePhi(10)
    1.6176470588235294
    >>> estimatePhi(-10)
    1.6176470588235294
    """
    try:
        if (n < -1) or (n > 1):
            seq = createSequence(n)
            return abs(seq[-1] / seq[-2])
        else:
            print("The 'n' term must be lower than -1 or greater than 1.")
    except TypeError:
        pass

