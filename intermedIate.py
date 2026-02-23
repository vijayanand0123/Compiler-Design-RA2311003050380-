
temp_count = 1

def generate_TAC(expression):
    global temp_count
    
    operators = ['+', '-', '*', '/']
    tokens = expression.split()

    while len(tokens) > 3:
        for i in range(len(tokens)):
            if tokens[i] in operators:
                op = tokens[i]
                arg1 = tokens[i-1]
                arg2 = tokens[i+1]

                temp_var = f"t{temp_count}"
                temp_count += 1

                print(f"{temp_var} = {arg1} {op} {arg2}")

                tokens = tokens[:i-1] + [temp_var] + tokens[i+2:]
                break

    print(f"{tokens[0]} = {tokens[2]}")

expr = input("Enter expression (with spaces): ")
generate_TAC(expr)