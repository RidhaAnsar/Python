def set_union(A, B):
    return A.union(B)

def set_intersection(A, B):
    return A.intersection(B)

def set_difference(A, B):
    return A.difference(B)

def main():
    while True:
        print("1. Set Union")
        print("2. Set intersection")
        print("3 set Difference")
        print("4. Exit")

        ch=input("enter your choice:")
        if ch in ['1', '2', '3']:
            A = set(input("Enter elements of the set A: ").split())
            B = set(input("Enter elements of the set B: ").split())
        
        if ch == '1':
            result = set_union(A, B)
            print(result)

        elif ch == '2':
            result = set_intersection(A, B)
            print(result)
        elif ch == '3':
            result = set_difference(A, B)
            print(result)
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a number between 1 and 4.")
            
if __name__ == "__main__":
    main()