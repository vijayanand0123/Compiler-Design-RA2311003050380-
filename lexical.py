keywords = ["int", "float", "if", "else", "for", "while", "return"]

operators = ["+", "-", "*", "/", "=", ">", "<"]

symbols = ["(", ")", "{", "}", ";"]

code = input("Enter your program code:\n")

tokens = []   

for sym in symbols:
    code = code.replace(sym, f" {sym} ")

for op in operators:
    code = code.replace(op, f" {op} ")

words = code.split()

for word in words:
    if word in keywords:
        tokens.append(("KEYWORD", word))

    elif word in operators:
        tokens.append(("OPERATOR", word))

    elif word in symbols:
        tokens.append(("SYMBOL", word))

    elif word.isdigit():
        tokens.append(("NUMBER", word))

    elif word.isidentifier():
        tokens.append(("IDENTIFIER", word))

    else:
        tokens.append(("UNKNOWN", word))
print("\nTokens:")
for t in tokens:
    print(t)
