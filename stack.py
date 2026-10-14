stack = [0] * 5
top = -1
size = 5

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if top == size - 1:
            print("Stack Overflow")
        else:
            element = int(input("Enter element: "))
            top += 1
            stack[top] = element
            print("Element pushed successfully")

    elif choice == 2:
        if top == -1:
            print("Stack Underflow")
        else:
            print("Deleted element:", stack[top])
            top -= 1

    elif choice == 3:
        if top == -1:
            print("Stack is empty")
        else:
            print("Top element:", stack[top])

    elif choice == 4:
        if top == -1:
            print("Stack is empty")
        else:
            print("Stack elements:")
            for i in range(top, -1, -1):
                print(stack[i])

    elif choice == 5:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
