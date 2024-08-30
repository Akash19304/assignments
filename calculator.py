# calculator.py

def add(a, b):
    """
    Returns the sum of a and b.
    
    :param a: First number
    :param b: Second number
    :return: Sum of a and b
    """
    return a + b

def subtract(a, b):
    """
    Returns the difference of b subtracted from a.
    
    :param a: First number
    :param b: Second number
    :return: Difference of a and b
    """
    return a - b

def multiply(a, b):
    """
    Returns the product of a and b.
    
    :param a: First number
    :param b: Second number
    :return: Product of a and b
    """
    return a * b

def divide(a, b):
    """
    Returns the division of a by b. Raises a ValueError if b is zero.
    
    :param a: First number
    :param b: Second number
    :return: Result of a divided by b
    :raises ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
