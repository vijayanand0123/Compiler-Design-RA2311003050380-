# Semantic Analyzer for simple arithmetic expressions

# Symbol Table to store declared variables
symbol_table = {}

# Function to declare a variable
def declare(var, value):
    symbol_table[var] = value

# Function to check semantic correctness
def semantic_check(expr):
    tokens = expr.split()  # Simple split by space for simplicity
    for token in tokens:
        if token.isalpha():  # variable
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

# ===== MAIN =====

# Declare some variables
declare('a', 10)
declare('b', 5)

# Take first expression from user
expr1 = input("Enter first expression (use declared variables a,b): ")
if semantic_check(expr1):
    print("Expression 1: Semantic OK ✅")
else:
    print("Expression 1: Semantic Error ❌")

# Take second expression from user
expr2 = input("Enter second expression (use declared variables a,b): ")
if semantic_check(expr2):
    print("Expression 2: Semantic OK ✅")
else:
    print("Expression 2: Semantic Error ❌")
