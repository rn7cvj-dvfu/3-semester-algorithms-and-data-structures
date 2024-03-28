from operators import isOperator, getPrecedence, performOperation


def evaluatePostfix(expression):
    operand_stack = []
    number = ""
    for c in expression:
        if c.isdigit():
            number += c
        elif c == " " and number:
            operand_stack.append(int(number))
            number = ""
        elif isOperator(c):
            if c in ["l", "c", "s", "t", "g", "#", "!"]:
                if not operand_stack:
                    raise ValueError("Invalid expression")
                operand = operand_stack.pop()
                result = performOperation(c, operand)
                operand_stack.append(result)
            else:
                if len(operand_stack) < 2:
                    raise ValueError("Invalid expression")
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = performOperation(c, operand1, operand2)
                operand_stack.append(result)

    if number:
        operand_stack.append(int(number))

    if len(operand_stack) != 1:
        raise ValueError("Invalid expression")

    return operand_stack.pop()
