# Write code to remove duplicates from an unsorted linked list. 
# FOLLOW UP How would you solve this problem if a temporary buffer is not allowed?

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

    # First Iteration
    def removeDups1(self):
        n = self.head
        node_set = {n.val}
        while n:
            if n.next:
                if n.next.val in node_set:
                    n.next = n.next.next
                    continue
                else:
                    node_set.add(n.next.val)
            n = n.next

    # Second Iteration
    def removeDups(self):
        n = self.head
        node_set = {n.val}
        while n.next:
            if n.next.val in node_set:
                n.next = n.next.next
                continue
            else:
                node_set.add(n.next.val)
            n = n.next

    def printAll(self):
        if self.head:
            self.head.printAll()
    
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

    def printAll(self):
        result = ""
        n = self
        while n:
            result += str(n.val)
            n = n.next
        print(result)

sll = SinglyLinkedList()
sll.insert(4)
sll.insert(4)
sll.insert(4)
sll.insert(4)
sll.insert(5)
sll.insert(5)
sll.printAll()
sll.removeDups()
sll.printAll()