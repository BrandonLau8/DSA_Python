# Implement a stack using array or linked list.
class StackArray:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    def is_empty(self):
        return len(self.stack)==0
    def display(self):
        print('Stack  (top -> bottom):', self.stack[::-1])
        
s = StackArray()
s.push(10)
s.push(20)
s.push(30)
s.display()       # Stack (top -> bottom): [30, 20, 10]
print(s.pop())    # 30
print(s.peek())   # 20
s.display()       # Stack (top -> bottom): [20, 10]

# Implement a queue using array or linked list.

# Check for balanced parentheses.

# Evaluate a postfix expression.

# Sliding window maximum (for queues).