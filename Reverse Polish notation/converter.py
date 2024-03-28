from operators import isOperator, getPrecedence


def infixToPostfix(infix: str):
    postfix = ""
    operator_stack = []

    number = ""
    for c in infix:
        if c.isdigit():
            number += c
        else:
            if number:
                postfix += number + " "
                number = ""
            if c == "(":
                operator_stack.append(c)
            elif c == ")":
                while operator_stack and operator_stack[-1] != "(":
                    postfix += operator_stack.pop() + " "
                operator_stack.pop()

            elif isOperator(c):
                while operator_stack and getPrecedence(
                    operator_stack[-1]
                ) >= getPrecedence(c):
                    postfix += operator_stack.pop() + " "
                operator_stack.append(c)

            elif c == "!":
                postfix += "! "

            elif c != " ":
                raise ValueError("Invalid character in the expression")

    if number:
        postfix += number + " "

    while operator_stack:
        postfix += operator_stack.pop() + " "

    return postfix
