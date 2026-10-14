queue = [0] * 5
front = -1
rear = -1
size = 5

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if rear == size - 1:
            print("Queue Overflow")
        else:
            element = int(input("Enter element: "))

            if front == -1:
                front = 0

            rear += 1
            queue[rear] = element
            print("Element inserted successfully")

    elif choice == 2:
        if front == -1 or front > rear:
            print("Queue Underflow")
        else:
            print("Deleted element:", queue[front])
            front += 1

            if front > rear:
                front = -1
                rear = -1

    elif choice == 3:
        if front == -1:
            print("Queue is empty")
        else:
            print("Front element:", queue[front])

    elif choice == 4:
        if front == -1:
            print("Queue is empty")
        else:
            print("Queue elements:")
            for i in range(front, rear + 1):
                print(queue[i], end=" ")
            print()

    elif choice == 5:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
