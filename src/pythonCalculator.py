from enum import Enum

class Operation(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4

def basicCalculator(operation, num1, num2):
    result = 0

    if operation == Operation.ADD:
        result = num1 + num2
    elif operation == Operation.SUBTRACT:
        result = num1 - num2
    elif operation == Operation.MULTIPLY:
        result = num1 * num2
    elif operation == Operation.DIVIDE:
        result = num1/num2
    else:
        print("Please enter valid operation)")
    return result


if __name__ == "__main__":
    print(basicCalculator(Operation.DIVIDE, 1, 2))

