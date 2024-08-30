# string_utils.py

def reverse_string(s: str) -> str:
    """
    Reverses the given string.

    Parameters:
    s (str): The string to reverse.

    Returns:
    str: The reversed string.
    """
    return s[::-1]


def capitalize_string(s: str) -> str:
    """
    Capitalizes the first letter of each word in the given string.

    Parameters:
    s (str): The string to capitalize.

    Returns:
    str: The capitalized string.
    """
    return s.title()


def to_uppercase(s: str) -> str:
    """
    Converts the entire string to uppercase.

    Parameters:
    s (str): The string to convert.

    Returns:
    str: The string in uppercase.
    """
    return s.upper()


def to_lowercase(s: str) -> str:
    """
    Converts the entire string to lowercase.

    Parameters:
    s (str): The string to convert.

    Returns:
    str: The string in lowercase.
    """
    return s.lower()


def is_palindrome(s: str) -> bool:
    """
    Checks if the given string is a palindrome.

    Parameters:
    s (str): The string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    cleaned_str = ''.join(e for e in s if e.isalnum()).lower()
    return cleaned_str == cleaned_str[::-1]


def count_vowels(s: str) -> int:
    """
    Counts the number of vowels in the given string.

    Parameters:
    s (str): The string to check.

    Returns:
    int: The number of vowels in the string.
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
