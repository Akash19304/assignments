from collections import Counter
import re

def count_word_occurrences(file_path: str) -> dict:
    """
    Reads the specified file, counts occurrences of each word, and returns a dictionary
    with words as keys and their counts as values.

    Parameters:
    file_path (str): The path of the file to read from.

    Returns:
    dict: A dictionary where keys are words and values are the number of occurrences.
    """
    word_count = Counter()

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = re.findall(r'\b\w+\b', content.lower())
            word_count.update(words)
    
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except IOError:
        print(f"An error occurred while trying to read the file '{file_path}'.")

    return word_count


def display_word_counts(word_count: dict) -> None:
    """
    Displays the word counts in alphabetical order.

    Parameters:
    word_count (dict): A dictionary where keys are words and values are the number of occurrences.
    """
    for word in sorted(word_count):
        print(f"{word}: {word_count[word]}")


file_path = "paragraph.txt"

word_count = count_word_occurrences(file_path)

display_word_counts(word_count)
