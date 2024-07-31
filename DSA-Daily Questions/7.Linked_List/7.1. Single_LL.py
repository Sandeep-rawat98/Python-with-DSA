class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None  ### By default head is none if consider SLL is created


node1 = Node(5)
node2 = Node(76)
node3 = Node(32)
node4 = Node(90)

sll = SinglyLinkedList()
print(sll)  ## Address of SLL object
# print(sll.head) ## As no head

sll.head = node1
# print(sll.head)  ## Address of node 1
# print(node1)  ## Same address as node 1 and head is same

sll.head.next = node2  # both works either way
# node1.next=node2   # both works either way as head is node 1
node2.next = node3
node3.next = node4

print(sll.head.val)
print(
    sll.head.next.next.next.val
)  ## value of node 4 wull be output or print(node1.next.next.next.val)

# node1.next = node2
# node2.next = node3
# node3.next = node4

# print(node1)  ## Address of the object
# print(node1.val)
# print(node1.next)  ## Address of the node2
# print(node1.next.val)  ## value of the node2
# print(node1.next.next.next.val)  ## value of the node4 (iterate likewise)


"""
If head is set we can make methods like traverse,count,insert,remove for easier and less lines of codes
"""
 