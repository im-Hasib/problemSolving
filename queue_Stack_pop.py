# pop operation costly

class StackUsingQueue:
    def __init__(self):
        self.q1 = []  # Main queue
        self.q2 = []  # Temporary queue

    def push(self, x):
        self.q1.append(x)  # Efficient push (O(1))

    def pop(self):
        if not self.q1:
            return "Stack is empty"

        # Move all elements except the last to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))  # Manually mimicking queue dequeue

        # Remove the last element (top of stack)
        popped_element = self.q1.pop(0)

        # Swap q1 and q2 to maintain order
        self.q1, self.q2 = self.q2, self.q1

        return popped_element

    def top(self):
        if not self.q1:
            return "Stack is empty"

        return self.q1[-1]  # The last inserted element is the top of the stack

    def is_empty(self):
        return len(self.q1) == 0

# Testing the stack
stack = StackUsingQueue()
stack.push(1)
stack.push(2)
stack.push(3)

print("Top element:", stack.top())  # Output: 3
print("Popped:", stack.pop())       # Output: 3
print("Top element:", stack.top())  # Output: 2
print("Popped:", stack.pop())       # Output: 2
print("Top element:", stack.top())  # Output: 1
print("Popped:", stack.pop())       # Output: 1
print("Stack empty:", stack.is_empty())  # Output: True
