class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
  def __init__(self):
    self.stack = []
    self.total = self.size()
    pass
  def push(self, data):
    # write your code to add data following LIFO and return the Stack
    self.stack.insert(0,data)
    self.total = self.size()
    pass

  def pop(self):
    # write your code to removes the data following LIFO and return the Stack
    self.stack = self.stack[1:]
    self.total = self.size()
    pass

  def size(self):
    # write your code that returns the size of the Stack
    return len(self.stack)
    pass
  
test = Stack()
test.push(1)
test.push(23)
test.pop()
print(test.stack)
print(test.total)