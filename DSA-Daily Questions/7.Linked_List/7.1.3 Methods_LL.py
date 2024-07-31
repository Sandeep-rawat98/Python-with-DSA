"""
1. Append

First Case if SLL is empty
Second case if SLL is not empty
"""

"""
2. Traverse

First Case if SLL is empty
Second case if SLL is not empty
"""

"""
3. InsertAtStart

First Case if SLL is empty
Second case if SLL is not empty
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

    def InsertAtStart(self, value):
        new_node = Node(value)
        # if not self.head:
        if self.head is None:
            self.head = new_node
            # self.length = 1
        else:
            new_node.next = self.head  ## to make a connection with new node to next one
            self.head = new_node  ### then change the self
            # self.length += 1


sll = SinglyLinkedList()
# sll.traverse()  ### SLL is empty,cannot traverse
sll.append(100)
sll.append(200)
sll.append(300)
sll.append(400)
sll.append(500)
# sll.append([23, 56, 78, 9, 0])
# sll.traverse()  ##100 200 300 400 500 [23, 56, 78, 9, 0]
sll.InsertAtStart(600)
sll.traverse()
