# What is an array and how does it work?

# Stores a sequence of elements
# Each element must be the same data type
# Occupies a contiguous block of memory
# Can access data in constant time with this equation: memory_address = starting_address + index * data_size


class DynamicArray:
  def __init__(self, capacity=1):
    self.count = 0 # Number of elements in the array
    self.capacity = capacity # Total amount of storage in the array
    self.storage = [None] * capacity

  def insert(self, index, value):
    #  Check if we have enough capacity
    if self.count >= self.capacity:
      # If not, add more capacity
      self.resize()
    # Shift over every item after index to the right by 1
    for i in range(self.count, index, -1):
      self.storage[i] = self.storage[i-1]
    # Add the new value to the index
    self.storage[index] = value
    # Increment count
    self.count += 1

  def append(self, value):
    # O(1) (most of the time)
    # Check if we have enough capacity
    if self.count >= self.capacity:
      # If not, double the size
      self.resize()
    # Add value to the index of count
    self.storage[self.count] = value
    # Increment count
    self.count += 1


  def resize(self):
    # Double capacity
    self.capacity *= 2
    #  Allocate a new storage array with double capacity
    new_storage = [None] * self.capacity
    # Copy all elements from ofl storage to new
    for i in range(self.count):
      new_storage[i] = self.storage[i]
    self.storage = new_storage


a = DynamicArray(2)
a.insert(0, 10)
a.insert(0, 11)
a.append(9)
a.append(8)
print(a.storage)
a.append(7)

print(a.storage)


# O(n^2)
def add_to_front(n):
  x = []
  for i in range(0, n):
    x.insert(0, n - 1)
  return x

# O(n)
def add_to_back(n):
  x = []
  for i in range(0, n):
    x.append(i + 1)
  return x

# O(n)
def pre_allocate(n):
  x = [None] * n
  for i in range(0, n):
    x[i] = i + 1
  return x

n = 500000        # n = 500 thousand
add_to_back(n)    # 0.0752... seconds
pre_allocate(n)   # 0.0526... seconds

