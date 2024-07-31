class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    def traverse(self):
        if self.head is None:
            print("SLL is empty, cannot traverse")
            return
        temp = self.head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()
    def insertAtStart(self, value):
        pass

sll = SinglyLinkedList()
sll.append(100)
sll.append(200)
sll.append(500)
sll.append(300)
sll.traverse()