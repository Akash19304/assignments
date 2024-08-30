
def display_file_contents(file_path: str) -> None:
    """
    Opens the specified file in read mode and displays its contents line by line.

    Parameters:
    file_path (str): The path of the file to read from.
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip()) 
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except IOError:
        print(f"An error occurred while trying to read the file '{file_path}'.")


file_path = "inventory.txt"

display_file_contents(file_path)
