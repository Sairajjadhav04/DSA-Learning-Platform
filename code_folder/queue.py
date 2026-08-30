class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [0] * size
        self.front = -1
        self.rear = -1
    # Check Empty
    def is_Empty(self):
        return self.front == -1
    # Check Full
    def is_Full(self):
        return self.rear == self.size - 1
    # Enqueue Operation
    def Enqueue(self, item):
        if self.is_Full():
            print("Queue Overflow!!")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = item
            print(f"{item} entered inside the Queue")
    # Dequeue Operation
    def Dequeue(self):
        if self.is_Empty():
            print("Queue Underflow!!")
        else:
            item = self.queue[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front += 1
            print(f"{item} Removed From the Queue")
    # Peek Operation
    def Peek(self):
        if self.is_Empty():
            print("Queue is Empty!!")
        else:
            print(f"Peek / Front element is {self.queue[self.front]}")
    # Display Operation
    def display(self):
        if self.is_Empty():
            print("Queue is empty, nothing to display!!")
        else:
            print("Queue elements are:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
# Main Function
size = int(input("Enter the size of Queue: "))
q = Queue(size)
while True:
    print("\n\tQueue ADT Operations\n")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    # Switch Case using match-case
    match choice:
        case 1:
            value = int(input("Enter element: "))
            q.Enqueue(value)
        case 2:
            q.Dequeue()
        case 3:
            q.Peek()
        case 4:
            q.display()
        case 5:
            print("Exiting Program...")
            break
        case _:
            print("Invalid choice! Enter a valid choice.")