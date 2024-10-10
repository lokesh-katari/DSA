#  we have to implement a stack with the basic implementation but  the thing is it requires a 
# operation which get the min of the stack in constant time 
# for acheving this we can use the another stack which gets track of min element at each level 
# 

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack:

    def __init__(self):
        self.st = []
        self.minst = []

    def push(self, val: int) -> None:
        self.st.append(val)
        val = min(val , self.minst[-1] if self.minst else val)
        self.minst.append(val)

    def pop(self) -> None:
        
        self.minst.pop()
        self.st.pop()
    def top(self) -> int:
            return self.st[-1]

    def getMin(self) -> int:
            return self.minst[-1]


st = MinStack()
print(st.push(1000))
print(st.pop())
print(st.push(100))
print(st.push(-1))
print(st.push(1))
print(st.push(0))
print(st.getMin())
print(st.top())