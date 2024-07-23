def pal(s):
    return s==s[::-1]
    
string="mommy"
if pal(string):
    print("palindrome")
else:
    print("not")
