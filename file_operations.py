def write_to_file(file_path: str, data: str) -> None:
    """
    Writes the given data to a file, overwriting the file if it already exists.

    Parameters:
    file_path (str): The path of the file to write to.
    data (str): The data to write to the file.
    """
    with open(file_path, 'w') as file:
        file.write(data)


def append_to_file(file_path: str, data: str) -> None:
    """
    Appends the given data to a file. If the file does not exist, it creates a new one.

    Parameters:
    file_path (str): The path of the file to append to.
    data (str): The data to append to the file.
    """
    with open(file_path, 'a') as file:
        file.write(data)


def read_from_file(file_path: str) -> str:
    """
    Reads the content of a file and returns it as a string.

    Parameters:
    file_path (str): The path of the file to read from.

    Returns:
    str: The content of the file.
    """
    with open(file_path, 'r') as file:
        return file.read()
