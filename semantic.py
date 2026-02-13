
symbol_table = {}

def declare(var, value):
    symbol_table[var] = value

def semantic_check(expr):
    tokens = expr.split() 
    for token in tokens:
        if token.isalpha():  
            if token not in symbol_table:
                print(f"Semantic Error: Variable '{token}' not declared!")
                return False
        elif token.isdigit():
            continue
        elif token in ('+', '-', '*', '/'):
            continue
        else:
            print(f"Semantic Error: Unknown token '{token}'")
            return False
    return True


declare('a', 10)
declare('b', 5)

expr1 = input("Enter first expression (use declared variables a,b): ")
if semantic_check(expr1):
    print("Expression 1: Semantic OK ✅")
else:
    print("Expression 1: Semantic Error ❌")

expr2 = input("Enter second expression (use declared variables a,b): ")
if semantic_check(expr2):
    print("Expression 2: Semantic OK ✅")
else:
    print("Expression 2: Semantic Error ❌")


