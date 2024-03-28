import math


def isOperator(expression: str) -> bool:
    return expression in [
        "+",
        "-",
        "*",
        "/",
        "^",
        "%",
        "l",
        "c",
        "s",
        "t",
        "g",
        "#",
        "!",
    ]


def getPrecedence(operator: str) -> int:
    precedence: dict[str, int] = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "%": 2,
        "^": 3,
        "l": 4,
        "c": 4,
        "s": 4,
        "t": 4,
        "g": 4,
        "#": 5,
        "!": 5,
    }
    return precedence.get(operator, 0)


def performOperation(operator: str, firstOperand: int, secondOperand: int = 0):

    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "^": lambda a, b: a**b,
        "%": lambda a, b: a % b,
        "l": lambda a, b: math.log(a),
        "c": lambda a, b: math.cos(a),
        "s": lambda a, b: math.sin(a),
        "t": lambda a, b: math.tan(a),
        "g": lambda a, b: 1 / math.tan(a),
        "#": lambda a, b: a * -1,
        "!": lambda a, b: math.factorial(a),
    }

    if operator not in operations:
        raise ValueError("Unknown operator")

    if operator in ["/", "l"] and secondOperand == 0:
        raise ValueError("Invalid operation")

    return operations[operator](firstOperand, secondOperand)
