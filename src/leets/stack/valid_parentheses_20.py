def valid_parentheses_20(s):
    stack = []
    pair = {")": "(", "}": "{", "]": "["}
    left = {"(", "[", "{"}
    for brac in s:
        if brac in left:
            stack.append(brac)
        else:
            if len(stack) > 0 and pair[brac] == stack[-1]:
                stack.pop()
            else:
                return False
    if len(stack) > 0:
        return False
    return True
