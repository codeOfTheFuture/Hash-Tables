# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __str__(self):
        return f'<{self.key}, {self.value}'
class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.size = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        if self.size >= self.capacity:
            self.resize()
        index = self._hash_mod(key)
        if self.storage[index]:
            pair = self.storage[index]
            while pair:
                if pair.key == key:
                    pair.value = value
                    return
                if pair.next:
                    pair = pair.next
                else:
                    pair.next = LinkedPair(key, value)
                    return
        else:
            self.storage[index] = LinkedPair(key, value)
            self.size += 1
        

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        pair = self.storage[index]
        while pair:
            if pair.next is None:
                if pair.key == key:
                    self.storage[index] = None
                    return
            else:
                prev_pair = pair
                pair = pair.next
                next_pair = pair.next

                if pair.key == key:
                    prev_pair.next = next_pair
                    pair = None
        print('key does not exist')
        return None

            


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            pair = self.storage[index]
            while pair:
                if pair.key == key:
                    return pair.value
                else:
                    pair = pair.next
            return None
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        old_ht = self.storage
        self.storage = [None] * self.capacity

        for pair in old_ht:
            temp = pair
            while temp:
                self.insert(temp.key, temp.value)
                temp = temp.next

        
                
            
            
ht = HashTable(8)

ht.insert("key-0", "val-0")
ht.insert("key-1", "val-1")
ht.insert("key-2", "val-2")
ht.insert("key-3", "val-3")
ht.insert("key-4", "val-4")
ht.insert("key-5", "val-5")
ht.insert("key-6", "val-6")
ht.insert("key-7", "val-7")
ht.insert("key-8", "val-8")
ht.insert("key-9", "val-9")

return_value = ht.retrieve("key-0")
print(return_value)
return_value = ht.retrieve("key-1")
print(return_value)
return_value = ht.retrieve("key-2")
print(return_value)
return_value = ht.retrieve("key-3")
print(return_value)
return_value = ht.retrieve("key-4")
print(return_value)
return_value = ht.retrieve("key-5")
print(return_value)
return_value = ht.retrieve("key-6")
print(return_value)
return_value = ht.retrieve("key-7")
print(return_value)
return_value = ht.retrieve("key-8")
print(return_value)
return_value = ht.retrieve("key-9")
print(return_value)



# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")
