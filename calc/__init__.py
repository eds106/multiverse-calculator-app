def add(start_number, operation_number):
    return start_number + operation_number


def subtract(start_number, operation_number):
    return start_number - operation_number


def multiply(start_number, operation_number):
    return start_number * operation_number


def divide(start_number, operation_number):
    return start_number / operation_number


def index(start_number, operation_number):
    result = start_number

    for i in range(operation_number):
        result = result * i

    return result


def alt_index(start_number, operation_number):
    return start_number**operation_number


def get_calculation(operation, start_number, operation_number):
    operator = "???"

    if operation == "add":
        operator = "+"

    elif operation == "subtract":
        operator = "-"

    elif operation == "multiply":
        operator = "*"

    elif operation == "divide":
        operator = "/"

    elif operation == "index":
        operator = "^"
        
    return f"{start_number}{operator}{operation_number}"

