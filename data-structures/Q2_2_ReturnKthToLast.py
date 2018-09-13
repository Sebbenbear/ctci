# Find the Kth to last element of a linked list

# Runtime: O(n), since we only go through the list once
# Memory: O(1), since we keep track of a the size, and just calculate the idx we need
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def getCount(self):
        return self.size

    def insert(self, val):
        if self.head:
            self.head.appendToTail(val)
        else:
            self.head = Node(val)
        self.size += 1

    def delete(self, val):
        if self.head.val == val:
            self.head = None
        else:
            self.head.delete(val)
        self.size -= 1

    # Return the Kth to last value
    def findKthToLast(self, idx):
        if self.head:
            return self.head.find(self.size - idx - 1) # so 0 should return the last element
        else:
            return -1 # could also throw an exception here
    
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def appendToTail(self, val):
        n = self
        while n.next:
            n = n.next
        n.next = Node(val)

    def delete(self, val):
        n = self
        while n.next:
            if val == n.next.val:
                n.next = n.next.next
                break
            n = n.next

    def find(self, idx):
        count = 0
        n = self
        while n:
            if count == idx:
                return n.val
            n = n.next
            count += 1
        return -1

    def printAll(self):
        result = ""
        n = self
        while n:
            result += str(n.val)
            n = n.next
        print(result)

sll = SinglyLinkedList()
print(sll.getCount())
sll.insert(1)
sll.insert(2)
sll.insert(3)
print(sll.getCount())
sll.insert(4)
print(sll.findKthToLast(2))
print(sll.findKthToLast(0))