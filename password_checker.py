username = input("enter your username:")
password = input("enter your password:")

password_length = len(password)
hidden_password = '*' * password_length

print(f'your password {hidden_password} is{password_length} letters long')
