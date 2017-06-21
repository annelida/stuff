def square(x):
    """Return the square of x.

    >>> square(2)
    4
    >>> square(-2)
    4
    >>> square(2.0)
    4
    >>> square(-2.0)
    4
    >>> square(1j)
    (-1 + 0j)
    >>> square('2')
    TypeError
    """
    return x * x
