def substring():
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")
    if str2 in str1:
        print("string2  is a substring of string1 ")
    else:
        print("string2  is not a substring of string1 ")

def occurrence_count():
    str1 = input("Enter string: ")
    occ = input("Enter character: ")
    count = str1.count(occ)
    print(count)

def replace_substring():
    str1 = input("Enter string 1: ")
    substr1 = input("Enter substring to replace: ")
    substr2 = input("Enter new substring: ")
    new_string = str1.replace(substr1, substr2)
    print(new_string)

def convert_to_capital():
    str1 = input("Enter the string: ")
    capitalized_string = str1.upper()
    print(capitalized_string)

# Menu loop
while True:
    print("\nString Operations Menu:")
    print("1. Check if substring")
    print("2. Count occurrences of character")
    print("3. Replace substring with another substring")
    print("4. Convert to capital letters")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        substring()
    elif choice == '2':
        occurrence_count()
    elif choice == '3':
        replace_substring()
    elif choice == '4':
        convert_to_capital()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
