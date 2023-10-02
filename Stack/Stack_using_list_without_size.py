class Stack:

    # Creating the empty stack
    def __init__(self):
        self.list = []

    # Display all the elements in the stack
    def display(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    # Adding the elements in the stack
    def push(self, value):
        self.list.append(value)
        return 'value added successfully'
    
    # Checking the stack is empty or not
    def is_Empty(self):
        if self.list == 0:
            return True
        else:
            return False
    
    # Deleting the last element
    def pop(self):
        if self.is_Empty():
            return 'Not possible'
        else:
            return self.list.pop()

    # Viewing the first element
    def peek(self):
        if self.is_Empty():
            return 'This is empty'
        else:
            return self.list[len(self.list)-1]
        
    # Deleting the all the elements   
    def delete(self):
        self.list = None

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.is_Empty())
stack.push(30)
print(stack.peek())
print(stack.display())