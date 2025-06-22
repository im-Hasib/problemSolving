#  push operation costly

class StackUsingQueue:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self,x):
        while self.q1 :
            self.q2.append(self.q1.pop(0))
    
        self.q1.append(x)

        while self.q2 :
            self.q1.append(self.q2.pop(0))
    
    def pop(self) :

        if self.q1: 
            return self.q1.pop(0)

        return "Stack is empty"
    
    def peek(self):

        if self.q1: 
            return self.q1[0]

        return "Stack is empty"
    
    def is_empty(self):
        return len(self.q1) == 0


