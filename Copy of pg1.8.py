
print("A. Find Factorial ")
print("B. Exit")
ch = input()
num = []
fact_li = []
while ch == "A":
    print("Enter a number ")
    n = int(input())
    fact=1
    for i in range(1,n+1):
        fact = fact * i
    num.append(n)
    fact_li.append(fact)
    
    print("A. Find Factorial ")
    print("B. Exit")
    ch = input()
fact_dict={}

for i in range(len(num)):
    fact_dict.update({num[i]:fact_li[i]})

print(fact_dict)