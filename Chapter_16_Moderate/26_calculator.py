from queue import Queue
import unittest


def calculator(expression):
    '''
    16.26 Calculator: Given an arithmetic equation consisting of positive 
    integers, +, -, * and / (no parentheses), compute the result.

    EXAMPLE
    Input: 2*3+5/6*3+15
    Output: 23.5
    '''
    queue = _parse_expression(expression)

    stack = []
    a = queue.get()
    stack.append(a)

    while not queue.empty():
        op = queue.get()

        if op in '*/':
            a = stack.pop()
            b = queue.get()
            result = _calc(a, b, op)
            stack.append(result)
        else:
            # +, -
            if len(stack) > 1:
                _reduce(stack)

            stack.append(op)
            b = queue.get()
            stack.append(b)

    if len(stack) > 1:
        _reduce(stack)

    return stack.pop()


def _parse_expression(expression):
    op_indices = []

    for i in range(len(expression)):
        if expression[i] in '+-*/':
            op_indices.append(i)

    expr = Queue()
    cur_index = 0

    for op_index in op_indices:
        n = expression[cur_index:op_index]
        n = int(n)
        expr.put(n)
        expr.put(expression[op_index])

        cur_index = op_index + 1

    n = expression[cur_index:]
    n = int(n)
    expr.put(n)

    return expr


def _calc(a, b, op):
    if op == '+':
        return a + b

    if op == '-':
        return a - b

    if op == '*':
        return a * b

    if op == '/':
        return a / b

    raise ValueError(f'Invalid operation: {op}')


def _reduce(stack):
    b = stack.pop()
    op = stack.pop()
    a = stack.pop()
    result = _calc(a, b, op)
    stack.append(result)


class CalculatorTest(unittest.TestCase):
    def test_calculator(self):
        test_cases = [
            ('2*3+5/6*3+15', 23.5),
            ('1+2-3*4*5-6-7/8', -63.875)
        ]

        for expression, expected in test_cases:
            actual = calculator(expression)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
