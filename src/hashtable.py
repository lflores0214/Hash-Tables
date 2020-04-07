# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"<{self.key},{self.value}"


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

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
        # * Class solution
        # # hashmod the key to find the bucket
        # index = self._hash_mod(key)

        # # check if a pair already exists in the bucket
        # pair = self.storage[index]
        # if pair is not None:
        #     if pair.key != key:
        #         # if so overwrite the keyvalue and throw a warning
        #         print("warning: overwriting value")
        #         pair.key = key
        #     pair.value = value
        #     # if not create a new linked pair and place it in the bucket
        # else:
        #     self.storage[index] = LinkedPair(key, value)

        # * Day 1
        # # hash the key and make it the index
        # index = self._hash_mod(key)

        # # check for collisions and return an error message if there is one
        # if self.storage[index] is not None:
        #     print("ERROR: item already exists at this index")
        #     return
        # # if there is not a collision add the key: value
        # else:
        #     self.storage[index] = LinkedPair(key,value)
            
        # * Day 2
        # hash the key and make it the index
        index = self._hash_mod(key)
        pair = self.storage[index]
        # set temp variable to store current pair before it gets overwritten
        temp = None
        # check for collisions
        if pair is None:
            # if there is not a collision  add the key: value
            self.storage[index] = LinkedPair(key, value)
            return
        # if there is a collision loop through the list until you reach a node without a next value and set the key: value as next
        while pair is not None:
            # if there is a collision and keys are the same overwrite value
            if pair.key == key:
                pair.value = value
            temp = pair
            pair = pair.next
        # if we reach the end append the new node there
        temp.next = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # * Class Solution
        # index = self._hash_mod(key)
        # #check if a pair exists in the bucket with matching keys
        # if self.storage[index] is not None and self.storage[index].key == key:
        #     #if so remove the pair
        #     self.storage[index] = None
        # else:
        #     #else print warning
        #     print("Warning: Key does not exist ")

        # * My solution
        # hash the key and make it the index
        index = self._hash_mod(key)
        # check if the key exists
        if self.storage[index] == None:
            # if it doesn't, print error
            print("key not found")
            return
        else:
            # if it does remove it
            self.storage[index] = None
            return self.storage[index]

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # * Class Solution
        # index = self._hash_mod(key)

        # #check if a pair exists in the bucket with matching keys
        # if self.storage[index] is not None and self.storage[index].key == key:
        #     # if so return the value
        #     return self.storage[index].value
        # else:
        #     # else return none
        #     return None

        # # * Day 1
        # # hash the key and make it the index
        # index = self._hash_mod(key)
        # # check if key is in storage
        # if self.storage[index] == None:
        #     # if it is print error message and return
        #     print("ERROR: No item at this index")
        #     return None
        # else:
        #     # if it isn't return the value
        #     return self.storage[index].value

        # * Day 2
        # hash the key and make it the index
        index = self._hash_mod(key)
        pair = self.storage[index]
        # loop through the linked list at the given index until the keys match
        while pair is not None:
            # if the keys match return the value
            if pair.key == key:
                return pair.value
            # set pair to pair.next to keep the loop going
            pair = pair.next

        # if the key is not found, return None
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # double capacity
        self.capacity *= 2
        # make new storage with new capacity
        new_storage = [None] * self.capacity
        # copy all items over
        for item in range(len(self.storage)):
            new_storage[item] = self.storage[item]
        self.storage = new_storage
        print(self.storage)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
