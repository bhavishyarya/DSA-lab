dq = [0] * 5
front = -1
rear = -1
size = 5

while True:
    print("\n--- DEQUE MENU ---")
    print("1. Insert at Front")
    print("2. Insert at Rear")
    print("3. Delete from Front")
    print("4. Delete from Rear")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if rear == size - 1:
            print("Deque Overflow")
        else:
            element = int(input("Enter element: "))

            if front == -1:
                front = rear = 0
            else:
                for i in range(rear, front - 1, -1):
                    dq[i + 1] = dq[i]
                rear += 1

            dq[front] = element
            print("Inserted at front")

    elif choice == 2:
        if rear == size - 1:
            print("Deque Overflow")
        else:
            element = int(input("Enter element: "))

            if front == -1:
                front = rear = 0
            else:
                rear += 1

            dq[rear] = element
            print("Inserted at rear")

    elif choice == 3:
        if front == -1:
            print("Deque Underflow")
        else:
            print("Deleted:", dq[front])

            if front == rear:
                front = rear = -1
            else:
                front += 1

    elif choice == 4:
        if front == -1:
            print("Deque Underflow")
        else:
            print("Deleted:", dq[rear])

            if front == rear:
                front = rear = -1
            else:
                rear -= 1

    elif choice == 5:
        if front == -1:
            print("Deque is empty")
        else:
            for i in range(front, rear + 1):
                print(dq[i], end=" ")
            print()

    elif choice == 6:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
