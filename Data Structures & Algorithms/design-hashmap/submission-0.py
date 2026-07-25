class ListNode:
    def __init__(self, key, value = 0):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.capacity = 10009
        self.map = [ListNode(-1) for _ in range(self.capacity)]
        
    def hash(self, key: int) -> int:
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        cur = self.map[index]

        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return

            cur = cur.next

        newNode = ListNode(key, value)
        cur.next = newNode

    def get(self, key: int) -> int:
        index = self.hash(key)
        cur = self.map[index]

        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            
            cur = cur.next

        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        cur = self.map[index]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return

            cur = cur.next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)