class Queue:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
  def __init__(self):
    self.queue = []
    self.total = self.size()
    pass
  
  def __repr__(self):
    return str(self.queue)
  def enqueue(self, data):
    # write your code to add data to the Queue following FIFO and return the Queue
    self.queue.append(data)
    self.total = self.size()
    return self.queue
    pass

  def dequeue(self):
    # write your code to removes the data to the Queue following FIFO and return the Queue
    self.queue.pop(0)
    self.total = self.size()
    return self.queue
    pass

  def size(self):
    # write your code that returns the size of the Queue
    return len(self.queue)
    pass
testQ = Queue()
testQ.enqueue(613)
testQ.enqueue("Mark")
testQ.dequeue()
print(testQ)