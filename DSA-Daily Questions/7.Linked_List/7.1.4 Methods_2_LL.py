"""
4. Insert (value, index)
"""

"""
5. Delete Head 

First case SLL is empty
second case sll is not emopty
"""


class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        # self.length = 0  ## to track the length

    def append(self, data):  ## append--  one value or data
        new_node = Node(data)
        # if self.head is None:
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next  ## do until you find the current next as None
            current.next = (
                new_node  ## Once current next is none to uska next new _node for append
            )

    def traverse(self):
        # if self.head is None:
        if not self.head:
            print("SLL is empty,cannot traverse")
        else:
            current = self.head
            while current is not None:  ## if at last it reach and next is none
                print(current.val, end=" ")
                current = current.next
            print()

    def insert(self, value, index):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            count = 0
            while temp:
                count += 1
                if count == index:
                    break
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    ##a sk anriudh about to handle at last posiiton

    def deleteHead(self):
        if self.head is None:
            print("Cannot Delete,SLL is empty")
            return
        self.head = self.head.next

    def deletebyValue(self, value):
        if self.head is None:
            print("Cannot Delete,SLL is empty")
            return
        temp = self.head
        if temp.val == value:  ## if sinlge node '
            self.head = self.head.next
        else:
            found = False
            while temp is not None:
                if temp.val == value:
                    found = True
                    break
                prev = temp
                temp = temp.next
            if found:
                prev.next = temp.next
            else:
                print("Node not found")


sll = SinglyLinkedList()
sll.append(100)
sll.append(200)
sll.append(300)
sll.append(400)
sll.append(500)
sll.traverse()
sll.insert(1000, 3)
sll.traverse()
sll.insert(1000, 35)
sll.traverse()
sll.deletebyValue(700)
sll.traverse()
