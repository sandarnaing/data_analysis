# Perform simple arithmetic encoded in an input string:
# '1 + 2' -> 3, or '1 - 2' -> -1. hello
def compute(expression):
    num0, operator, num2 = expression.split(' ')
    num0, num2 = int(num0), int(num2)
    if operator == '+':
        return num0 + num2
    elif operator == '-':
        return num0 - num2
    elif operator == '*':
        return num0 * num2
    elif operator == '/':
        return num0 / num2
    else:
        print('unknown operator!')
        return None

    test123
