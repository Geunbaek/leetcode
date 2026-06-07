class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):

        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
       
        if index > self.size:
            return
       
        if index < 0:
            index = 0
            
        self.size += 1
        pred = self.head
        
        for _ in range(index):
            pred = pred.next
            
        to_add = ListNode(val)
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        
        if index < 0 or index >= self.size:
            return
        
        self.size -= 1
        pred = self.head
        
        for _ in range(index):
            pred = pred.next
            
        pred.next = pred.next.next