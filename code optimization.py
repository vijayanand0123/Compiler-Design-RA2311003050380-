def optimize_code(lines):
    optimized = []
    expr_table = {}

    for line in lines:
        parts = line.split("=")

        if len(parts) != 2:
            continue

        left = parts[0].strip()
        right = parts[1].strip()

        try:
            value = eval(right)
            right = str(value)
        except:
            pass

        if right in expr_table:
            optimized.append(f"{left} = {expr_table[right]}")
        else:
            expr_table[right] = left
            optimized.append(f"{left} = {right}")

    return optimized

print("Enter intermediate code line by line (type END to stop):")

code_lines = []
while True:
    line = input()
    if line == "END":
        break
    code_lines.append(line)

result = optimize_code(code_lines)

print("\nOptimized Code:")
for line in result:
    print(line)