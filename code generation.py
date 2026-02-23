def generate_code(tac_lines):
    assembly = []

    for line in tac_lines:
        parts = line.split("=")

        if len(parts) != 2:
            continue

        left = parts[0].strip()
        right = parts[1].strip().split()

        if len(right) == 3:
            arg1 = right[0]
            op = right[1]
            arg2 = right[2]

            assembly.append(f"LOAD {arg1}")

            if op == '+':
                assembly.append(f"ADD {arg2}")
            elif op == '-':
                assembly.append(f"SUB {arg2}")
            elif op == '*':
                assembly.append(f"MUL {arg2}")
            elif op == '/':
                assembly.append(f"DIV {arg2}")

            assembly.append(f"STORE {left}")

        else:
            assembly.append(f"LOAD {right[0]}")
            assembly.append(f"STORE {left}")

    return assembly

print("Enter Three Address Code line by line (type END to stop):")

tac_code = []
while True:
    line = input()
    if line == "END":
        break
    tac_code.append(line)

result = generate_code(tac_code)

print("\nGenerated Assembly Code:")
for line in result:
    print(line)