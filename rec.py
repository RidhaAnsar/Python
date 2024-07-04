def print_pyramid(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print numbers in ascending order
        for k in range(1, i + 1):
            print(k, end="")
        # Print numbers in descending order
        for l in range(i - 1, 0, -1):
            print(l, end="")
        # Move to the next line
        print()

def main():
    try:
        rows = int(input("Enter the number of rows for the pyramid: "))
        if rows <= 0:
            print("Invalid input! Number of rows should be a positive integer.")
        else:
            print_pyramid(rows)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()

