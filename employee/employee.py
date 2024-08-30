def write_employee_details(file_path: str, employees: list) -> None:
    """
    Writes the details of employees to a file.

    Parameters:
    file_path (str): The path of the file to write to.
    employees (list): A list of tuples, each containing the name, age, and salary of an employee.
    """
    with open(file_path, 'w') as file:
        for employee in employees:
            name, age, salary = employee
            file.write(f"Name: {name}, Age: {age}, Salary: ${salary}\n")



employees = [
    ("John Doe", 28, 50000),
    ("Jane Smith", 34, 65000),
    ("Emily Davis", 45, 80000),
    ("Michael Brown", 30, 55000)
]


file_path = "employees.txt"


write_employee_details(file_path, employees)

print(f"Employee details have been written to {file_path}")
