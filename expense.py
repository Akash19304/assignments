def calculate_total_expenses(file_path: str) -> float:
    """
    Reads the specified file and calculates the total amount spent on expenses.

    Parameters:
    file_path (str): The path of the file to read from.

    Returns:
    float: The total amount spent.
    """
    total_amount = 0.0
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(':')
                    if len(parts) == 2:
                        description, amount_str = parts
                        try:
                            amount = float(amount_str.strip())
                            total_amount += amount
                        except ValueError:
                            print(f"Warning: Could not convert '{amount_str}' to a float.")
    
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except IOError:
        print(f"An error occurred while trying to read the file '{file_path}'.")
    
    return total_amount


file_path = "expenses.txt"

total_expenses = calculate_total_expenses(file_path)
print(f"Total amount spent: ${total_expenses:.2f}")
