

import re

def check(expr):
    tokens = re.findall(r'\w+|[()+\-*/]', expr)
    pos = 0

    def error():
        raise Exception

    def peek():
        return tokens[pos] if pos < len(tokens) else None

    def advance():
        nonlocal pos
        pos += 1

    def F():
        if peek() == '(':
            advance()
            E()
            if peek() == ')':
                advance()
            else:
                error()
        elif peek() and peek().isalnum():
            advance()
        else:
            error()

    def T():
        F()
        while peek() in ('*', '/'):
            advance()
            F()

    def E():
        T()
        while peek() in ('+', '-'):
            advance()
            T()

    try:
        E()
        return pos == len(tokens)
    except:
        return False

expr1 = input("Enter first expression: ")
print("Output 1:", "Valid ✅" if check(expr1) else "Invalid ❌")

expr2 = input("Enter second expression: ")
print("Output 2:", "Valid ✅" if check(expr2) else "Invalid ❌")
