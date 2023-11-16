def evaluate_reverse_polish_notation_150(tokens):
    def get_value(a, b, x):
        if x == "+":
            return a + b
        elif x == "-":
            return b - a
        elif x == "*":
            return a * b
        elif x == "/":
            return b / a

    real_stack = []
    visited = []
    operators = ("+", "-", "*", "/")
    n = len(tokens)
    for i in range(n - 1, -1, -1):
        real_stack.append(tokens[i])

    while real_stack:
        if real_stack[-1] not in operators:
            visited.append(round(int(real_stack.pop())))
        else:
            a = visited.pop()
            b = visited.pop()
            x = real_stack.pop()
            value = get_value(a, b, x)
            visited.append(round(int(value)))
    return value
