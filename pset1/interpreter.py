expression = input("Expression: ").strip()

x,op,z = expression.split()

x = float(x)
z = float(z)

if op == "+":
    result = x + z
elif op == "-":
    result = x - z
elif op == "*":
    result = x * z
elif op == "/":
    result = x / z

print(result)
