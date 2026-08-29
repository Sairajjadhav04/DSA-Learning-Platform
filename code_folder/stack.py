# Python Program for Stack ADT using Array
class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [0] * size
        self.top = -1
    # Push Operation
    def push(self, element):
        if self.top == self.size - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = element
            print(f"{element} entered in the stack successfully")
    # Pop Operation
    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            print("Pop element:", self.stack[self.top])
            self.top -= 1
    # Peek Operation
    def peek(self):
        if self.top == -1:
            print("Stack is Empty")
        else:
            print("Top element is:", self.stack[self.top])
    # Check Stack is Empty
    def is_empty(self):
        return self.top == -1
    # Check Stack is Full
    def is_full(self):
        return self.top == self.size - 1
    # Display Stack
    def display(self):
        if self.top == -1:
            print("Stack is Empty, Nothing to display")
        else:
            print("Stack elements are:")
            for i in range(0,self.top+1):
                print(self.stack[i])
# Main Program
size = int(input("Enter the size of stack: "))
s = Stack(size)
while True:
    print("\n\tStack Operation Menu \n")
    print("1. Push Operation")
    print("2. Pop Operation")
    print("3. Peek Operation")
    print("4. Check Stack is Empty")
    print("5. Check Stack is Full")
    print("6. Display Stack")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            element = int(input("Enter the element to enter: "))
            s.push(element)
        case 2:
            s.pop()
        case 3:
            s.peek()
        case 4:
            if s.is_empty():
                print("Stack is Empty")
            else:
                print("Stack is not Empty")
        case 5:
            if s.is_full():
                print("Stack is Full")
            else:
                print("Stack is not Full")
        case 6:
            s.display()
        case 7:
            print("Program ended!!!")
            break
        case _:
            print("Invalid choice, Please enter correct choice")