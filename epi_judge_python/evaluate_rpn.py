from test_framework import generic_test


def evaluate(expression: str) -> int:
    stack = []
    operations = set(["+", "-", "*", "/"])
    elements = expression.split(",")
    for element in elements:
        if element not in operations:
            stack.append(int(element))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            result = None
            if element == "+":
               result = operand1 + operand2
            elif element == "-":
                result = operand1 - operand2
            elif element == "*":
                result = operand1 * operand2
            else:
                result = operand1 // operand2

            stack.append(result)

    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
