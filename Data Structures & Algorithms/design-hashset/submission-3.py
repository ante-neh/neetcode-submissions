class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self, initialCapacity = 10009):
        self.capacity = initialCapacity
        self.count = 0
        self.loadFactor = 0.75
        self.set = [ListNode(-1) for i in range(self.capacity)]

    def hash(self, key: int, capacity: int) -> int:
        return key % capacity

    def add(self, key: int) -> None:
        if ((self.count + 1) / self.capacity) >= self.loadFactor:
            self.resize()

        index = self.hash(key, self.capacity)
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next

        cur.next = ListNode(key)
        self.count += 1

    def remove(self, key: int) -> None:
        index = self.hash(key, self.capacity)
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                self.count -= 1
                return

            cur = cur.next

        
    def contains(self, key: int) -> bool:
        index = self.hash(key, self.capacity)
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                return True

            cur = cur.next

        return False

    def resize(self) -> None:
        newCapacity = self.capacity * 2
        newSet = [ListNode(-1) for _ in range(newCapacity)]

        for head in self.set:
            cur = head.next
            while cur:
                newIndex = self.hash(cur.key, newCapacity)
                newHead = newSet[newIndex]

                newNode = ListNode(cur.key)

                newHead.next = newNode

                cur = cur.next

        self.capacity = newCapacity
        self.set = newSet


# This is dynamic sized hashset implementation. 
# Generally when the load factor is higher than 0.75 searching through the linked list degrade significantly i.e where load factor is the ration of the number of elements to the size of the set 
# We can say the time complexity is now amortized O(1) because we resize the set infrequently 

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)