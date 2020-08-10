class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here'
        self.capacity = capacity

        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY

        self.storage = [None] * self.capacity
        self.items_in_storage = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        # can we just return self.capacity here?
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.items_in_storage/self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash_index = 5381
        hash_bytes = key.encode()

        for byte in hash_bytes:
            hash_index = ((hash_index << 5) + hash_index) + byte
        return hash_index

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        # DAY 1 CODE
        # hash_index = self.hash_index(key)
        # self.storage[hash_index] = HashTableEntry(key, value)

        # DAY 2
        # find the start of the linked list using the index
    # Search through linked list
    # IF the key already exists in the linked list
        # Replace the value
    # Else
        # Add new HashTable Entry to the head of linked list

        hash_index = self.hash_index(key)

        # find an empty spot for new data
        if not self.storage[hash_index]:
            self.storage[hash_index] = HashTableEntry(key, value)
            self.items_in_storage += 1

        # if a linked list already exists at this location
        # we either update the value for an existing key OR create a new entry for the key
        else:
            current = self.storage[hash_index]

            while current.key != key and current.next:
                current = current.next

            # find the key and update its current value
            if current.key == key:
                current.value = value

            # if key not found, we just add a new node entry
            else:
                current.next = HashTableEntry(key, value)
                self.items_in_storage += 1

        if self.get_load_factor() > 0.7:
            self.resize(self.capacity*2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # first need to hash the key
        # DAY 1 CODE
        # hash_index = self.hash_index(key)
        # # check if value in array, if it is set it to None
        # if self.storage[hash_index] is not None:
        #     self.storage[hash_index] = None
        # else:
        #     print("Key not found")

        # DAY 2 CODE

        hash_index = self.hash_index(key)
        current = self.storage[hash_index]

        while current.next != None:
            if current.key == key:
                current.value = None
                return

            else:
                current = current.next
        if current.next == None:
            if current.key == key:
                current.value = None

        # resize if load factor is too small

        if self.get_load_factor() < 0.2:
            self.resize(self.capacity // 2)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        # DAY 1 CODE
        # hash_index = self.hash_index(key)
        # if self.storage[hash_index] is not None:
        #     return self.storage[hash_index].value
        # else:
        #     return None

        # DAY 2 CODE

        hash_index = self.hash_index(key)
        current = self.storage[hash_index]
        while current != None:
            # if key exists
            if current.key == key:
                return current.value
            current = current.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        old_data = self.storage

        # init new hash table
        self.capacity = new_capacity
        self.storage = [None] * new_capacity

        # loop through and add each node to new hashtable

        for i in old_data:
            if i:
                current = i
                while current:
                    self.put(current.key, current.value)
                    current = current.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
