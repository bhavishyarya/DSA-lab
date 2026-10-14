arr = [0] * 100
n = int(input("Enter number of elements: "))

print("Enter array elements:")
for i in range(n):
    arr[i] = int(input())

while True:
    print("\n--- ARRAY MENU ---")
    print("1. Insertion")
    print("2. Deletion")
    print("3. Print Array")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pos = int(input("Enter position: "))
        element = int(input("Enter element: "))

        if pos >= 1 and pos <= n + 1 and n < 100:
            for i in range(n, pos - 1, -1):
                arr[i] = arr[i - 1]

            arr[pos - 1] = element
            n += 1

            print("Element inserted successfully")
        else:
            print("Invalid position or array is full")

    elif choice == 2:
        pos = int(input("Enter position to delete: "))

        if pos >= 1 and pos <= n:
            for i in range(pos - 1, n - 1):
                arr[i] = arr[i + 1]

            n -= 1
            print("Element deleted successfully")
        else:
            print("Invalid position")

    elif choice == 3:
        if n == 0:
            print("Array is empty")
        else:
            print("Array elements:")
            for i in range(n):
                print(arr[i], end=" ")
            print()

    elif choice == 4:
        print("Program terminated")
        break

    else:
        print("Invalid choice")