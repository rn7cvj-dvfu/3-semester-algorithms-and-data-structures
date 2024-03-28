from converter import infixToPostfix
from evaluator import evaluatePostfix


def main():

    infix_expression = "1 + 2 + 3 + 4"
    postfix_expression = infixToPostfix(infix_expression)

    print("Postfix Expression: ", postfix_expression)

    result = evaluatePostfix(postfix_expression)
    print("Result: ", result)


if __name__ == "__main__":
    main()
