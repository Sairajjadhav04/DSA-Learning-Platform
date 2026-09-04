import heapq
class PriorityQueue:
    def __init__(self):
        self.queue = []

    # Insert an element
    def enqueue(self, item):
        heapq.heappush(self.queue, item)
        print(f"{item} inserted successfully.")

    # Remove highest priority element
    def dequeue(self):
        if self.is_empty():
            print("Priority Queue is Empty!")
        else:
            item = heapq.heappop(self.queue)
            print(f"Removed element: {item}")

    # View highest priority element
    def peek(self):
        if self.is_empty():
            print("Priority Queue is Empty!")
        else:
            print(f"Highest Priority Element: {self.queue[0]}")

    # Check whether queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display queue
    def display(self):
        if self.is_empty():
            print("Priority Queue is Empty!")
        else:
            print("Priority Queue:", self.queue)
# Create Priority Queue
pq = PriorityQueue()
while True:
    print("\n\tPRIORITY QUEUE MENU")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Check Empty")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            item = int(input("Enter element to insert: "))
            pq.enqueue(item)
        case 2:
            pq.dequeue()
        case 3:
            pq.peek()
        case 4:
            pq.display()
        case 5:
            if pq.is_empty():
                print("Priority Queue is Empty.")
            else:
                print("Priority Queue is not Empty.")
        case 6:
            print("Exiting Priority Queue Program...")
            break
        case _:
            print("Invalid Choice! Please enter a number between 1 and 6.")