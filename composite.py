def is_composite(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

# User input
num = int(input("Enter a number: "))

if is_composite(num):
    print(f"{num} is a composite number")
else:
    print(f"{num} is not a composite number")
