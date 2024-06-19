n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
x = input("Enter operation to be performed ")

if x == '+':
    result = n1 + n2
elif x == '-':
    result = n1 - n2
elif x == '*':
    result = n1 * n2
elif x == '/':
    if n2 != 0:
        result = n1 / n2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"

print(result)
