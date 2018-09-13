class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head:
            self.head.appendToTail(val)
        else:
            self.head = Node(val)

    def delete(self, val):
        if self.head.val == val:
            self.head = None
        else:
            self.head.delete(val)
    
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

sll = SinglyLinkedList()
sll.insert(4)
sll.insert(3)
sll.insert(2)
sll.insert(1)
print(sll.head.next.next.val)
sll.delete(2)
print(sll.head.next.next.val)

