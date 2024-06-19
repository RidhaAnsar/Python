num = int(input("Enter the number: "))
rev = 0
n = num
while num != 0:
    val = num % 10
    rev = (rev * 10) + val
    num = int(num/10)

print("Reverse:", rev)
sum = rev + n
print("Sum of the numbers:", sum)
sum_rev = 0
temp = sum

while temp != 0:
    val = temp % 10
    sum_rev = (sum_rev * 10) + val
    temp = int(temp/10)

print("Reverse of sum:", sum_rev)

if sum_rev == sum:
    print("Sum is a palindrome")
else:
    print("Sum is not a palindrome")

