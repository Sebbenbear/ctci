# Delete Middle Node
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

    # Delete middle node
    def deleteMiddle(self):
        if self.head:
            if self.head.deleteAtIndex(self.size//2-1):
                self.size -= 1
    
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

    def deleteAtIndex(self, idx):
        n = self
        count = 0
        while n:
            if count == idx:
                n.next = n.next.next
                return True
            n = n.next
            count += 1
        return False

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
sll.insert(1)
sll.insert(2)
sll.insert(3)
sll.insert(4)
sll.insert(5)
sll.head.printAll()
sll.deleteMiddle()
sll.head.printAll()
